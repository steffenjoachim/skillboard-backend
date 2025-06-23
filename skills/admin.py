from django.contrib import admin
from .models import Skill, User

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')  
    list_filter = ('category',)           
    search_fields = ('title',)

admin.site.register(User)
