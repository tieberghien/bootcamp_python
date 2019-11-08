from FileLoader import FileLoader

def howManyMedalsByCountry(data, country):
    dict = {}
    data = data.loc[(data['Team'] == country)]
    athlete = data.drop_duplicates('Event', keep='last')
    for year in athlete['Year']:
        gold = 0
        silver = 0
        bronze = 0
        years = athlete.loc[(data['Year'] == year)]
        for medal in years['Medal']:
            if medal == 'Gold':
                gold += 1
            elif medal == 'Silver':
                silver += 1
            elif medal == 'Bronze':
                bronze += 1
        dict.update({year: {'G': gold, 'S': silver, 'B' : bronze}})
    return dict

if __name__ == '__main__':
    loader = FileLoader()
    data = loader.load("../athlete_events.csv")
    print(howManyMedalsByCountry(data, 'France'))