import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from FileLoader import FileLoader

class MyPlotLib:
    def __init__(self):
        pass

    def histogram(self, df, features):
        fig, axes = plt.subplots(ncols=len(df.columns), figsize=(10,5))
        for col, ax in zip(df, axes):
            df[col].value_counts().sort_index().plot.bar(ax=ax, title=col)

        plt.tight_layout()    
        plt.show()
        # for f in features:
        #     sns.distplot(data[f[0]],kde = False)
        # plt.show()
    
    def density(self, data, features):
        pass

    def pair_plot(self, data, features):
        sns.pairplot(features)
        plt.show()

    def box_plot(self, data, features):
        pass

if __name__ == '__main__':
    loader = FileLoader()
    data = loader.load("../athlete_events.csv")
    dataset = data.dropna()
    features = dataset._get_numeric_data()
    plot = MyPlotLib()
    plot.histogram(dataset, features)
    #plot.pair_plot(dataset, features)