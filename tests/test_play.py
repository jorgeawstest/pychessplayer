import pytest
import sys
sys.path.insert(0, "pychessplayer")
from pychessplayer.play import get_board



def test_get_board():
    value = get_board()
    assert value == "aaa"    