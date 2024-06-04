from django.contrib.auth.models import User
from django.test import TestCase

from .models import Glucose
from .serializers import LevelsSerializer
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from glucose.helpers import create_random_levels

class GlucoseTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user("john", "lennon@thebeatles.com", "johnpassword")
        Glucose.objects.create(
            device="device-1",
            serial_number="serial_number-1",
            device_timestamp='2023-01-15 07:42:08.000000',
            user=user,
            glucose_history=1.07,
            glucose_scan=3.07,
            carbohydrates_grams=10.22,
            carbohydrates_servings=4.47,
            glucose_test_strip=9.667,
            ketone=92.767,
        )
        Glucose.objects.create(
            device="device-2",
            serial_number="serial_number-2",
            device_timestamp='2024-01-16 07:42:08.000000',
            user=user,
            glucose_history=1.07,
            glucose_scan=3.07,
            carbohydrates_grams=10.22,
            carbohydrates_servings=4.47,
            glucose_test_strip=9.667,
            ketone=92.767
        )

    def test_glucose_model(self):
        device_glucose = Glucose.objects.get(device="device-1")
        serial_number_glucose = Glucose.objects.get(serial_number="serial_number-2")
        self.assertEqual(device_glucose.serial_number, 'serial_number-1')
        self.assertEqual(serial_number_glucose.device, 'device-2')


    def test_levels_serializer(self):
        device_glucose = Glucose.objects.get(device="device-1")
        level_serializer = LevelsSerializer(device_glucose,many=False)

        self.assertDictContainsSubset(
            subset={
                "device": device_glucose.device,
                "serial_number": device_glucose.serial_number,
                "glucose_history": device_glucose.glucose_history,
                "glucose_scan": device_glucose.glucose_scan,
                "carbohydrates_grams": device_glucose.carbohydrates_grams,
                "carbohydrates_servings": device_glucose.carbohydrates_servings,
                "glucose_test_strip": device_glucose.glucose_test_strip,
                "ketone": device_glucose.ketone,
            },
            dictionary=level_serializer.data
        )

class StudentListTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        user = User.objects.create_user("john", "lennon@thebeatles.com", "johnpassword")

        url = reverse('token_obtain_pair')
        resp = self.client.post(url, {'username':'john', 'password':'johnpassword'}, format='json')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + resp.data['access'])
        self.length = 100
        self.student_list = create_random_levels(self.length,user)

    def test_student_list(self):

        url = reverse('levels-view')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 10)
        self.assertEqual(response.data['count'], 100)
