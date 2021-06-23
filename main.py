from flask import Flask, render_template, abort, request, redirect, url_for


app = Flask(__name__)


@app.route('/')
@app.route('/index.html')
def index():
    # categories = models.ProductDB(PRODUCT_DB).get_categories()
    # return render_template('index.html', categories=categories)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
