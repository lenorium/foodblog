import os
import sys

from services import RecipeService


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
        RecipeService.create(name, description)


if __name__ == '__main__':
    parse_cli_args()

    # data = {"meals": ("breakfast", "brunch", "lunch", "supper"),
    #         "ingredients": ("milk", "cacao", "strawberry", "blueberry", "blackberry", "sugar"),
    #         "measures": ("ml", "g", "l", "cup", "tbsp", "tsp", "dsp", "")}
    #
    # MeasureService.create(data['measures'])
    # IngredientService.create(data['ingredients'])
    # MealService.create(data['meals'])

    add_recipes()



