from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Product)
admin.site.register(State)
admin.site.register(Category)
admin.site.register(State_Category_Tax)
admin.site.register(FormInfoHandler)