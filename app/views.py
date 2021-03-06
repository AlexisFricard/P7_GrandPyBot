from flask import Flask, render_template, request, jsonify
import config
import json

from app.grandpy.papybot import GrandPy

app = Flask(__name__)

app.config.from_object('config')

@app.route('/')
def index():
        gm_api_key = config.GM_API_KEY
        return render_template('index.html', gm_api_key=gm_api_key)


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