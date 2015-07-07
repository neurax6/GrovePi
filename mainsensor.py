__author__ = 'neuraxis'
from dht import *
from sensor import *


def main():
    sensor = Dht(p_link=666, p_link_id=667)
    sensor2 = Dht(p_link=667, p_link_id=666)
    sensor3 = Dht(p_link=677, p_link_id=777)
    config = Loader()
    config.addsensor(sensor)
    config.addsensor(sensor2)
    print(config.listsensor())
    config.delsensor(666)
    print(config.listsensor())
    config.addsensor(sensor3)
    print(config.listsensor())
if __name__ == "__main__":
    main()