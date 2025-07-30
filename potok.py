import time
from threading import Thread
import time
def green_light():
    print('Зелёный свет')
    time.sleep(2)
def yellow_light():
    print('Жёлтый свет')
    time.sleep(1)
def red_light():
    print('Красный свет')
    time.sleep(3)

svet1 = Thread(target=green_light)
svet2 = Thread(target=yellow_light)
svet3 = Thread(target=red_light)
svet2.run()
svet1.run()
svet3.run()
# я хотел порядок цветов жёлтый зелёный красный