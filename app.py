from flask import Flask, render_template, request
import json
import requests

app = Flask(__name__) 


@app.route('/', methods=['GET', 'POST'])
def message():
    if request.method == 'GET':
        return render_template("obsluga_api.html", stations=get_stations())
    elif request.method == 'POST':
        print(request.form)
        station = request.form['stacja']
        for stations in get_stations(): 
            if stations['id_stacji'] == station:
                result = stations
        return render_template("obsluga_api.html", stations=get_stations(), result=result)

def get_stations():
    response = requests.get("https://danepubliczne.imgw.pl/api/data/synop/")
#    data = response.json()
#    data_as_json = json.dumps(data)
#    data_from_json = json.loads(data_as_json)
#    stations = data_from_json[0]
    return response.json()
    