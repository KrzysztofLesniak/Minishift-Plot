import pandas as pd
import warnings
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.statespace.tools import diff
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.statespace.sarimax import SARIMAX, SARIMAXResults
from statsmodels.tsa.seasonal import seasonal_decompose
# from pmdarima import auto_arima
from statsmodels.tools.eval_measures import rmse, mse
import time


class ReturnDataFrame:
    def __init__(self):
        df = pd.read_csv('./data/co2_mm_gl.csv', sep=',')
        df["date"] = df["year"].astype(str) + '.' + df["month"].astype(str)
        df.rename(columns=lambda x: x.strip(), inplace=True)
        df.drop('year', axis='columns', inplace=True)
        df.drop('month', axis='columns', inplace=True)
        df.drop('decimal', axis='columns', inplace=True)
        df.drop('trend', axis='columns', inplace=True)
        df.drop('trend_unc', axis='columns', inplace=True)
        df.drop('average_unc', axis='columns', inplace=True)
        df = df.set_index('date')
        df.columns = ['C02']
        df.index = pd.to_datetime(df.index, format='%Y.%m')
        df.index.freq = 'MS'
        self.df = df

    def print(self):
        print(self.df.tail())

    def returnDate(self):
        return self.df.index

    def returnValues(self):
        return self.df['C02']

    def returnDataframe(self):
        return self.df
