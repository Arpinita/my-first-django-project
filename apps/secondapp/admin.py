from django.contrib import admin
from .models import Animals
from .models import Owners


class AnimalsModelAdmin(admin.ModelAdmin):
    class Meta:
        model = Animals


admin.site.register(Animals, AnimalsModelAdmin)


class OwnersModelAdmin(admin.ModelAdmin):
    class Meta:
        model = Owners


admin.site.register(Owners, OwnersModelAdmin)
