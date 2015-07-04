_author__ = 'neuraxis'
from contracts import contract, new_contract
from validationsleeptime import *
import grovepi
"""Class docstring.
    :type p_data_hum: float
    :type p_on: Bool
    :type p_sleep: Bool
"""


# Connect the Grove Temperature & Humidity Sensor Pro to digital port D4
# SIG,NC,VCC,GND
class Dht(object):
    """Class docstring.

        :type p_data_hum: float
        :type p_on: Bool
        :type p_sleep: Bool
    """
    @new_contract
    def valsleeptime(x):
        if not validesleeptime(x):
            msg = 'Invalid format.'
            raise ValueError(msg)
    @new_contract
    def corf(x):
        if not 'C' or not 'F':
            msg = 'Invalid entry: C or F'
            raise ValueError(msg)

    @contract(p_name='str')
    @contract(p_sensor='int,>0')
    @contract(p_mu='corf')
    @contract(p_sleep='bool')
    @contract(p_sleep_time='valsleeptime',)
    def f(x):
        pass

    @contract(p_on='bool')
    def __init__(self, p_sleep_time, p_name="dht", p_sensor=5, p_mu="C", p_sleep=True, p_on=True, p_data_temp=None,
                 p_data_hum=None, p_average_temp=None, p_average_hum=None):


        """Method docstring.
        :type p_data_hum: float
        :type p_on: Bool
        :type p_sleep: Bool
        """
        if not p_data_temp:
            p_data_temp = []
        if not p_data_hum:
            p_data_hum = []
        if not p_average_temp:
            p_average_temp = []


        if not p_average_hum:
            p_average_hum = []
        self.__name = p_name  # Name &/or description of the sensor.
        self.__sensor = p_sensor  # Sensor number
        self.__mu = p_mu  # Measurement Unit.
        # Bool,device sleep,running 24/24 ?
        self.__sleep = p_sleep
        # string, millitary time format : 0000, 1200, 1900
        self.__sleep_time = p_sleep_time  #
        self.__on = p_on
        self.__dataTemp = p_data_temp
        self.__dataHum = p_data_hum
        self.__averageTemp = p_average_temp
        self.__averageHum = p_average_hum
        """Get and set"""



    def getname(self):
        return self.__name
    @contract(p_name='str')
    def setname(self, p_name):
        self.__name = p_name

    def getdatatemp(self):
        return self.__dataTemp

    def setdatatemp(self, p_data_temp):
        self.__dataTemp.append(p_data_temp)

    def getdatahum(self):
        return self.__dataHum

    def setdatahum(self, p_data_hum):
        self.__dataHum.append(p_data_hum)

    def getaveragetemp(self):
        return self.__averageTemp

    def setaveragetemp(self, p_average_temp):
        self.__averageTemp.append(p_average_temp)

    def getaveragehum(self):
        return self.__averageHum

    def setaveragehum(self, p_average_hum):
        self.__averageHum.append(p_average_hum)

    def getsensor(self):
        return self.__sensor

    def setsensor(self, p_sensor):
        self.__sensor = p_sensor

    def setmu(self, p_mu):
        self.__mu = p_mu

    def getmu(self):
        return self.__mu

    def setsleep(self, p_sleep):
        self.__sleep = p_sleep

    def getsleep(self):
        return self.__sleep

    def setsleeptime(self, p_sleep_time):
        self.__sleep_time = p_sleep_time

    def getsleeptime(self):
        return self.__sleep_time

    def seton(self, p_on):
        self.__on = p_on

    def geton(self):
        return self.__on

    name = property(getname, setname)
    sensor = property(getsensor, setsensor)
    mu = property(getmu, setmu)
    sleep = property(getsleep, setsleep)
    sleep_time = property(getsleeptime, setsleeptime)
    on = property(geton, seton)
    data_temp = property(getdatatemp, setdatatemp)
    data_hum = property(getdatahum, setdatahum)
    average_temp = property(getaveragetemp, setaveragetemp)
    average_hum = property(getaveragehum, setaveragehum)


    def run(self):
        while self.__on:
            try:
                if len(self.__dataTemp) == 59:
                    self.setaveragetemp(sum(self.__dataTemp)/60)
                    del self.__dataTemp[:]
                if len(self.__dataHum) == 59:
                    self.setaveragehum(sum(self.__dataTemp)/60)
                    del self.__dataHum[:]
                [temp, humidity] = grovepi.dht(self.__sensor, 1)
                self.setdatatemp(temp), self.setdatahum(humidity)
                print("temp =", temp, " humidity =", humidity)
            except IOError:
                print(0)







