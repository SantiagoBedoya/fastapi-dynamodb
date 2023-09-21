from fastapi import APIRouter, HTTPException
from service.recipe_service import RecipeService
from model.recipe import Recipe

router = APIRouter(prefix='/recipes', tags=['recipes'])

class RecipeRouter:
    def __init__(self, recipe_service: RecipeService) -> None:
        self.__recipe_service = recipe_service

    @property
    def router(self):
        api_router = APIRouter(prefix='/recipes', tags=['recipes'])

        @api_router.get('')
        async def get_all():
            return self.__recipe_service.get_all()

        @api_router.post('')
        async def create(recipe: Recipe):
            return self.__recipe_service.create_recipe(recipe)

        @api_router.get('/{recipe_uid}')
        async def get_one(recipe_uid:str):
            try:
                return self.__recipe_service.get_recipe(recipe_uid)
            except KeyError:
                raise HTTPException(status_code=404, detail='No recipe found')

        @api_router.put('/{recipe_uid}')
        def update(recipe_uid: str, recipe: Recipe):
            recipe.uid = recipe_uid
            return self.__recipe_service.update_recipe(recipe)

        @api_router.delete('/{recipe_uid}')
        def delete(recipe_uid: str):
            return self.__recipe_service.delete_recipe(recipe_uid)

        return api_router