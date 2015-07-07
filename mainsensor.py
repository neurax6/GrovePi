__author__ = 'neuraxis'
from dht import Dht
from sensor import Sensor


def main():
    sensor = Dht()
    config = Sensor()
    config.addsensor(sensor)
    print(config.listsensor())


if __name__ == "__main__":
    main()