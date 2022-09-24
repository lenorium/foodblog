from db import DbInstance
from models import Measure, Meal, Ingredient


def session_maker():
    return DbInstance().session_maker


def save(entities):
    try:
        with session_maker().begin() as session:
            for entity in entities:
                session.add(entity)
    except Exception as e:
        print(e)


class MeasureRepository:

    @staticmethod
    def create(measure_names: tuple):
        measures = [Measure(name) for name in measure_names]
        save(measures)


class IngredientRepository:

    @staticmethod
    def create(ingredient_names: tuple):
        ingredients = [Ingredient(name) for name in ingredient_names]
        save(ingredients)


class MealRepository():

    @staticmethod
    def create(meal_names: tuple):
        meals = [Meal(name) for name in meal_names]
        save(meals)