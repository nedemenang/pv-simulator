# PV SIMULATOR CHALLENGE

## This application generates sample photovoltaic power values to mimic a power profile

The PV simulator project contains the following components that perform the following tasks:

* Meter: This component produces messages to a broker with random but continuous values from 0 to 9000watts.
* Broker: RabbitMQ was used as a broker to receive messages passed from the meter.
* PV simulator: This listens to the meter for meter values, generates a random PV value, adds the value to the meter value and outputs the result.
* Output.json file: This receives the values generated from the PV simulator.

## How to Run the Project

* Open the pv-simulator folder in a terminal window and run the following commands in order
    * `virtualenv venv --python=python3.6`
    * `source venv/bin/activate`
    * `pip install -r requirements.txt`
    * `./install_redis.sh`
    * `./redis-5.0.4/src/redis-server`

* Open another terminal window and run the following command from the pv-simulator folder
    * `source venv/bin/activate`
    * `celery beat -A app.celery --schedule=/tmp/celerybeat-schedule --loglevel=INFO --pidfile=/tmp/celerybeat.pid`
    
* Open another terminal window and run the following command from the pv-simulator folder
    * `source venv/bin/activate`
    * `celery worker -A app.celery --loglevel=INFO`

* Open another terminal window and run the following command from the pv-simulator folder
    * `source venv/bin/activate`
    * ` python ./app/simulator/pv_simulator.py `
    

After approximately a minute, an output.json folder will be created in the root directory of the pv-simulator folder. Open it to view the results.

