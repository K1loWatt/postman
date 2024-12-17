from postman.connector import Gmail
from tests.conftest import FAKE_MAIL, FAKE_PASS
from postman.mail import Mail


def test_connector():
    conn = Gmail(FAKE_MAIL, FAKE_PASS, "localhost", 1025, tls=False)
    conn.connect()
    assert conn.is_connected == True

    mail = Mail("mensaje", "titulo")
    result = conn.send(mail, "Test2@localhost.com")
    assert not result

    conn.disconnect()
    assert conn.is_connected == False
