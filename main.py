from flask import Flask, render_template, abort, request, redirect, url_for

from models import TestDB


app = Flask(__name__)


@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/db_conn_check.html')
def db_conn_check():
    users = TestDB().get_test_data()
    return render_template('db_conn_check.html', users=users)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
