import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')
application = get_wsgi_application()

# ML registry
import inspect
from apps.ml.registry import MLRegistry
from apps.ml.income_classifier.random_forest import RandomForestClassifier
from apps.ml.income_classifier.flight_predictor_rfr import RandomForestRegression
<<<<<<< HEAD
from apps.ml.income_classifier.flight_predictor_xgb import XGBRegression
from apps.ml.income_classifier.flight_predictor_dl import DLRegression
=======
>>>>>>> main
# from apps.ml.income_classifier.extra_trees import ExtraTreesClassifier # import ExtraTrees ML algorithm

try:
    registry = MLRegistry() # create ML registry
    # Random Forest classifier
    rf = RandomForestRegression()
    # add to ML registry
    registry.add_algorithm(endpoint_name="flight",
                            algorithm_object=rf,
                            algorithm_name="random forest",
                            algorithm_status="production",
                            algorithm_version="0.0.1",
                            owner="Mircea",
                            algorithm_description="Flight random forest",
                            algorithm_code=inspect.getsource(RandomForestRegression))
<<<<<<< HEAD
    
    xgb = XGBRegression()
    # add to ML registry
    registry.add_algorithm(endpoint_name="flight_xgboost",
                            algorithm_object=xgb,
                            algorithm_name="XGB",
                            algorithm_status="production",
                            algorithm_version="0.0.1",
                            owner="Mircea",
                            algorithm_description="Flight XGBoosting",
                            algorithm_code=inspect.getsource(XGBRegression))

    dl = DLRegression()
    # add to ML registry
    registry.add_algorithm(endpoint_name="flight_dl",
                            algorithm_object=dl,
                            algorithm_name="DL",
                            algorithm_status="production",
                            algorithm_version="0.0.1",
                            owner="Mircea",
                            algorithm_description="Flight Deep Learning",
                            algorithm_code=inspect.getsource(DLRegression))
=======
>>>>>>> main
    #registry = MLRegistry() # create ML registry
    # Random Forest classifier
    #rf = RandomForestClassifier()
    # add to ML registry
    #registry.add_algorithm(endpoint_name="income_classifier",
    #                        algorithm_object=rf,
    #                        algorithm_name="random forest",
    #                        algorithm_status="production",
    #                        algorithm_version="0.0.1",
    #                        owner="Piotr",
    #                        algorithm_description="Random Forest with simple pre- and post-processing",
    #                        algorithm_code=inspect.getsource(RandomForestClassifier))

    # Extra Trees classifier
    # et = ExtraTreesClassifier()
    # # add to ML registry
    # registry.add_algorithm(endpoint_name="income_classifier",
    #                         algorithm_object=et,
    #                         algorithm_name="extra trees",
    #                         algorithm_status="testing",
    #                         algorithm_version="0.0.2",
    #                         owner="Piotr",
    #                         algorithm_description="Extra Trees with simple pre- and post-processing",
    #                         algorithm_code=inspect.getsource(ExtraTreesClassifier))
    
except Exception as e:
    print("Exception while loading the algorithms to the registry,", str(e))
