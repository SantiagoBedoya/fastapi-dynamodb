from uuid import uuid4
from repository.recipe_repository import RecipesRepository
from model.recipe import Recipe

class RecipeService():
    def __init__(self, repository: RecipesRepository) -> None:
        self.__repository = repository

    def get_all(self):
        return self.__repository.get_all()
    
    def get_recipe(self, uid: str):
        return self.__repository.get_recipe(uid)
    
    def create_recipe(self, recipe: Recipe):
        recipe.uid = str(uuid4())
        return self.__repository.create_recipe(recipe.model_dump())

    def update_recipe(self, recipe: Recipe):
        return self.__repository.update_recipe(recipe.model_dump())

    def delete_recipe(self, uid: str):
        return self.__repository.delete_recipe(uid)