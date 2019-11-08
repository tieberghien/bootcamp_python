import pandas as pd

class FileLoader():
    def __init__(self):
        pass

    def load(self, path):
        try:
            df = pd.read_csv(path)
        except IOError:
            print("No dataset found")
            exit()
        print("Loading dataset of dimensions {} x {}".format(df.shape[0], df.shape[1]))
        return df

    def display(self, df, n):
        if n > 0:
            print(df.head(n))
        else:
            print(df.tail(-n))


if __name__ == '__main__':
    loader = FileLoader()
    data = loader.load("../athlete_events.csv")
    loader.display(data, -12)