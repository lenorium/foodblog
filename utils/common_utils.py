import repository


def add(*entities):
    repository.save_bulk(*entities)


def one(cls, error: str, *filter_exp):
    res = repository.all(cls, *filter_exp)
    if len(res) != 1:
        print(error)
        return None
    return res[0]


def all(cls, *filter_exp):
    return repository.all(cls, *filter_exp)