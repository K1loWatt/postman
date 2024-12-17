from postman.connector import Connector
import pytest


def test_connector_unit():
    conn = Connector("origin", "pass", "uri", 9000)
    with pytest.raises(NotImplementedError):
        conn.connect()

    with pytest.raises(NotImplementedError):
        conn.disconnect()

    with pytest.raises(NotImplementedError):
        conn.send(None, None)
