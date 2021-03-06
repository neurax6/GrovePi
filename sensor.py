__author__ = 'neuraxis'
import copy
import dht


class Loader(object):
    def __init__(self, p_linked_list=None, p_sensor_list=None, ):
        if not p_sensor_list:
            p_sensor_list = []
        if not p_linked_list:
            p_linked_list = []
        self.__sensorlist = p_sensor_list
        self.__linkedlist = p_linked_list

    def addsensor(self, p_object):
        self.__sensorlist.append(copy.deepcopy(p_object))

    def delsensor(self, p_linkid):
        i = 0
        while i < len(self.__sensorlist):
            test = self.__sensorlist[i]
            if p_linkid == test.getlinkid():
                self.__sensorlist.remove(self.__sensorlist[i])
                i += 1
            else:
                i += 1


    def listsensor(self):
        i = 0
        while i < len(self.__sensorlist):
            print(self.__sensorlist[i].readconfig())
            i += 1

            # def addlink(self):
            #
            #def dellink(self):
            #
            #def listlink(self):
            #
            #def saveconfig(self):
