__author__ = 'neuraxis'
from dht import *
from validationsleeptime import *

def main():

    sensor = Dht("10:00")

    print(sensor.getname())
    sensor.setname("lplololol")
    print(sensor.getname())
    print(validesleeptime("2300"))
    sensor.run()
    temp = sensor.getaveragetemp()
    print(temp[0])
if __name__ == "__main__":
    main()
