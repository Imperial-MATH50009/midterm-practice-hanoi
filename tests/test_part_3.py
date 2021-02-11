import pytest


@pytest.mark.parametrize("input, board", [
    (3, '> 4, 3, 2\n> \n> '),
    (0, '> \n> \n> ')
])
def test_str(input, board):
    from hanoi.hanoi import Game
    assert Game(input).__str__() == board
