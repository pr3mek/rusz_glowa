import html

from flask import Flask, render_template, request, escape
from mymodules.vsearch import search4letters, log_request

app = Flask(__name__)


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
    contents = []
    with open('vsearch.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('Dane z formularza', 'Adres klienta', 'Agent użytkownika', 'Wyniki')
    return render_template('viewlog.html',
                           the_title='Widok logu',
                           the_row_titles=titles,
                           the_data=contents,)


@app.route('/')
@app.route('/entry')
def entry_page():
    return render_template('entry.html', the_title='Witamy na naszej stronie search4letters!')


if __name__ == '__main__':
    app.run(debug=True)
