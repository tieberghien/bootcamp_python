from FileLoader import FileLoader

def youngestFellah(data, year):
    dict = {}
    df = data.loc[:, ['Sex', 'Age', 'Year']]
    male = data.loc[(df['Year'] == year) & (df['Sex'] == "M")]
    female = data.loc[(df['Year'] == year) & (df['Sex'] == "F")]
    dict.update({'f': female['Age'].min()})
    dict.update({'m': male['Age'].min()})
    print(dict)

if __name__ == '__main__':
    loader = FileLoader()
    data = loader.load("../athlete_events.csv")
    youngestFellah(data, 2004)