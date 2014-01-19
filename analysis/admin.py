from django.contrib import admin
from .models import Show, Episode


class ShowAdmin(admin.ModelAdmin):
    pass


admin.site.register(Show, ShowAdmin)


class EpisodeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Episode, EpisodeAdmin)
