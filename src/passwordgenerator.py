
from abc import ABC, abstractmethod
from datetime import datetime, timedelta

class PasswordGenerator(ABC):
    """
    The PasswordGenerator interface declares operations common to all supported versions
    of some algorithm.
    """

    @abstractmethod
    def get_next_password(self) -> str:
        pass

    @abstractmethod
    def get_password_count(self) -> int:
        pass

class DatesGenerator(PasswordGenerator):

    def __init__(self, startdate: datetime, enddate: datetime, format: str):
        self.startdate = startdate
        self.enddate = enddate
        self.format = format

    def get_next_password(self) -> str:
        currentdate = self.startdate
        
        while currentdate <= self.enddate:
            yield currentdate.strftime(self.format)
            currentdate = currentdate + timedelta(days=1)
        
        return

    def get_password_count(self) -> int:
        delta = self.enddate - self.startdate
        return delta.days