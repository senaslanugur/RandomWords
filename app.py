from flask import Flask, render_template, jsonify
import random
import json

app = Flask(__name__)

with open('data.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

@app.route('/')
def index():
    random_item = random.choice(data)
    return render_template('index.html', random_item=random_item)

if __name__ == '__main__':
    app.run(debug=True)
