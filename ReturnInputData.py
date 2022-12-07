import pandas as pd

class ReturnDataFrame:
    def __init__(self):
        df = pd.read_csv('./data/C02_input_and_predictions.csv', sep=',')
        df = df.set_index('Date')
        df.columns = ['C02']
        df.index = pd.to_datetime(df.index, format='%Y-%m-%d')
        df.index.freq = 'MS'
        self.df = df

    def print(self):
        print(self.df.tail())

    def returnDataframe(self):
        return self.df
