import csv
from  datetime import datetime as datetime
import pandas as pd

class twitterData:
    def __init__(self, file):
        self.data = []
        self.get_csv(file)

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
            lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M'))


if __name__ == "__main__":
    a = twitterData('../../twitter_client/twitter_client/data/output_got.csv')
    print(a.data)
