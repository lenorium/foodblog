import os
import sys

import services


def parse_cli_args():
    os.environ['db_name'] = next(filter(lambda arg: arg.endswith('.db'), sys.argv))
    os.environ['db_log'] = str('log' in sys.argv)


def add_recipes():
    print('Pass the empty recipe name to exit.')
    while True:
        name = input('Recipe name:').strip()
        if not name:
            break
        description = input('Recipe description:').strip()

        meals = services.get_meals()
        print(' '.join([f'{i + 1}) {m.name}' for i, m in enumerate(meals)]))
        selected_meals_indices = input('When the dish can be served: ').strip().split()
        selected_meals = [meals[int(i) - 1] for i in selected_meals_indices]

        services.create_recipe(name, description, selected_meals)


if __name__ == '__main__':
    parse_cli_args()

    # data = {"meals": ("breakfast", "brunch", "lunch", "supper"),
    #         "ingredients": ("milk", "cacao", "strawberry", "blueberry", "blackberry", "sugar"),
    #         "measures": ("ml", "g", "l", "cup", "tbsp", "tsp", "dsp", "")}
    #
    # services.create_measures(data['measures'])
    # services.create_ingredients(data['ingredients'])
    # services.create_meals(data['meals'])

    add_recipes()



