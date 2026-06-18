import pytest
import numpy as np
import pandas as pd
import matplotlib
import seaborn

from find_single import find_single


# --- Normalfälle ---

def test_beispiel_aus_aufgabe():
    """Testfall aus der Aufgabenstellung: [1,2,3,4,3,1,2] -> 4."""
    assert find_single([1, 2, 3, 4, 3, 1, 2]) == 4


def test_einzelnes_element():
    """Liste mit nur einem Element gibt dieses zurück."""
    assert find_single([7]) == 7


def test_erstes_element_ist_einzeln():
    """Das einzelne Element steht am Anfang der Liste."""
    assert find_single([5, 1, 1, 2, 2]) == 5


def test_letztes_element_ist_einzeln():
    """Das einzelne Element steht am Ende der Liste."""
    assert find_single([3, 3, 9, 9, 42]) == 42


def test_negative_zahlen():
    """Funktioniert auch mit negativen Zahlen."""
    assert find_single([-1, -2, -1]) == -2


def test_grosse_zahlen():
    """Funktioniert mit großen Integer-Werten."""
    assert find_single([10**9, 10**9, 99]) == 99


# --- Randfälle / ungültige Eingaben ---

def test_leere_liste_wirft_fehler():
    """Leere Liste soll ValueError auslösen."""
    with pytest.raises(ValueError):
        find_single([])


def test_gerade_laenge_wirft_fehler():
    """Liste mit gerader Länge ist ungültig."""
    with pytest.raises(ValueError):
        find_single([1, 2])


def test_kein_list_wirft_fehler():
    """Nicht-Listen-Eingabe soll TypeError auslösen."""
    with pytest.raises(TypeError):
        find_single((1, 2, 1))


def test_bibliotheken_importierbar():
    """Stellt sicher, dass numpy, pandas, matplotlib und seaborn installiert sind."""
    assert np.__version__ is not None
    assert pd.__version__ is not None
    assert matplotlib.__version__ is not None
    assert seaborn.__version__ is not None
