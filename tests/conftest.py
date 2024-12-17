from postman.connector import Connector
from dataclasses import dataclass


FAKE_MAIL = "test@localhost.com"
FAKE_PASS = "pass"


@dataclass
class FakeConn(Connector):
    sended = False

    def connect(self):
        self.is_connected = True

    def disconnect(self):
        self.is_connected = False

    def send(self, mail, destination):
        self.sended = True
        return {}
