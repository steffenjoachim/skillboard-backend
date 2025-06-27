from django.contrib import admin
from .models import Skill, User, Category, Subcategory

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    pass

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Subcategory)
