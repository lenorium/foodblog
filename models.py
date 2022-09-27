from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


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

    def __init__(self, name):
        super().__init__()
        self.name = name


class Recipe(Base):
    __tablename__ = 'recipes'

    recipe_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String)

    def __init__(self, name, description):
        super().__init__()
        self.name = name
        self.description = description
