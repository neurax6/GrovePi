__author__ = 'neuraxis'
from connect import Connection
def main():
    test = Connection("raspy","postgres","192.168.0.103","yolo","dht")
    test.connect()
    test.cursor()
    test.create()

    test.commit()
    test.close()

if __name__ == "__main__":
    main()

