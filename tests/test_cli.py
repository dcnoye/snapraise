# Author: D.C. Noye <dcnoye@gmail.com>

from app.commands import pcalc

def test_postfix():
    # Try some data we know
    test_data = "5 5 5 8 + + -"
    assert pcalc.postfix(test_data)==-13

    # Try some data we know
    more_data = "25 1 2 + 3 * -"
    assert pcalc.postfix(test_data)==16
