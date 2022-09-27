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
    name = Column(String, unique=True, nullable=False)

    def __init__(self, name):
        super().__init__()
        self.name = name


class Ingredient(Base):
    __tablename__ = 'ingredients'

    ingredient_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)

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

    def __init__(self, name, description, meals):
        super().__init__()
        self.name = name
        self.description = description
        self.meals = meals
