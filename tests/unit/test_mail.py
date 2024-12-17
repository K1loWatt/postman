import pytest
from postman.mail import Mail


def test_mail():
    mail = Mail("Hello", "Test")
    assert str(mail) == "Subject: Test"
