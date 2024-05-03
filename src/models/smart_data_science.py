from enum import Enum
from pydantic import BaseModel


class MyException(Exception):
    pass

class Company:
    def __init__(self, symbol):
        self.name = None
        self.symbol = symbol
        self.sector = None
        self.industry = None
    
    def __str__(self) -> str:
        return self.name + self.symbol

class Index(str, Enum):
    FTSE100 = "FTSE 100"
    SNP500 = "S&P 500"
    DOWJONE = "Dow Jones"
    NDX100 = "Nasdaq 100"


# Note that the Configuration class inherits from the pydantic BaseModel. 
# This will enable us to generate automatic data schema documentation.
class Configuration(BaseModel):
    index: str = None

    index_map: dict = {
        Index.FTSE100: 'https://en.wikipedia.org/wiki/FTSE_100_Index',
        Index.SNP500: 'http://en.wikipedia.org/wiki/List_of_S%26P_500_companies',
        Index.NDX100: 'https://en.wikipedia.org/wiki/Nasdaq-100'
    }

    def get_url(self):
        return self.index_map[self.index]