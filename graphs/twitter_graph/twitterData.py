import csv
import numpy as np
import  datetime as dt
import pandas as pd

class twitterData:
    def __init__(self, file):
        self.data = []
        self.get_csv(file)
        self.data['score'] = np.random.randn(len(self.data)) # mocking


    def get_csv(self, file):
        with open(file, 'r') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            for row in spamreader:
                if len(row) is 4:
                    self.data.append(row)
        header = self.data[0]
        self.data = self.data[1:]
        self.data = pd.DataFrame(self.data, columns=header)
        self.data.date=self.data.date.apply(
            lambda x: dt.datetime.strptime(x, '%Y-%m-%d %H:%M'))

    def final_socre(self, last_n_days=180):
        date_range = list(self.data['date'])[-1] - dt.timedelta(days=last_n_days)
        select = self.data[self.data['date'] > date_range]
        return(np.mean(select['score']))
    
    def aggregate_score(self, interval_days=30):
        drange = pd.date_range(self.data['date'][0], periods=interval_days,
                               freq='D')
        s = pd.Series(np.float64(self.data.score), index=self.data.date)
        return(s.resample('W', np.mean))


if __name__ == "__main__":
    a = twitterData('../../twitter_client/twitter_client/data/output_got.csv')
    print(a.final_socre())
    m = a.aggregate_score()
    print(m)
