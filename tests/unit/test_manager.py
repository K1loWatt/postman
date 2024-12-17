import pytest
from tests.conftest import FakeConn
from postman.manager import Manager
from postman.mail import Mail


def test_manager():
    conn = FakeConn("origin", "pass", "uri", 9000)
    manager = Manager(conn)
    mail = Mail("Hello", "Test")
    result = manager.send(mail, "msg")

    assert conn.sended == True
    assert conn.is_connected == False
    assert not result
