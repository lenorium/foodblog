from db import DbInstance


def session_maker():
    return DbInstance().session_maker


def save(entities):
    try:
        with session_maker().begin() as session:
            for entity in entities:
                session.add(entity)
    except Exception as e:
        print(e)
