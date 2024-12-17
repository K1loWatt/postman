from dataclasses import dataclass


class Template:
    pass


@dataclass
class Mail:
    body: str
    subject: str

    @property
    def msg(self):
        return f"Subject: {self.subject}\n\n{self.body}"

    def __str__(self):
        return f"Subject: {self.subject}"
