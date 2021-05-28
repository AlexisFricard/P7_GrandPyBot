from flask import Flask, render_template, request
import config
import json

from app.grandpy.papybot import GrandPy

app = Flask(__name__)

app.config.from_object('config')


@app.route('/')
def index():
    front_key = config.FRONT_KEY
    return render_template('index.html', front_key=front_key)


@app.route('/grandpy/', methods=['GET', 'POST'])
def grandpy():
    # COULD BE IMPROVE WITH "/grandpy/<path>"
    msg = json.loads(request.data)
    gp = GrandPy()

    if request.method == "POST":
        grandPy_answer = gp.get_response(msg)
        return json.loads(grandPy_answer)


if __name__ == "__main__":
    app.run()
