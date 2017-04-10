# -*- coding: utf-8 -*-
import pytest
from persefone import Siren

def test_siren_encode():
    siren = Siren()
    assert type(siren.encode()) == dict
