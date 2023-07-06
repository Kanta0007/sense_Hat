from sense_hat import SenseHat
from signal import pause
from datetime import datetime

sense = SenseHat()
sense.clear()

dt = datetime.now()

temp = round(sense.get_temperature(),1)
humi = round(sense.get_humidity(), 1)
press = round(sense.get_pressure(), 1)

while True:
    for event in sense.stick.get_events():
        if event.direction == 'up':
            sense.show_message("{}".format(temp))

        if event.direction == 'left':
            sense.show_message("{}".format(humi))

        if event.direction == 'right':
            sense.show_message("{}".format(press))

        if event.action == 'released':
            sense.show_message("")

        if event.direction == 'down':
            if (temp <= 28 and temp >= 25) {
                if (humi <= 60 and humi >= 45) {
                    sense.show_message('快適')
                }
            } else {
                sense.show_message('快適ではない')
            }
