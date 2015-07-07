__author__ = 'neuraxis'
from dht import *
from sensor import *


def main():
    sensor = Dht(p_link=5, p_link_id=1)
    sensor2 = Dht(p_link=6, p_link_id=2)
    sensor3 = Dht(p_link=7, p_link_id=3)
    config = Loader()
    config.addsensor(sensor)
    config.addsensor(sensor2)
    print(config.listsensor())
    config.delsensor(1)
    print(config.listsensor())
    config.addsensor(sensor3)
    print(config.listsensor())
if __name__ == "__main__":
    main()