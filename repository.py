from database import DbInstance


def session_maker():
    return DbInstance().session_maker


def save_bulk(*entities):
    try:
        with session_maker().begin() as session:
            for entity in entities:
                session.add(entity)
    except Exception as e:
        print(e)


def all(cls, *filter_exp) -> list:
    with session_maker()() as session:
        return session.query(cls).filter(*filter_exp).all()
