import unicodedata
import re
from numbers import Number


def slugify(value):
    """
    Zamienia podany string w slug:
    - Zamiana na małe litery.
    - Zamiana spacji na myślniki.
    - Usunięcie diakrytyków (w tym polskich znaków jak 'ł' -> 'l').
    - Usunięcie niedozwolonych znaków.
    """

    if isinstance(value, Number):
        value = str(value)

    # Mapa do ręcznej zamiany polskich znaków na odpowiedniki bez ogonków
    polish_char_map = {
        'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n',
        'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z'
    }

    # Zamiana polskich znaków na odpowiedniki
    for polish_char, ascii_char in polish_char_map.items():
        value = value.replace(polish_char, ascii_char).replace(polish_char.upper(), ascii_char.upper())

    # Usunięcie innych diakrytyków
    value = unicodedata.normalize('NFKD', value)
    value = ''.join(c for c in value if not unicodedata.combining(c))

    # Zamiana na małe litery
    value = value.lower()

    # Zamiana niedozwolonych znaków na spacje
    value = re.sub(r'[^a-z0-9\s-]', '', value)

    # Zamiana wielokrotnych spacji i myślników na jeden myślnik
    value = re.sub(r'[\s-]+', '-', value)

    # Usunięcie myślników na początku i końcu
    value = value.strip('-')

    return value
