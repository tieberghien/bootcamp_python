from FileLoader import FileLoader

def howManyMedals(data, name):
    dict = {}
    athlete = data.loc[(data['Name'] == name)]
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
    print(dict)

if __name__ == '__main__':
    loader = FileLoader()
    data = loader.load("../athlete_events.csv")
    howManyMedals(data, 'Kjetil Andr Aamodt')