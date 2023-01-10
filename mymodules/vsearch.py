def search4vowels(phrase: str) -> set:
    """Wyświetla samogłoski znalezione w podanym słowie"""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    """Sprawdza czy podane znaki (domyślnie samogłoski) znajdują się w podanej frazie"""
    return set(letters).intersection(set(phrase))


def log_request(req: 'flask_request', res: str) -> None:
    """Zapisuje logi dotyczące bieżącego żądania sieciowego, oraz wyniku wyszukiwania podanych liter"""

    """with open('vsearch.log', 'a') as log:
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')"""
