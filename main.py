from time import sleep

__author__ = 'neuraxis'
from dht import *


def main():

    sensor = Dht()

    print(sensor.getname())
    sensor.setname("dht")
    print(sensor.getname())
    sensor.seton(True)
    print(sensor.readconfig())
    sensor.loadconfig("dht")
 #   sensor.configsave()
    print(sensor.readconfig())

    sensor.run()
    temp = sensor.getaveragetemp()
if __name__ == "__main__":
    main()
