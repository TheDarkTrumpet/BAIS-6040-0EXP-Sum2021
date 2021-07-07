from flask import Flask
from flask.templating import render_template
from lib.plot import getPiePlot, getChartPlot

app = Flask(__name__)

allReports = [
    ("/pieplot", "Pie Rates in Mexico (Pie Plot)"),
    ("/barchart", "Pie Rates in Mexico (Bar Chart Plot)")
]


def plot(data):
    return render_template('report.html', report=data)


@app.route('/')
def index():
    return render_template('index.html', reports=allReports)


@app.route('/pieplot')
def pieplot():
    chart = getPiePlot()
    return plot(chart)


@app.route('/barchart')
def piechart():
    chart = getChartPlot()
    return plot(chart)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
