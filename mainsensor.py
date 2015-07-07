__author__ = 'neuraxis'
from dht import *
from sensor import *


def main():
    sensor = Dht(p_link_id=666)
    sensor2 = Dht(p_link_id=667)
    config = Loader()
    config.addsensor(sensor)
    config.addsensor(sensor2)
    print(config.listsensor())


if __name__ == "__main__":
    main()