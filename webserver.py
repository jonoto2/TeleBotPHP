from flask import Flask
from threading import Thread

app = Flask('')


@app.route('/')
def home():
    return '<div style="height: 100%;display: flex;justify-content: center;align-content: center;flex-wrap: wrap;"><h1 style="font-family: sans-serif;">Шарманка Работает!</h1></div>'


def run():
    app.run(host='0.0.0.0', port=8080)


def keep_alive():
    t = Thread(target=run)
    t.start()
