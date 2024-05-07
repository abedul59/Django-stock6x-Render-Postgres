from django.contrib import admin

# Register your models here.
from myapp import models

admin.site.register(models.Person)
admin.site.register(models.NewsUnit)
admin.site.register(models.MacroWaveA)
admin.site.register(models.MacroWaveB)
admin.site.register(models.MacroWaveC)
admin.site.register(models.USBondYieldDB)
admin.site.register(models.Stock6Sign202404)
admin.site.register(models.StockPERseg202404)
admin.site.register(models.StockFavs_test168)
