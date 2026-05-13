from django.contrib import admin
from .models import Profile, Group, Food, NutritionPlan, DefaultPlan

# This makes them show up in the Django Admin sidebar
admin.site.register(Profile)
admin.site.register(Group)
admin.site.register(Food)
admin.site.register(NutritionPlan)
admin.site.register(DefaultPlan)
