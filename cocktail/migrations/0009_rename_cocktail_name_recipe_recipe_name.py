# Generated by Django 3.2.7 on 2021-10-03 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cocktail', '0008_recipe_date_posted'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='cocktail_name',
            new_name='recipe_name',
        ),
    ]
