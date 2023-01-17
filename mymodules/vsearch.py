import mysql.connector
from flask import app


def search4vowels(phrase: str) -> set:
    """Wyświetla samogłoski znalezione w podanym słowie"""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    """Sprawdza czy podane znaki (domyślnie samogłoski) znajdują się w podanej frazie"""
    return set(letters).intersection(set(phrase))




