import sibenice
import pytest

def test_tah():
    pole = sibenice.tah('tulipan', '-------', 'a')
    assert len(pole) == 7
    assert pole.count('-') == 6
    assert pole.count('a') == 1
    assert pole.index('a') == 5

def test_overeni():
    assert sibenice.overeni('fff', '-------') == False
    assert sibenice.overeni('5', '-------') == False
    assert sibenice.overeni('!', '-------') == False
    assert sibenice.overeni('a', '---a---') == False
    assert sibenice.overeni('z', '-------') == True
    assert sibenice.overeni('H', '-------') == True

def test_kolo():
    assert sibenice.kolo(0, 'tulipan', '-------', 'a') == ('-----a-', 0, '///')
    assert sibenice.kolo(0, 'tulipan', '-------', 'e') == ('-------', 1, '+++')
    
   