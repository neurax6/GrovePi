__author__ = 'neuraxis'
from dht import Dht
from sensor import Loader


def main():
    sensor = Dht()
    config = Loader()
    config.addsensor(sensor)
    print(config.listsensor())


if __name__ == "__main__":
    main()