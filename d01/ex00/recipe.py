from six import string_types

class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, descriptions, recipe_type):
        try:
            self.name = name
            assert isinstance(name, str)
        except:
            print("{} type provided for attribute 'name' instead of 'str'".format(type(name)))
            exit()
        try:
            self.cooking_lvl = cooking_lvl
            assert (cooking_lvl > 0 and cooking_lvl < 6)
        except:
            print("Cooking level needs to range from 1 to 5")
            exit()
        try:
            self.cooking_time = cooking_time
            assert cooking_time > 0
        except:
            print("Cooking time can't be negative (yeah, figures)")
            exit()
        try:
            self.ingredients = ingredients
            assert isinstance(ingredients, list)
        except:
            print("{} type provided for attribute 'ingredients' instead of 'list'".format(type(ingredients)))
            exit()
        try:
            self.descriptions = descriptions
            assert isinstance(descriptions, str)
        except:
            print("{} type provided for attribute 'descriptions' instead of 'str'".format(type(descriptions)))
            exit()
        try:
            self.recipe_type = recipe_type
            assert (recipe_type == "starter" or recipe_type == "lunch" or recipe_type == "dessert")
        except:
            print("Recipe type needs be either starter, lunch or dessert")
            exit()
        
    def __str__(self):
        return ', '.join(['{key}={value}'.format(key=key, value=self.__dict__.get(key)) for key in self.__dict__])


if __name__ == '__main__':
    gateau = Recipe("coucou", 3, 120, ["pouet", "120", "ouaisouais"], "kdjfbdkjfgd ", "lunch")
    to_print = str(gateau)
    print(to_print)