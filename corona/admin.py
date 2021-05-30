from django.contrib import admin
from corona.models.lucknowarea import LucknowArea
from corona.models.delhiarea import DelhiArea
from corona.models.lucknowdealers import LucknowDealer
from corona.models.kanpurdealers import KanpurDealer
from corona.models.delhidealers import DelhiDealer
from corona.models.lkobeds import Lucknowbeds
from corona.models.delhibeds import Delhibeds
from corona.models.kanpurbeds import Kanpurbeds

class LucknowAdminArea(admin.ModelAdmin):
    list_display=['name']
class DelhiAdminArea(admin.ModelAdmin):
    list_display=['name']
class LucknowAdminDealer(admin.ModelAdmin):
    list_display=['name','address','phone']
class DelhiAdminDealer(admin.ModelAdmin):
    list_display=['name','address','phone']
class KanpurAdminDealer(admin.ModelAdmin):
    list_display=['name','address','phone']
class LucknowbedsAdmin(admin.ModelAdmin):
    list_display=['condition','centre','number']
class KanpurbedsAdmin(admin.ModelAdmin):
    list_display=['condition','centre','number']
class DelhibedsAdmin(admin.ModelAdmin):
    list_display=['Hospital','Type','Total','Vacant']

# Register your models here.
admin.site.register(LucknowArea,LucknowAdminArea)
admin.site.register(DelhiArea,DelhiAdminArea)
admin.site.register(LucknowDealer,LucknowAdminDealer)
admin.site.register(KanpurDealer,KanpurAdminDealer)
admin.site.register(DelhiDealer,DelhiAdminDealer)
admin.site.register(Lucknowbeds,LucknowbedsAdmin)
admin.site.register(Delhibeds,DelhibedsAdmin)
admin.site.register(Kanpurbeds,KanpurbedsAdmin)
