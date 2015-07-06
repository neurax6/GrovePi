_author__ = 'neuraxis'
from contracts import contract, new_contract

from tools.validations import valsleeptime, corf
import grovepi


class Dht(object):
    """Object Dht docstring.



        :precondition p_name: Must be a string
        :precondition p_sensor: Must be a  integer  & > 0
        :precondition p_mu: Must be a string and == C or F
        :precondition p_sleep: Must be a bool
        :precondition p_data_hum: Must be a float but initialised with None for a empty array.
        :precondition p_data_temp: Must be a float but initialised with None for a empty array.
        :precondition p_average_hum: Must be a float but initialised with None for a empty array.
        :precondition p_average_temp: Must be a float but initialised with None for a empty array.
        :precondition p_link: Must be a string but initialised with None.
        :precondition p_link_id: Must be a string but initialised with None for a empty array.


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
        :param p_link: A string representing the id of the linked device(ex: coil1)
        :param p_link_id: A string representing the id of the device(ex: dht1)

        :type p_average_hum: Float but initialised with None for a empty array.
        :type p_average_temp: Float but initialised with None for a empty array.
        :type p_data_hum: Float but initialised with None for a empty array.
        :type p_data_temp: Float but initialised with None for a empty array.
        :type p_mu: String:
        :type p_name: String
        :type p_sleep: Bool
        :type p_sleep_time: String
        :type p_sensor: Integer
        :type p_link: String
        :type p_link_id: String

        """


    def __init__(self, p_name='dht', p_sensor=5, p_mu="C", p_sleep=False, p_on=False, p_data_temp=None,
                 p_data_hum=None, p_average_temp=None, p_average_hum=None, p_link_id=None, p_link=None):
        init = 0
        if not isinstance(p_name, str):
            raise AssertionError("name is not a string:", p_name)
        if not isinstance(p_sensor, int):
            raise AssertionError("The sensor must be a int > 0", p_sensor)
        if p_sensor < 0:
            raise AssertionError("The sensor must be a int > 0", p_sensor)
        if not isinstance(p_mu, str):
            raise AssertionError("The sensor measurement unit  must be  a string 'C' or 'F'", p_mu)
        if not corf(p_mu):
            raise AssertionError("The sensor measurement unit  must be 'C' or 'F'", p_mu)
        if not isinstance(p_sleep, bool):
            raise AssertionError("Must be a bool , sleep? True/1 or False/0", p_sleep)
        if not isinstance(p_on, bool):
            raise AssertionError("The sensor must be on or off, based on a bool", p_on)
        if not init:
            if p_data_temp is not None:
                raise AssertionError("Must not be set on start", p_data_temp)
            if p_data_hum is not None:
                raise AssertionError("Must not be set on start", p_data_hum)
            if p_average_temp is not None:
                raise AssertionError("Must not be set on start", p_average_temp)
            if p_average_hum is not None:
                raise AssertionError("Must not be set on start", p_average_hum)
        if init:
            if not isinstance(p_data_temp, float):
                raise AssertionError("Must not be set on start", p_data_temp)
            if not isinstance(p_data_hum, float):
                raise AssertionError("Must not be set on start", p_data_hum)
            if not isinstance(p_average_temp, float):
                raise AssertionError("Must not be set on start", p_average_temp)
            if not isinstance(p_average_temp, float):
                raise AssertionError("Must not be set on start", p_average_hum)
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
        self.__on = p_on
        self.__dataTemp = p_data_temp
        self.__dataHum = p_data_hum
        self.__averageTemp = p_average_temp
        self.__averageHum = p_average_hum
        self.__link = p_link
        self.__link_id = p_link_id
        init += 1

    def setmu(self, p_mu):
        """
            :precondition p_mu must be string
            :precondition p_mu must be C or F
            :param p_mu: Measurement unit, C or F.
        """
        if not isinstance(p_mu, str):
            raise AssertionError("The sensor measurement unit  must be  a string 'C' or 'F'", p_mu)
        if not corf(p_mu):
            raise AssertionError("The sensor measurement unit  must be 'C' or 'F'", p_mu)
        self.__mu = p_mu

    def setsleep(self, p_sleep):
        """

            :param p_sleep:

        """
        if not isinstance(p_sleep, bool):
            raise AssertionError("Must be a bool , sleep? True/1 or False/0", p_sleep)
        self.__sleep = p_sleep


    def setsensor(self, p_sensor):
        """
            :precondition p_sensor: int & >0
            :param p_sensor: int
        """
        if not isinstance(p_sensor, int):
            raise AssertionError("The sensor must be a int > 0", p_sensor)
        if p_sensor < 0:
            raise AssertionError("The sensor must be a int > 0", p_sensor)
        self.__sensor = p_sensor


    def setname(self, p_name):
        """
            :precondition string:
            :param p_name:
        """
        if not isinstance(p_name, str):
            raise AssertionError("name is not a string:", p_name)
        self.__name = p_name


    def seton(self, p_on):
        """

            :rtype : object
        """
        if not isinstance(p_on, bool):
            raise AssertionError("The sensor must be on or off, based on a bool", p_on)
        self.__on = p_on


    def setdatatemp(self, p_data_temp):
        """

            :param p_data_temp:
        """
        if not isinstance(p_data_temp, float):
            raise AssertionError("Must not be set on start", p_data_temp)

        self.__dataTemp.append(p_data_temp)


    def setdatahum(self, p_data_hum):
        """

            :param p_data_hum:
        """
        if not isinstance(p_data_hum, float):
            raise AssertionError("Must not be set on start", p_data_hum)
        self.__dataHum.append(p_data_hum)


    def setaveragetemp(self, p_average_temp):
        """

            :param p_average_temp:
        """
        if not isinstance(p_average_temp, float):
            raise AssertionError("Must not be set on start", p_average_temp)
        self.__averageHum.append(p_average_temp)


    def setaveragehum(self, p_average_hum):
        """

            :param p_average_hum:
        """
        if not isinstance(p_average_hum, float):
            raise AssertionError("Must not be set on start", p_average_hum)
        self.__averageHum.append(p_average_hum)


    def setlink(self, p_link):
        """

            :param p_link:
        """
        if not isinstance(p_link, str):
            raise AssertionError("Must be a string", p_link)
        self.__link = p_link


    def setlinkid(self, p_link_id):
        """

            :param p_link_id:
        """
        if not isinstance(p_link_id, str):
            raise AssertionError("Must be a string", p_link_id)
        self.__p_link_id = p_link_id


    def getname(self):
        """
            Get device name.
            :return: :string:
        """
        return self.__name


    def getsensor(self):
        """
            :return: :int:
        """
        return self.__sensor


    def getmu(self):
        """


            :return: :String:
        """
        return self.__mu


    def getsleep(self):
        """


            :return: :rtype:
        """
        return self.__sleep


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


    def getdatahum(self):
        """


            :return: :rtype:
        """
        return self.__dataHum


    def getaveragetemp(self):
        """


            :return: :rtype:
        """
        return self.__averageTemp


    def getaveragehum(self):
        """


            :return: :rtype:
        """
        return self.__averageHum


    def getlink(self):
        """


            :return: :rtype:
        """
        return self.__link


    def getlinkid(self):
        """


            :return: :rtype:
        """
        return self.__link_id


    name = property(getname, setname)
    sensor = property(getsensor, setsensor)
    mu = property(getmu, setmu)
    sleep = property(getsleep, setsleep)
    on = property(geton, seton)
    link = property(getlink, setlink)
    link_id = property(getlinkid, setlinkid)
    data_temp = property(getdatatemp, setdatatemp)
    data_hum = property(getdatahum, setdatahum)
    average_temp = property(getaveragetemp, setaveragetemp)
    average_hum = property(getaveragehum, setaveragehum)


    def run(self):
        """
        × 1.8 + 32
        """
        i = 0
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
                if self.__mu == 'F':
                    temp = (temp * 1.8) + 32
                    print("entry #:", i, "temp =", temp, self.getmu(), " humidity =", humidity)
                    i += 1
                else:
                    print("entry #:", i, "temp =", temp, self.getmu(), " humidity =", humidity)
                    i += 1
            except IOError:
                print(0)

    def configsave(self):
        '{0}, {1}, {2}'.format('a', 'b', 'c')
        t = "{0}.cfg".format(self.getname())
        try:
            f = open(t, 'w')
        except:
            print("non")
        f.write("{0}{1}".format(self.getname(), "\n"))
        f.write("{0}{1}".format(self.getsensor(), "\n"))
        f.write("{0}{1}".format(self.getmu(), "\n"))
        f.write("{0}{1}".format(self.getsleep(), "\n"))
        f.write("{0}{1}".format(self.geton(), "\n"))
        f.write("{0}{1}".format(self.getlink(), "\n"))
        f.write("{0}{1}".format(self.getlinkid(), "\n"))
        f.closed()




