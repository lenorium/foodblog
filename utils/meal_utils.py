from models import Meal
from utils import common_utils


def add_all(names):
    meals = (Meal(name) for name in names)
    common_utils.add(*meals)


def all(*filter_exp):
    return common_utils.all(Meal, *filter_exp)
