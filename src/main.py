import fastapi as _fastapi
import sqlalchemy.orm as _orm
import services as _services, schema as _schema

app = _fastapi.FastAPI()

_services.create_database()

@app.post("/recipes", response_model=_schema.Recipe)
def create_recipe(
    recipe: _schema.RecipeCreate, db: _orm.Session=_fastapi.Depends(_services.get_db)
):
    db_recipe = _services.create_recipe(db=db, recipe=recipe)
    
    return db_recipe