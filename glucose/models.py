from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

# Create your models here.
class Glucose(models.Model):
    device = models.CharField(blank=False,null=False,max_length=255)
    serial_number = models.CharField(blank=False,null=False,max_length=100)
    device_timestamp = models.DateTimeField(blank=False,null=False)
    record_type = models.IntegerField(default=0)
    glucose_history = models.DecimalField(max_digits = 5,decimal_places = 2)
    glucose_scan = models.DecimalField(max_digits = 5,decimal_places = 2)
    non_numeric_rapid_acting_insulin = models.CharField(blank=False,null=False,max_length=500)
    rapid_acting_insulin = models.IntegerField(default=0)
    non_numeric = models.CharField(blank=False,null=False,max_length=500)
    food_data = models.CharField(blank=False,null=False,max_length=500)
    carbohydrates_grams  = models.DecimalField(max_digits = 5,decimal_places = 2)
    carbohydrates_servings  = models.DecimalField(max_digits = 5,decimal_places = 2)
    non_numeric_depot_insulin = models.CharField(blank=False,null=False,max_length=500)
    depot_insulin = models.IntegerField(default=0)
    notes = models.TextField(blank=True)
    glucose_test_strip = models.DecimalField(max_digits = 5,decimal_places = 2)
    ketone = models.DecimalField(max_digits = 5,decimal_places = 2)
    mealtime_insulin = models.IntegerField(default=0)
    correction_insulin = models.IntegerField(default=0)
    user_insulin_change = models.IntegerField(default=0)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class GlucoseAdmin(admin.ModelAdmin):
    list_display= ('device', 'serial_number', 'device_timestamp')

admin.site.register(Glucose,GlucoseAdmin)
