from django.contrib import admin
from .models import InfoBox

class InfoBoxAdmin(admin.ModelAdmin):
	pass

admin.site.register(InfoBox,  InfoBoxAdmin)