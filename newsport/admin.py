from django.contrib import admin
from .models import News,Publisher

# Register your models here.
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title','publisher',)

@admin.register(Publisher)
class publisherAdmin(admin.ModelAdmin):
    list_display = ('name','phone_no')


