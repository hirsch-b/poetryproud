import pytest

from poetryproud import haiku
from poetryproud import regular


def test_random_haiku():
    poem = haiku.get_random()
    assert poem is not None
    assert "author" in poem
    assert "haiku" in poem


def test_random_regular():
    poem = regular.get_random()
    assert poem is not None
    assert "author" in poem
    assert "poem" in poem
