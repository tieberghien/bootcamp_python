from FileLoader import FileLoader

class SpatioTemporalData:
    def __init__(self, data):
        self.data = data

    def when(self, location):
        years = []
        seen = set()
        city = data.loc[(data['City'] == location)]
        for year in city['Year']:
            if year not in seen:
                seen.add(year)
                years.append(year)
        return (years)
    
    def where(self, date):
        city = []
        seen = set()
        year = data.loc[(data['Year'] == date)]
        for c in year['City']:
            if c not in seen:
                seen.add(c)
                city.append(c)
        return (city)

if __name__ == '__main__':
    loader = FileLoader()
    data = loader.load("../athlete_events.csv")
    sp = SpatioTemporalData(data)
    print(sp.when('Athina'))
    print(sp.where(1896))