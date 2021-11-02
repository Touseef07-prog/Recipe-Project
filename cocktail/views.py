from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from users.models import User
from cocktail.models import Recipe, Category
from django.contrib.postgres.search import SearchVector
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


class HomePageView(View):
    def get(self, request, *args, **kwargs):
        get_recipe = Recipe.objects.all()
        context = {"recipe": get_recipe}
        return render(request, "cocktail/home.html", context=context)

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        recipes = Recipe.objects.annotate(
            search=SearchVector("recipe_name")
            + SearchVector("characteristics")
            + SearchVector("recipe_method")
            + SearchVector("glass")
            + SearchVector("garnish")
        ).filter(search=data.get("search"))

        # context = {"recipe": recipe}
        # return render(request, "cocktail/home.html", context=context)
        return JsonResponse([recipe.serialize() for recipe in recipes], safe=False)


class RecipeSearchView(View):
    def get(self, request, search, *args, **kwargs):
        recipes = Recipe.objects.annotate(
            search=SearchVector("recipe_name")
            + SearchVector("characteristics")
            + SearchVector("recipe_method")
            + SearchVector("glass")
            + SearchVector("garnish")
        ).filter(search=search)

        # context = {"recipe": recipe}
        # return render(request, "cocktail/home.html", context=context)
        return JsonResponse([recipe.serialize() for recipe in recipes], safe=False)


class SingleRecipeView(View):
    def get(self, request, id, *args, **kwargs):
        get_recipe = Recipe.objects.get(id=id)
        context = {"recipe": get_recipe}
        return render(request, "cocktail/single_recipe.html", context=context)
