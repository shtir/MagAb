#! /usr/bin/env python
# sudo pip install pyModbusTCP
from pyModbusTCP.client import ModbusClient
import datetime
from influxdb import InfluxDBClient
from env import *
import sys
from idselector import idselector

if ((len(sys.argv)) == 3):
    info = idselector(sys.argv[1])
    ipAddress = info.ipAddress
    port = info.port
    dbname = info.dbname
    mode = sys.argv[2]

else:
    print('less arguments!')
    print('STOPED!')
    exit()

time = datetime.datetime.utcnow()


class getdata:
    def __init__(self, address, port, id):
        c = ModbusClient()
        c.host(address)
        c.port(port)
        c.unit_id(id)
        c.open()

        data = c.read_input_registers(100, 22)
        c.close()
        if data:
            self.flow = data[0]
            self.total = (data[3] << 16 | data[4])
        else:
            print("Read Data ERROR")


MagAB = getdata(ipAddress, port, id)

measurement_name = dbname
body = [
    {
        "measurement": measurement_name,
        "time": time,
        "fields": {
            "Flow": MagAB.flow,
            "Total": MagAB.total,
        }
    }
]
