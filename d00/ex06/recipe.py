def del_recipe(recipe):
    del recipe
    

def print_recipe(recipe):
    res = {key: recipe[key] for key in recipe.keys()}
    print(res)

if __name__ == '__main__':
    cookbook = { 'sandwich': {'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'], 'meal': 'lunch', 'prep_time': 10}, 
    'cake': {'ingredients': ['flour', 'sugar', 'eggs'], 'meal': 'dessert', 'prep_time': 60}, 
    'salad': {'ingredients': ['avocado', 'arugula', 'tomatoes','spinach'], 'meal': 'lunch', 'prep_time': 15} }

    # for k, v in cookbook.items():
    #     for k1, v1 in v.items():
    #         print(k1, v1)

    print_recipe(cookbook['sandwich'])
    del_recipe(cookbook['sandwich'])
    print_recipe(cookbook['sandwich'])