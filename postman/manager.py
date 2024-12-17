from dataclasses import dataclass
from postman.connector import Connector
from postman.mail import Mail


@dataclass
class Manager:
    connector: Connector

    def send(self, mail: Mail, destination: str) ->:

        if not self.connector.is_connected:
            self.connector.connect()
        result = self.connector.send(mail, destination)

        self.connector.disconnect()

        return result
