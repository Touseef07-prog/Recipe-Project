from django.db import models
from django.core.validators import FileExtensionValidator
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

import cocktail


Category_Name = (("cocktail", "cocktail"), ("other", "other"))


class Category(models.Model):
    name = models.CharField(
        max_length=30,
        choices=Category_Name,
        default="Cocktail",
        null=False,
        blank=False,
    )

    def __str__(self):
        return f"{self.name}"


class Recipe(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    recipe_name = models.CharField(max_length=30, null=False, blank=False)
    ingredients = models.TextField(null=True, blank=True)
    recipe_method = models.CharField(max_length=30, null=False, blank=False)
    glass = models.CharField(max_length=30, null=False, blank=False)
    process = models.TextField(null=True, blank=True)
    garnish = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    characteristics = models.TextField(null=True, blank=True)
    recipe_image = models.ImageField(
        null=True,
        default="default.jpg",
        validators=[FileExtensionValidator(["jpg", "jpeg", "png"])],
        blank=True,
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    date_posted = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.recipe_name}"

    def serialize(self):
        return {
            "id": self.id,
            "recipe_name": self.recipe_name,
            "ingredients": self.ingredients,
            "recipe_method": self.recipe_method,
            "glass": self.glass,
            "process": self.process,
            "garnish": self.garnish,
            "notes": self.notes,
            "characteristics": self.characteristics,
        }
