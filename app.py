import os
import sys
from repositories import MeasureRepository, IngredientRepository, MealRepository


def parse_cli_args():
    os.environ['db_name'] = next(filter(lambda arg: arg.endswith('.db'), sys.argv))
    os.environ['db_log'] = str('log' in sys.argv)


if __name__ == '__main__':
    parse_cli_args()

    data = {"meals": ("breakfast", "brunch", "lunch", "supper"),
            "ingredients": ("milk", "cacao", "strawberry", "blueberry", "blackberry", "sugar"),
            "measures": ("ml", "g", "l", "cup", "tbsp", "tsp", "dsp", "")}

    MeasureRepository().create(data['measures'])
    IngredientRepository().create(data['ingredients'])
    MealRepository().create(data['meals'])



