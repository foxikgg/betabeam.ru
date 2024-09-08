from flask import Flask, request, render_template
import time


application = Flask(__name__)


@application.route('/')
def index():
    return render_template('index.html', time=time)


if __name__ == '__main__':
    application.run(debug=True)