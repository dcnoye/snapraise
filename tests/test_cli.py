# Author: D.C. Noye <dcnoye@gmail.com>

from app.commands import pcalc

def test_postfix():
    test_data = "5 5 5 8 + + -"
    
    assert pcalc.postfix(test_data)==-13
