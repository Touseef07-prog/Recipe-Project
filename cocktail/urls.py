from django.urls import path
from . import views
from cocktail.views import SingleRecipeView, HomePageView, RecipeSearchView


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("single_recipe/<int:id>", SingleRecipeView.as_view(), name="single_recipe"),
    path(
        "recipe_search/<str:search>", RecipeSearchView.as_view(), name="recipe_search"
    ),
]
