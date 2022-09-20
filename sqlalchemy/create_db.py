from sqlalchemy import User, engine, Base


Base.metadata.create_all(engine)
