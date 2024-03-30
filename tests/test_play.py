import pytest
from com.jorgeawstest.pychessplayer.play import *


def test_get_board():
    value = get_board()
    assert value == "aaa"    