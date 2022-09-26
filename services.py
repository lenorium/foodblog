from models import Measure, Meal, Ingredient, Recipe
import repository


class MeasureService:

    @staticmethod
    def create(measure_names: tuple):
        measures = [Measure(name) for name in measure_names]
        repository.save_bulk(measures)


class IngredientService:

    @staticmethod
    def create(ingredient_names: tuple):
        ingredients = [Ingredient(name) for name in ingredient_names]
        repository.save_bulk(ingredients)


class MealService:

    @staticmethod
    def create(meal_names: tuple):
        meals = [Meal(name) for name in meal_names]
        repository.save_bulk(meals)


class RecipeService:

    @staticmethod
    def create(name, description):
        repository.save(Recipe(name, description))
