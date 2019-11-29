import pika
import math
import decimal
import random
from datetime import datetime
from generate_output import GenerateOutput


class PV:

    def generate_pv_value(self):
        now = datetime.now()
        morning = now.replace(hour=8, minute=0, second=0, microsecond=0)
        evening = now.replace(hour=20, minute=0, second=0, microsecond=0)
        if morning <= now <= evening:
            x = (now - now.replace(hour=8, minute=0, second=0, microsecond=0)).total_seconds()
            return self.pv(x)
        return 0

    def pv(self, x):
        x = x / 3850
        round(float(decimal.Decimal(random.randrange(50, 65)) / 100), 1)
        value = math.sin(0.27 * x) + abs(math.sin(0.27 * x))
        pv_value = 0.7 * value
        return round(pv_value, 1)


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='meter')


def callback(ch, method, properties, body):
    pv_simulator = PV()
    meter_value = round(float(body)/1000, 1)
    pv_value = pv_simulator.generate_pv_value()
    output = {
        'meter_value': round(float(body), 1),
        "pv_value": pv_value,
        "sum": round(meter_value + pv_value, 1),
        "timestamp": str(datetime.now())
    }
    generate_output = GenerateOutput()
    generate_output.generate_output(output)


channel.basic_consume(queue='meter', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
