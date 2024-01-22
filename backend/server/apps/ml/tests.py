from django.test import TestCase

from apps.ml.income_classifier.flight_predictor_rfr import RandomForestRegression
<<<<<<< HEAD
from apps.ml.income_classifier.flight_predictor_xgb import XGBRegression
from apps.ml.income_classifier.flight_predictor_dl import DLRegression
=======
>>>>>>> main
import inspect
from apps.ml.registry import MLRegistry
# from apps.ml.income_classifier.extra_trees import ExtraTreesClassifier

class MLTests(TestCase):
    def test_rf_algorithm(self):
        input_data = {
            # "age": 37,
            # "workclass": "Private",
            # "fnlwgt": 34146,
            # "education": "HS-grad",
            # "education-num": 9,
            # "marital-status": "Married-civ-spouse",
            # "occupation": "Craft-repair",
            # "relationship": "Husband",
            # "race": "White",
            # "sex": "Male",
            # "capital-gain": 0,
            # "capital-loss": 0,
            # "hours-per-week": 68,
            # "native-country": "United-States"
            'departure': 'Bucuresti',
            'destination': 'Atena',
            'flight_date': '23-12-2023',
            'arrival_date': '29-12-2023'
        }
        my_alg = RandomForestRegression()
        response = my_alg.compute_prediction(input_data)
        print(response)
        self.assertEqual('OK', response['status'])
        #self.assertTrue('label' in response)
        #[self.assertEqual('<=50K', response['label'])

    def test_xgb_algorithm(self):
        input_data = {
            # "age": 37,
            # "workclass": "Private",
            # "fnlwgt": 34146,
            # "education": "HS-grad",
            # "education-num": 9,
            # "marital-status": "Married-civ-spouse",
            # "occupation": "Craft-repair",
            # "relationship": "Husband",
            # "race": "White",
            # "sex": "Male",
            # "capital-gain": 0,
            # "capital-loss": 0,
            # "hours-per-week": 68,
            # "native-country": "United-States"
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
            # "age": 37,
            # "workclass": "Private",
            # "fnlwgt": 34146,
            # "education": "HS-grad",
            # "education-num": 9,
            # "marital-status": "Married-civ-spouse",
            # "occupation": "Craft-repair",
            # "relationship": "Husband",
            # "race": "White",
            # "sex": "Male",
            # "capital-gain": 0,
            # "capital-loss": 0,
            # "hours-per-week": 68,
            # "native-country": "United-States"
            'departure': 'Bucuresti',
            'destination': 'Atena',
            'flight_date': '23-12-2023',
            'arrival_date': '29-12-2023'
        }
        my_alg = DLRegression()
        response = my_alg.compute_prediction(input_data)
        print(response)
        self.assertEqual('OK', response['status'])
    # def test_et_algorithm(self):
    #     input_data = {
    #         "age": 37,
    #         "workclass": "Private",
    #         "fnlwgt": 34146,
    #         "education": "HS-grad",
    #         "education-num": 9,
    #         "marital-status": "Married-civ-spouse",
    #         "occupation": "Craft-repair",
    #         "relationship": "Husband",
    #         "race": "White",
    #         "sex": "Male",
    #         "capital-gain": 0,
    #         "capital-loss": 0,
    #         "hours-per-week": 68,
    #         "native-country": "United-States"
    #     }
    #     my_alg = ExtraTreesClassifier()
    #     response = my_alg.compute_prediction(input_data)
    #     self.assertEqual('OK', response['status'])
    #     self.assertTrue('label' in response)
    #     self.assertEqual('<=50K', response['label'])

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
