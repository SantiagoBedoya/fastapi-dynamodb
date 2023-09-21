from fastapi import FastAPI
import uvicorn
from db import initialize_db
from service.recipe_service import RecipeService
from repository.recipe_repository import RecipesRepository
from routers.recipe_router import RecipeRouter

app = FastAPI()
db = initialize_db()
recipe_repository = RecipesRepository(db)
recipe_service = RecipeService(recipe_repository)
recipe_router = RecipeRouter(recipe_service)

app.include_router(recipe_router.router)


@app.get('/')
async def root():
    return {
        "health": "OK"
    }

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)