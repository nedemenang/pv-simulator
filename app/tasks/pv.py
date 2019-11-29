import celery
import pika
from app.meter.meter import Meter
from app import app


@celery.task()
def meter():
    with app.app_context():
        pv_meter = Meter()
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()

        channel.queue_declare(queue='meter')

        channel.basic_publish(exchange='',
                              routing_key='meter',
                              body=str(pv_meter.generate_meter_value()))
        print('Sent Meter value')
