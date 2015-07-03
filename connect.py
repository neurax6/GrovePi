__author__ = 'neuraxis'
import psycopg2
import datetime


class Connection(object):
    """Class docstring."""

    # @contract(p_name='str')
    # @contract(p_sensor='int,>0')
    # @contract(p_mu='str')
    # @contract(p_sleep='bool')
    # @contract(p_sleep_time='str')
    # @contract(p_on='bool')
    def __init__(self, p_dbname, p_user, p_host, p_password,p_table_name,p_con=None,p_cur=None):
        self.__dbname = p_dbname
        self.__user = p_user
        self.__host = p_host
        self.__password = p_password
        self.__table_name = p_table_name
        self.__connection  = p_con
        self.__cursor  = p_cur
        #self.__con_chain="dbname={0} user={1} host={2} password={3}".format(self.__dbname,self.__user,self.__host,self.__password)

    def connect(self):
        try:
           self.__connection  = psycopg2.connect("dbname='raspy' user='postgres' host='192.168.0.103' password='M4lh4v0C'")
        except:
            print("I am unable to connect to the database")
    def create(self):
        try:
            self.__connection.set_isolation_level(0)
            self.__cursor.execute("CREATE TABLE dht (id serial PRIMARY KEY, num float, data varchar);")
        except:
            print("I can't drop our dht database! or your table is already created")
    def cursor(self):
        self.__cursor = self.__connection.cursor()
    def insert(self,p_temp,p_hum):
        date = str(datetime.datetime.now())
        self.__cursor.execute("INSERT INTO dht (num,num,data) VALUES (%s, %s,%s)",(p_temp,p_hum,date[0:len(date) - 7]))
    def commit(self):
        self.__connection.commit()
    def close(self):
        self.__connection.close()
