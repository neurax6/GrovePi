from time import sleep

__author__ = 'neuraxis'
from dht import *


def main():

    sensor = Dht()

    print(sensor.getname())
    sensor.setname("lplololol")
    print(sensor.getname())
    print(valsleeptime("2300"))
    sensor.run()
    temp = sensor.getaveragetemp()
if __name__ == "__main__":
    main()
