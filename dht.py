_author__ = 'neuraxis'
from contracts import contract, new_contract

from tools.validations import valsleeptime
import grovepi


class Dht(object):
    """Object Dht docstring.



        :precondition p_name: string
        :precondition p_sensor: int  & > 0
        :precondition p_mu: string: == C or == F
        :precondition p_sleep: Bool
        :precondition p_sleep_time: string & format '1000', '2300', '2359'
        :precondition p_data_hum: Float but initialised with None for a empty array.
        :precondition p_data_temp: Float but initialised with None for a empty array.
        :precondition p_average_hum: Float but initialised with None for a empty array.
        :precondition p_average_temp: Float but initialised with None for a empty array.


        :param p_name: Names of the device, dht in our case.
        :param p_sensor: Sensor device number on your GrovePi board.
        :param p_mu: Measurement unit , Celcius or Fahrenheits. Data are always stored in Celcius,changing the setting to 'F' will only affect display.
        :param p_sleep: Device sleeping ?
        :param p_sleep: Device sleeping at which time, using military format ex: '1000' for (10am) '2300' (11pm)
        :param p_on: Device reading data.
        :param p_data_temp: Array of float representing 1 reading of temperature each.
        :param p_data_hum: Array of float representing 1 reading of humidity each.
        :param p_average_temp: Array of float representing the average of 60 temperature reading each.
        :param p_average_hum: Array of float representing the average of 60 humidity reading each.

        :type p_average_hum: Float but initialised with None for a empty array.
        :type p_average_temp: Float but initialised with None for a empty array.
        :type p_data_hum: Float but initialised with None for a empty array.
        :type p_data_temp: Float but initialised with None for a empty array.
        :type p_mu: string: C or F
        :type p_name: string
        :type p_sleep: Bool
        :type p_sleep_time: string
        :type p_sensor: int


        """
    @new_contract
    def valsleeptime(x):
        if not valsleeptime(x):
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
    @contract(p_sleep_time='valsleeptime', )
    @contract(p_on='bool')
    @contract(p_data_temp='None')
    @contract(p_data_hum='None')
    @contract(p_average_temp='None')
    @contract(p_average_hum='None')
    def __init__(self, p_sleep_time, p_name="dht", p_sensor=5, p_mu="C", p_sleep=True, p_on=True, p_data_temp=None,
                 p_data_hum=None, p_average_temp=None, p_average_hum=None):
       if type(p_name)is not str:
        raise AssertionError("name is not a string: %r" % p_name)


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
        # string, military time format : 0000, 1200, 1900
        self.__sleep_time = p_sleep_time  #
        self.__on = p_on
        self.__dataTemp = p_data_temp
        self.__dataHum = p_data_hum
        self.__averageTemp = p_average_temp
        self.__averageHum = p_average_hum


    def getname(self):
        """
        Get device name.
        :return: :string:
        """
        return self.__name

    @contract(p_name='str')
    def setname(self, p_name):
        """
        :precondition string:
        :param p_name:
        """
        self.__name = p_name


    def getsensor(self):
        """


        :return: :int:
        """
        return self.__sensor

    @contract(p_sensor='int,>0')
    def setsensor(self, p_sensor):
        """
        :precondition p_sensor: int & >0
        :param p_sensor: int
        """
        self.__sensor = p_sensor


    def getmu(self):
        """


        :return: :String:
        """
        return self.__mu

    @contract(p_mu='corf')
    def setmu(self, p_mu):
        """

        :param p_mu:
        """
        self.__mu = p_mu

    @contract(p_sleep='bool')
    def setsleep(self, p_sleep):
        """

        :param p_sleep:
        """
        self.__sleep = p_sleep

    def getsleep(self):
        """


        :return: :rtype:
        """
        return self.__sleep

    @contract(p_sleep_time='valsleeptime', )
    def setsleeptime(self, p_sleep_time):
        """
        :param p_sleep_time:
        """
        self.__sleep_time = p_sleep_time

    def getsleeptime(self):
        """


        :return: :rtype:
        """
        return self.__sleep_time

    @contract(p_on='bool')
    def seton(self, p_on):
        """

        :rtype : object
        """
        self.__on = p_on

    def geton(self):
        """


        :return: :rtype:
        """
        return self.__on

    def getdatatemp(self):
        """


        :return: :rtype:
        """
        return self.__dataTemp

    @contract(p_data_temp='float')
    def setdatatemp(self, p_data_temp):
        """

        :param p_data_temp:
        """
        self.__dataTemp.append(p_data_temp)

    def getdatahum(self):
        """


        :return: :rtype:
        """
        return self.__dataHum

    @contract(p_data_hum='float')
    def setdatahum(self, p_data_hum):
        """

        :param p_data_hum:
        """
        self.__dataHum.append(p_data_hum)

    def getaveragetemp(self):
        """


        :return: :rtype:
        """
        return self.__averageTemp

    @contract(p_average_temp='float')
    def setaveragetemp(self, p_average_temp):
        """

        :param p_average_temp:
        """
        self.__averageTemp.append(p_average_temp)

    def getaveragehum(self):
        """


        :return: :rtype:
        """
        return self.__averageHum

    @contract(p_average_hum='float')
    def setaveragehum(self, p_average_hum):
        """

        :param p_average_hum:
        """
        self.__averageHum.append(p_average_hum)


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
        """


        """
        i=0
        while self.__on:

            try:

                if len(self.__dataTemp) == 59:
                    self.setaveragetemp(sum(self.__dataTemp) / 60)
                    del self.__dataTemp[:]
                if len(self.__dataHum) == 59:
                    self.setaveragehum(sum(self.__dataHum) / 60)
                    del self.__dataHum[:]
                [temp, humidity] = grovepi.dht(self.__sensor, 1)
                self.setdatatemp(float(temp)), self.setdatahum(float(humidity))
                print("entry #:",i,"temp =", temp, " humidity =", humidity)
                i+=1
            except IOError:
                print(0)







