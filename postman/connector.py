from dataclasses import dataclass, field
import smtplib
from email.mime.text import MIMEText
from postman.mail import Mail


@dataclass
class Connector:
    sender_email: str
    password: str
    smtp_server_uri: str
    port: int
    server: smtplib.SMTP = None
    is_connected: bool = False
    TLS = True

    def connect(self):
        raise NotImplementedError("Method not implemented")

    def send(self, mail: Mail, destination: str):
        raise NotImplementedError("Method not implemented")

    def disconnect(self):
        raise NotImplementedError("Method not implemented")


@dataclass
class Gmail(Connector):
    smtp_server_uri: str = field(default="smtp.gmail.com")
    port: int = field(default=587)
    TLS: bool = field(default=True)

    def connect(self):
        self.server = smtplib.SMTP(self.smtp_server_uri, self.port)
        if self.TLS:
            self.server.starttls()
        self.server.login(self.sender_email, self.password)
        self.is_connected = True

    def send(self, mail: Mail, destination: str):
        byte_string = mail.msg.encode("utf-8")
        self.server.sendmail(self.sender_email, destination, byte_string)

    def disconnect(self):
        if self.server:
            self.server.quit()
            self.server = None
        self.is_connected = False
