import pytest
import sys
sys.path.insert(0, "pychessplayer")
from pychessplayer.board import Board

def test_init():
    board = Board()
    assert board.sayhello() == "hello"

