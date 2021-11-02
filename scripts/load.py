import csv
import os
from cocktail.models import Recipe


def run():
    file = open(
        "C:/Users/M.Raees Iqbal/Desktop/Recipe/New folder/recipe_project copy/scripts/data.csv"
    )
    read_file = csv.reader(file)
    # Recipe.objects.all().delete()
    get = Recipe.objects.order_by("-date_posted")

    count = 1
    for recipe in read_file:
        if count == 1:
            pass
        elif recipe[1] != "":
            print(recipe[0])
            Recipe.objects.create(
                recipe_name=recipe[0],
                # ingredients=recipe[1],
                # recipe_method=recipe[2],
                # process=recipe[3],
                # glass=recipe[4],
                # garnish=recipe[5],
                # notes=recipe[6],
                # characteristics=recipe[7],
            )
        count = count + 1

    # count = 1
    # for recipe in read_file:
    #     if count == 1:
    #         pass
    #     elif recipe[0] != "":
    #         print(recipe[0])
    #         Recipe.objects.create(
    #             recipe_name=recipe[0],
    #             # ingredients=recipe[1],
    #             # recipe_method=recipe[2],
    #             # process=recipe[3],
    #             # glass=recipe[4],
    #             # garnish=recipe[5],
    #             # notes=recipe[6],
    #             # characteristics=recipe[7],
    #         )
    #     count = count + 1
