from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/steamie2')
def steamie():
    c.execute('SELECT * from chosen')
    output = c.fetchall()
    outlist = []
    for i in range(5):
        outlist.append(output.pop())
    return "Boob"

if __name__ == '__main__':
    db = 'steamie.db'
    schema = 'schema.sql'
    conn = sqlite3.connect(db)
    c = conn.cursor()
    app.run()
