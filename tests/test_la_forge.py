#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `la_forge` package."""

import pytest


from la_forge import core
from la_forge import diagnostics
from la_forge import red_noise
from la_forge import slices
from la_forge import utils


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
