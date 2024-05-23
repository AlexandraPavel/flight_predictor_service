# Machine Learning Models with Django
Requirements:

	Ubuntu Jammy Jellyfish 22.04
 	Docker Desktop

Put more memory in the docker desktop settings in order to train the model:

	cpu: max 8
	memory limit: 8.5 GB
	swap: 1gb
	virtual disk limit: 64GB

Training of the model was done in colab: https://github.com/AlexandraPavel/PriceFlightEstimator

Before starting the development in .devcontainer, run:

	docker-compose build
 
	docker-compose up

How to open the folder in a container vs code
https://code.visualstudio.com/docs/devcontainers/containers

Run the app in terminal vscode inside the container (changing the ports)

	cd backend/server/

if migrations is commented in /app/docker/backend/wsgi-entrypoint.sh:

	python3 ./manage.py migrate

then:

	python3 ./manage.py runserver 8000

Backend models:

	flight
	flight_xgboost
	flight_dl


The application is at: 

	http://127.0.0.1:8080/api/v1/flight_prediction


Data input prediction:

	{
		"departure": "Bucuresti",
		"destination": "Istanbul",
		"flight_date": "23-12-2023",
		"arrival_date": "29-12-2023"
	}
