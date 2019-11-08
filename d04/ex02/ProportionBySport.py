from FileLoader import FileLoader

def proportionBySport(data, year, sport, gender):
    dict = {}
    data = data.drop_duplicates('Name', keep='last')
    df = data.loc[:, ['Sex', 'Age', 'Year', 'Sport']]
    spec = data.loc[(df['Year'] == year) & (df['Sex'] == gender) & (df['Sport'] == sport)]
    total = data.loc[(df['Year'] == year) & (df['Sex'] == gender)]
    print(spec.shape[0] / total.shape[0])

if __name__ == '__main__':
    loader = FileLoader()
    data = loader.load("../athlete_events.csv")
    proportionBySport(data, 2004, 'Tennis', 'F')