#! /usr/bin/env python
# sudo pip install pyModbusTCP
from pyModbusTCP.client import ModbusClient
import datetime
from influxdb import InfluxDBClient
from env import *
import sys
from idselector import idselector

if ((len(sys.argv)) == 2):
    info = idselector(sys.argv[1])
    ipAddress = info.ipAddress
    port = info.port
    dbname = info.dbname
    slaveID = info.slaveID

else:
    print('less arguments!')
    print('STOPED!')
    exit()

time = datetime.datetime.utcnow()


class getdata:
    def __init__(self, address, port, slaveID):
        c = ModbusClient()
        c.host(address)
        c.port(port)
        c.unit_id(slaveID)
        c.open()

        data = c.read_holding_registers(100, 22)
        c.close()
        if data:
            self.flow = float(data[0])
            self.total = ((data[3]*1000)+ data[4])/1000
        else:
            print("Read Data ERROR")


MagAB = getdata(ipAddress, port, slaveID)

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
#print(body)


ifclient = InfluxDBClient(ifhost, ifport, ifuser, ifpass, ifdb)
ifclient.write_points(body)