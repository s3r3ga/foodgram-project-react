from django.contrib import admin
from .models import Recipe, Ingredient, Tag, Favorite, ShoppingCart, IngredientAmount

admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(IngredientAmount)
admin.site.register(Tag)
admin.site.register(Favorite)
admin.site.register(ShoppingCart)
