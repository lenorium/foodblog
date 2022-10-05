from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship

Base = declarative_base()

serve = Table(
    "serve",
    Base.metadata,
    Column('serve_id', Integer, primary_key=True, autoincrement=True),
    Column('meal_id', ForeignKey('meals.meal_id'), nullable=False),
    Column('recipe_id', ForeignKey('recipes.recipe_id'), nullable=False),
)


class Measure(Base):
    __tablename__ = 'measures'

    measure_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True)
    quantities = relationship('Quantity')

    def __init__(self, name):
        super().__init__()
        self.name = name


class Ingredient(Base):
    __tablename__ = 'ingredients'

    ingredient_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    quantities = relationship('Quantity')

    def __init__(self, name):
        super().__init__()
        self.name = name


class Meal(Base):
    __tablename__ = 'meals'

    meal_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    recipes = relationship('Recipe', secondary=serve, back_populates='meals')

    def __init__(self, name):
        super().__init__()
        self.name = name


class Recipe(Base):
    __tablename__ = 'recipes'

    recipe_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String)
    meals = relationship('Meal', secondary=serve, back_populates='recipes')
    quantities = relationship('Quantity')

    def __init__(self, name, description, meals: list, quantities: list):
        super().__init__()
        self.name = name
        self.description = description
        self.meals = meals
        self.quantities = quantities


class Quantity(Base):
    __tablename__ = 'quantity'

    quantity_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    quantity = Column(Integer, nullable=False)
    recipe_id = Column(Integer, ForeignKey('recipes.recipe_id'), nullable=False)
    measure_id = Column(Integer, ForeignKey('measures.measure_id'), nullable=False)
    ingredient_id = Column(Integer, ForeignKey('ingredients.ingredient_id'), nullable=False)

    def __init__(self, quantity, measure: Measure, ingredient: Ingredient):
        super().__init__()
        self.quantity = quantity
        self.measure_id = measure.measure_id
        self.ingredient_id = ingredient.ingredient_id
