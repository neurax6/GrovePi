__author__ = 'neuraxis'
from dht import *
from sensor import *


def main():
    sensor = Dht()
    config = Sensor()
    config.addsensor(sensor)
    print(config.listsensor())


if __name__ == "__main__":
    main()