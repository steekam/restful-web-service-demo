import app.database as database

database.Base.metadata.create_all(bind=database.engine)
