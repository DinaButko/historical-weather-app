from flask import Flask, render_template

app = Flask("Website")

@app.route("/")
def home():
    """if we put template in tutorials folder we don't write path"""
    return render_template("home.html")

@app.route("/api/v1/<station>/<date>")
def about(station, date):
    """if we put template in tutorials folder we don't write path"""
    """<> what user puts as for request """
    temperature = 23
    df = pandas.read_csv("")
    temperature = df.station(date)
    #return render_template("about.html")
    return{"staion": station,
           "date": date,
           "temperature": temperature}

app.run(debug=True)