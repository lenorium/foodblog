from models import Ingredient
from utils import common_utils


def add_all(names):
    ingredients = (Ingredient(name) for name in names)
    common_utils.add(*ingredients)


def one_by_name(name):
    return common_utils.one(Ingredient, 'The ingredient is not conclusive!',  Ingredient.name.startswith(name))
