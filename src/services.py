import sqlalchemy.orm as _orm
import database as _database, model as _model, schema as _schema


def create_database():
    return _database.Base.metadata.create_all(bind=_database.engine)

def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
def create_recipe(db: _orm.Session, recipe: _schema.RecipeCreate):
    db_recipe = _model.Recipe(title=recipe.title, ingredients=recipe.ingredients, method=recipe.method)
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe