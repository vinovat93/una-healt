import json,os,string,random,decimal
from random import randrange
from glucose.models import Glucose
from datetime import timedelta,datetime

def getRandomInt():
    return random.randint(1, 300)

def getRandomString():
    return ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(90))

def getRandomDecimal():
    return float(decimal.Decimal(random.randrange(0, 300))/100)

def getRandomDatetimeFromPast():

    start = datetime.strptime('2020-10-25 14:30:59', '%Y-%m-%d %H:%M:%S')
    end = datetime.strptime('2023-01-25 14:30:59', '%Y-%m-%d %H:%M:%S')
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)



def create_random_levels(length,user):
    for x in range(length):
        Glucose.objects.create(**{
            "device":getRandomString(),
            "serial_number":getRandomString(),
            "device_timestamp":getRandomDatetimeFromPast(),
            "record_type":getRandomInt(),
            "glucose_history":getRandomDecimal(),
            "glucose_scan":getRandomDecimal(),
            "non_numeric_rapid_acting_insulin":getRandomString(),
            "rapid_acting_insulin":getRandomInt(),
            "non_numeric":getRandomString(),
            "food_data":getRandomString(),
            "carbohydrates_grams":getRandomDecimal(),
            "carbohydrates_servings":getRandomDecimal(),
            "non_numeric_depot_insulin":getRandomString(),
            "depot_insulin":getRandomInt(),
            "notes":getRandomString(),
            "glucose_test_strip":getRandomDecimal(),
            "ketone":getRandomDecimal(),
            "mealtime_insulin":getRandomInt(),
            "correction_insulin":getRandomInt(),
            "user_insulin_change":getRandomInt(),
            "user":user
        })