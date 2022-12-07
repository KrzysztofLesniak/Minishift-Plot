import pandas as pd


class ReturnDataFrame:
    def __init__(self):
        df = pd.read_csv('./data/C02_Date_Value_Prediction.csv', sep=',')
        self.df = df

    def print(self):
        print(self.df.tail())

    def returnDataframe(self):
        return self.df
