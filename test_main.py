import pytest
from main import name


def test_name():
  assert name() == 'yo face'