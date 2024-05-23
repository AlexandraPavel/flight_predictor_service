from django.test import TestCase

from apps.ml.models.flight_predictor_rfr import RandomForestRegression
from apps.ml.models.flight_predictor_xgb import XGBRegression
from apps.ml.models.flight_predictor_dl import DLRegression
import inspect
from apps.ml.registry import MLRegistry

class MLTests(TestCase):
    def test_rf_algorithm(self):
        input_data = {
            'departure': 'Bucuresti',
            'destination': 'Atena',
            'flight_date': '23-12-2023',
            'arrival_date': '29-12-2023'
        }
        my_alg = RandomForestRegression()
        response = my_alg.compute_prediction(input_data)
        print(response)
        self.assertEqual('OK', response['status'])

    def test_xgb_algorithm(self):
        input_data = {
            'departure': 'Bucuresti',
            'destination': 'Atena',
            'flight_date': '23-12-2023',
            'arrival_date': '29-12-2023'
        }
        my_alg = XGBRegression()
        response = my_alg.compute_prediction(input_data)
        print(response)
        self.assertEqual('OK', response['status'])
    
    def test_dl_algorithm(self):
        input_data = {
            'departure': 'Bucuresti',
            'destination': 'Atena',
            'flight_date': '23-12-2023',
            'arrival_date': '29-12-2023'
        }
        my_alg = DLRegression()
        response = my_alg.compute_prediction(input_data)
        print(response)
        self.assertEqual('OK', response['status'])

    def test_registry(self):
        registry = MLRegistry()
        self.assertEqual(len(registry.endpoints), 0)
        endpoint_name = "flight"
        algorithm_object = RandomForestRegression()
        algorithm_name = "random forest"
        algorithm_status = "production"
        algorithm_version = "0.0.1"
        algorithm_owner = "Mircea"
        algorithm_description = "Flight random forest"
        algorithm_code = inspect.getsource(RandomForestRegression)
        # add to registry
        registry.add_algorithm(endpoint_name, algorithm_object, algorithm_name,
                    algorithm_status, algorithm_version, algorithm_owner,
                    algorithm_description, algorithm_code)
        # there should be one endpoint available
        self.assertEqual(len(registry.endpoints), 1)
