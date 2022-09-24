from models import Measure, Meal, Ingredient
import repository


class MeasureService:

    def create(self, measure_names: tuple):
        measures = [Measure(name) for name in measure_names]
        repository.save(measures)


class IngredientService:

    @staticmethod
    def create(ingredient_names: tuple):
        ingredients = [Ingredient(name) for name in ingredient_names]
        repository.save(ingredients)


class MealService:

    @staticmethod
    def create(meal_names: tuple):
        meals = [Meal(name) for name in meal_names]
        repository.save(meals)