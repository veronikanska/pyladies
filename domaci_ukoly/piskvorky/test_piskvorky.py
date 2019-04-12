import piskvorky
import util
import ai
import pytest

def test_vyhodnoceni():
    assert piskvorky.vyhodnot('xxx' + '-' * 17) == 'x'
    assert piskvorky.vyhodnot('ooo' + '-' * 17) == 'o'
    assert piskvorky.vyhodnot('xoxoxoxoxoxoxoxoxoxo') == '!'
    assert piskvorky.vyhodnot('xoxoxoxoxoxoxoxoxox-') == '-'

def test_tah():
    pole = util.tah('-' * 20, 5, 'x')
    assert len(pole) == 20
    assert pole.count('-') == 19
    assert pole.count('x') == 1
    assert pole.index('x') == 5

def test_tah_pocitace_prazdne_pole():
    pole = ai.tah_pocitace('-' * 20, 'o')
    assert len(pole) == 20
    assert pole.count('o') == 1
    assert pole.count('-') == 19

def test_tah_pocitace_neprazdne_pole():
    pole = ai.tah_pocitace('--x-x--o-o---x------', 'o')
    assert len(pole) == 20
    assert pole.count('o') == 3
    assert pole.count('x') == 3
    assert pole.count('-') == 14

def test_tah_pocitace_symbol_x():
    pole = ai.tah_pocitace('x' + '-' * 19, 'o')
    assert pole.count('x') == 1
    assert pole.count('o') == 1

def test_tah_pocitace_symbol_o():
    pole = ai.tah_pocitace('o' + '-' * 19, 'o')
    assert pole.count('x') == 1
    assert pole.count('o') == 1

def test_tah_pocitace_dlouhe_pole():
    pole = ai.tah_pocitace('-' * 25, 'o')
    assert pole.count('o') == 1
    assert pole.count('-') == 24

def test_tah_pocitace_nulove_pole():
    with pytest.raises(ValueError):
        ai.tah_pocitace('', 'o')

def test_tah_pocitace_plne_pole():
    with pytest.raises(ValueError):
        ai.tah_pocitace('xoxoxoxoxoxoxoxoxoxo', 'o')

def test_vklad():
    assert piskvorky.vklad('-' * 20, 'fff') == False
    assert piskvorky.vklad('-' * 20, '100') == False
    assert piskvorky.vklad('-' * 20, '-20') == False
    assert piskvorky.vklad('-' * 20, '1.6') == False
    assert piskvorky.vklad('x' + '-' * 19, '0') == False
    assert piskvorky.vklad('-' * 20, '5') == True

# Nevim, jak mam otestovat funkci piskvorky1d, nema vstup, vraci print,
# Je to jen kus kodu dany do funkce.