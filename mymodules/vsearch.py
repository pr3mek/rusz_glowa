import mysql.connector


def search4vowels(phrase: str) -> set:
    """Wyświetla samogłoski znalezione w podanym słowie"""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    """Sprawdza czy podane znaki (domyślnie samogłoski) znajdują się w podanej frazie"""
    return set(letters).intersection(set(phrase))


def log_request(req: 'flask_request', res: str) -> None:
    """Zapisuje logi dotyczące bieżącego żądania sieciowego, oraz wyniku wyszukiwania podanych liter"""
    dbconfig = {'host': 's177.cyber-folks.pl',
                'user': 'nnmyhiacdt_rusz_glowa',
                'password': 'Pandi1992cao@',
                'database': 'nnmyhiacdt_rusz_glowa', }
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    _SQL = """INSERT INTO LOGS
                (phrase, letters, ip, browser_string, results)
                values
                (%s, %s, %s, %s, %s)"""
    cursor.execute(_SQL, (req.form['phrase'],
                          req.remote_addr,
                          req.user_agent.browser,
                          res, ))
    conn.commit()
    cursor.close()
    conn.close()
