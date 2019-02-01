from pyzomato import Pyzomato
from flask import Flask, render_template
import json

from urllib import request

def callAPI():
    p = Pyzomato("0037bd86fc45f5201beebaa204099f72")

    er = p.getLocationDetails(484, "city")

    final = []
    for k in er["best_rated_restaurant"]:
        for k2 in k:
            if "American" in k[k2]["cuisines"] and "Latin American" not in k[k2]["cuisines"]:
                d = {}
                d["name"] = k[k2]["name"]
                d["address"] = k[k2]["location"]["address"]
                d["cuisines"] = k[k2]["cuisines"]
                d["rating"] = k[k2]["user_rating"]["aggregate_rating"]
                d["votes"] = k[k2]["user_rating"]["votes"]
                d["photo_url"] = k[k2]["photos_url"]
                d["menu_url"] = k[k2]["menu_url"]
                final.append(d)



    final = sorted(final, key=lambda k: k["rating"], reverse = True)
    return final


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/results', methods=['GET', 'POST']) # decorator, defines your website's /
def result():
    
    results = callAPI()
    return render_template('results.html', results = results)

if __name__ == "__main__":
    app.run(debug = True) #Set debug = False in a production environment

