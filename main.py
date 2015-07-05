from time import sleep

__author__ = 'neuraxis'
from dht import *


def main():

    sensor = Dht("1000")

    print(sensor.getname())
    sensor.setname("lplololol")
    print(sensor.getname())
    print(valsleeptime("2300"))
    sensor.run()
    temp = sensor.getaveragetemp()
    sleep(60)
    for i in temp:
        print(i)
    sleep(60)
if __name__ == "__main__":
    main()
