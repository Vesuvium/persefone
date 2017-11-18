# -*- coding: utf-8 -*-
from unittest.mock import MagicMock

from persefone import Siren

from pytest import fixture

import ujson


@fixture
def item():
    return MagicMock()


@fixture
def siren(item):
    return Siren(item, '/path')


@fixture
def siren_with_list(item):
    return Siren([item], '/path')


def test_paginate():
    links = Siren([], 'path', total_items=1, current_page=1).paginate()
    assert links[0] == {'rel': ['self'], 'href': 'path'}
    assert links[1] == {'href': 'path?page=2', 'rel': ['next']}


def test_paginate_middle():
    links = Siren([], 'path', total_items=1, current_page=2).paginate()
    assert links[0] == {'href': 'path', 'rel': ['self']}
    assert links[1] == {'href': 'path?page=3', 'rel': ['next']}
    assert links[2] == {'href': 'path?page=1', 'rel': ['previous']}


def test_paginate_last():
    links = Siren([], 'path', total_items=0, current_page=3).paginate()
    assert links[0] == {'rel': ['self'], 'href': 'path'}
    assert links[1] == {'rel': ['previous'], 'href': 'path?page=2'}


def test_make_entity(siren, item):
    entity = siren.make_entity()
    assert entity['properties'] == item._data
    assert entity['class'] == [item.__class__.__name__]
    assert entity['links'] == [
        {'href': '/path/{}'.format(item.id), 'rel': 'self'}
    ]


def test_make_entities(mocker, siren_with_list):
    mocker.patch.object(Siren, 'make_entity')
    mocker.patch.object(Siren, 'paginate')
    entities = siren_with_list.make_entities()
    assert entities['entities'] == [Siren.make_entity()]
    assert type(entities['actions']) == list
    assert entities['links'] == Siren.paginate()


def test_encode(mocker, siren_with_list):
    mocker.patch.object(Siren, 'make_entities')
    mocker.patch.object(ujson, 'dumps')
    siren_with_list.encode()
    ujson.dumps.assert_called_with(Siren.make_entities())


def test_encode_one(mocker, siren):
    mocker.patch.object(Siren, 'make_entity')
    mocker.patch.object(ujson, 'dumps')
    siren.encode()
    ujson.dumps.assert_called_with(Siren.make_entity())
