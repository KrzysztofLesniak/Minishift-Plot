import pandas as pd


class ReturnDataFrame:
    def __init__(self):
        df = pd.read_csv('./data/C02_Date_Value_Prediction.csv', sep=',')
        test_df = pd.read_csv('./data/C02_LSTM_test_results.csv', sep=',')

        self.df = df
        self.testDf = test_df

    def print(self):
        print(self.df.tail())

    def returnDataframe(self):
        return self.df

    def returnTestDataframe(self):
        return self.testDf
