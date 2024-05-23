import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')
application = get_wsgi_application()

# ML registry
import inspect
from apps.ml.registry import MLRegistry
from apps.ml.models.flight_predictor_rfr import RandomForestRegression
from apps.ml.models.flight_predictor_xgb import XGBRegression
from apps.ml.models.flight_predictor_dl import DLRegression
try:
    registry = MLRegistry() # create ML registry
    # Random Forest model
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
except Exception as e:
    print("Exception while loading the algorithms to the registry,", str(e))
