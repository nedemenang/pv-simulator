import math
from datetime import datetime


class Meter:

    def generate_meter_value(self):
        now = datetime.now()
        morning = now.replace(hour=4, minute=0, second=0, microsecond=0)
        evening = now.replace(hour=20, minute=0, second=0, microsecond=0)
        if morning <= now <= evening:
            x = (now - now.replace(hour=4, minute=0, second=0, microsecond=0)).total_seconds()
            return self.meter(x)
        return 0

    def meter(self, x):
        x = x / 3850
        value = math.sin(0.20 * x) + abs(math.sin(0.20 * x))
        meter_value = value * 1000
        return round(meter_value, 1)

