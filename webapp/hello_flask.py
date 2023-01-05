from flask import Flask
from mymodules.vsearch import search4letters

app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return 'Witaj w świecie Flask!'


@app.route('/vsearch')
def do_search() -> str:
    return str(search4letters('życie, wszechświat i cała reszta', 'eiru'))


app.run()
