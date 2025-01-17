from flask import Flask, render_template, url_for, request
import json
from .converter import smartify

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        text = request.json.get('text')

        if text:
            return json.dumps({'smartified': smartify(text)})
        return json.dumps({'smartified': ""})

    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)