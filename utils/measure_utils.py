from models import Measure
from utils import common_utils


def add_all(names):
    measures = (Measure(name) for name in names)
    common_utils.add(*measures)


def one_by_name(name):
    return common_utils.one(Measure, 'The measure is not conclusive!', Measure.name == name)

