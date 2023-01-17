import html

from flask import Flask, render_template, request, escape
from mymodules.vsearch import search4letters
from DBcm import UseDatabase

app = Flask(__name__)

app.config['dbconfig'] = {'host': 's177.cyber-folks.pl',
                          'user': 'nnmyhiacdt_rusz_glowa',
                          'password': 'Pandi1992cao@',
                          'database': 'nnmyhiacdt_rusz_glowa', }

# def fav_letter() -> str:
#     with UseDatabase(app.config['dbconfig']) as cursor:
#         _SQL = """select count(letters) as 'count', letters
#                     from logs
#                     group by letters
#                     order by count desc
#                     limit 1"""
#         return cursor.execute(_SQL)

# def count_search() -> str:
#     with UseDatabase(app.config['dbconfig']) as cursor:
#         _SQL = """select count(*) from logs"""
#         return cursor.execute(_SQL)


def log_request(req: 'flask_request', res: str) -> None:
    """Zapisuje logi dotyczące bieżącego żądania sieciowego, oraz wyniku wyszukiwania podanych liter"""
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """INSERT INTO logs
                (phrase, letters, ip, browser_string, results)
                values
                (%s, %s, %s, %s, %s)"""
        cursor.execute(_SQL, (req.form['phrase'],
                              req.form['letters'],
                              req.remote_addr,
                              req.user_agent.browser,
                              res,))


@app.route('/search4', methods=['POST'])
def do_search():
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = "Oto Twoje wyniki: "
    results = str(search4letters(phrase, letters))
    log_request(request, results)
    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results, )


@app.route('/viewlog')
def view_the_log() -> 'html':
    """Wyświetla zawartość pliku logu w postaci tabeli HTML"""
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """select phrase, letters, ip, browser_string, results
                    from logs"""
        cursor.execute(_SQL)
        contents = cursor.fetchall()
    titles = ('Fraza', 'Litery', 'Adres klienta', 'Agent użytkownika', 'Wyniki')
    return render_template('viewlog.html',
                           the_title='Widok logu',
                           the_row_titles=titles,
                           the_data=contents, )


@app.route('/')
@app.route('/entry')
def entry_page():
    # count = count_search()
    # letters = fav_letter()
    return render_template('entry.html',
                           the_title='Witamy na naszej stronie search4letters!')


if __name__ == '__main__':
    app.run(debug=True)
