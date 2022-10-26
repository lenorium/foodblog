import os
import sys

from models import Quantity, Recipe
from utils import measure_utils, ingredient_utils, meal_utils, recipe_utils


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
        meals = select_meals()
        ingredients = input_ingredients()
        recipe_utils.add(Recipe(name, description, meals, ingredients))


def select_meals():
    meals = meal_utils.all()
    print(*[f'{i}. {v}' for i,v in enumerate(meals, start=1)])
    selected_meals_indices = input('When the dish can be served: ').strip().split()
    return [meals[int(i) - 1] for i in selected_meals_indices]


def input_ingredients():
    ingredients = []
    while True:
        details = input('Input quantity of ingredient <press enter to stop>: ')
        if not details:
            break
        details = details.split()
        if len(details) not in (2, 3) or not details[0].isdigit():
            print('Incorrect quantity of ingredient. Try again ')
            continue
        quantity = details.pop(0)
        ingredient = details.pop(-1)
        measure = details[0] if details else ''

        measure = measure_utils.one_by_name(measure)
        ingredient = ingredient_utils.one_by_name(ingredient)
        if not measure or not ingredient:
            continue
        ingredients.append(Quantity(quantity, measure, ingredient))
    return ingredients


def init():
    data = {"meals": ("breakfast", "brunch", "lunch", "supper"),
            "ingredients": ("milk", "cacao", "strawberry", "blueberry", "blackberry", "sugar"),
            "measures": ("ml", "g", "l", "cup", "tbsp", "tsp", "dsp", "")}
    measure_utils.add_all(data['measures'])
    ingredient_utils.add_all(data['ingredients'])
    meal_utils.add_all(data['meals'])


if __name__ == '__main__':
    parse_cli_args()
    # init()
    add_recipes()
