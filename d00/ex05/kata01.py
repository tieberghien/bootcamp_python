if __name__ == '__main__':
    languages = {
        'Python': 'Guido van Rossum',
        'Ruby': 'Yukihiro Matsumoto',
        'PHP': 'Rasmus Lerdorf',
        }

    for lang, creator in languages.items():
        print("{0} was created by {1}".format(lang, creator))