from django.test import TestCase
from rest_framework.test import APIClient

class EndpointTests(TestCase):

    def test_predict_view(self):
        client = APIClient()
        input_data = {
            'departure',
            'destination',
            'flight_date',
            'arrival_date',
        }
        classifier_url = "/api/v1/flight/predict"
        response = client.post(classifier_url, input_data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertTrue("request_id" in response.data)
        self.assertTrue("status" in response.data)

    def test_predict_view2(self):
        client = APIClient()
        input_data = {
            'departure',
            'destination',
            'flight_date',
            'arrival_date',
        }
        classifier_url = "/api/v1/flight_xgboost/predict"
        response = client.post(classifier_url, input_data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertTrue("request_id" in response.data)
        self.assertTrue("status" in response.data)
    
    def test_predict_view3(self):
        client = APIClient()
        input_data = {
            'departure',
            'destination',
            'flight_date',
            'arrival_date',
        }
        classifier_url = "/api/v1/flight_dl/predict"
        response = client.post(classifier_url, input_data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertTrue("request_id" in response.data)
        self.assertTrue("status" in response.data)
