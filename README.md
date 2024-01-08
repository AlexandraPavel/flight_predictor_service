# Machine Learning Models with Django

Put more memory in the docker desktop settings in order to train the model:
cpu: max 8
memory limit: 8.5 GB
swap: 1gb
virtual disk limit: 64GB

Training of the model can be done on google colab using

research/train_flight_classifier.ipynb
and
research/flight_training.py

or it can be done in the container (enviroment settings are included)

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




Data input prediction:

{
	"date_of_enquiry": "2023-12-02",
 
	"departure": "Bucuresti",
 
	"destination": "Istanbul",
 
	"flight_date": "2023-12-20",
 
	"flight_time": "16:25",
 
	"arrival_time": "18:40",
 
	"airline": "AF",
 
	"layovers": 0,
 
	"flight_duration": 75
}
