class idselector:

    def __init__(self, id):
        if (id == "1"):
            self.ipAddress = "192.168.88.60"
            self.port = 502
            self.dbname = "CIP2-line1"
            self.slaveID = 1
        if (id == "2"):
            self.ipAddress = "192.168.88.60"
            self.port = 502
            self.dbname = "CIP2-line2"
            self.slaveID = 2
        if (id == "3"):
            self.ipAddress = "192.168.88.60"
            self.port = 502
            self.dbname = "CIP2-line3"
            self.slaveID = 3
        if (id == "4"):
            self.ipAddress = "192.168.88.60"
            self.port = 502
            self.dbname = "CIP2-line4"
            self.slaveID = 4
        if (id == "5"):
            self.ipAddress = "192.168.88.60"
            self.port = 502
            self.dbname = "CIP2-water"
            self.slaveID = 5

        if (id == "6"):
            self.ipAddress ="192.168.88.61"
            self.port = 502
            self.dbname = "utility-water-softner"
            self.slaveID = 1

        if (id == "7"):
            self.ipAddress ="192.168.88.61"
            self.port = 502
            self.dbname = "utility-Condens-10Bar"
            self.slaveID = 2

        if (id == "8"):
            self.ipAddress ="192.168.88.61"
            self.port = 502
            self.dbname = "utility-Condens-15Bar"
            self.slaveID = 3

        if (id == "9"):
            self.ipAddress ="192.168.88.61"
            self.port = 502
            self.dbname = "utility-Condens-6Bar"
            self.slaveID = 4
