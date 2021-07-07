import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from io import BytesIO
import base64

def getData():
    pieRates = pd.read_csv(
        "https://raw.githubusercontent.com/TheDarkTrumpet/BAIS-6040-0EXP-spr2021/master/data/pie_rates.csv")
    return pieRates


def getMexicoData():
    pieRates = getData()
    mexicoPieRates = pieRates[pieRates["Country"] == "Mexico"]
    mexicoPies = mexicoPieRates["Pie"]
    mexicoRates = mexicoPieRates["Rate"]
    return mexicoPies, mexicoRates


def getPiePlot():
    mexicoPies, mexicoRates = getMexicoData()

    fig = plt.figure(figsize=(10, 10))
    fig.patch.set_facecolor('white')
    plt.pie(mexicoRates, labels=mexicoPies)
    plt.legend(loc='upper left')
    plt.title("Pie rates in Mexico")

    buf = BytesIO()

    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return data


def getChartPlot():
    pieData = getData()
    sns.set_style("whitegrid")
    plt.subplots(figsize=(10, 6))
    axis = sns.barplot(x="Pie", y="Rate", hue="Country", data=pieData, ci=None, palette="muted", orient='v')
    axis.set_title("Pie Rates!")
    axis.set_xlabel("Pies")
    axis.set_ylabel("Rate")

    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return data
