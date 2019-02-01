
from flask import Flask, render_template
import json
import Pyzamoto


app = Flask(__name__)

@app.route('/') # decorator, defines your website's /
def index():
    
    test_titles = ["A", "B", "C", "D", "E", "F"]
    return render_template('results.html', results = test_titles)

if __name__ == "__main__":
    app.run(debug = True) #Set debug = False in a production environment