# -*- coding: utf-8 -*-
from persefone.sqlalchemy import Siren

from pytest import raises


def test_sqlalchemy():

    with raises(NotImplementedError):
        Siren({}, '/path').encode()
