from pydantic import BaseModel
from typing import Optional, Union, NewType, Tuple, List, Dict, DefaultDict
import datetime

Date = NewType('Date', datetime.datetime)


class CreateSpiderRequest(BaseModel):
    Name : str
    Date : Date
    PolygonId : int
    ZeroZero : float
    ZeroOne : float
    OneZero : float
    OneOne : float
    
# class CreateInfoRequest(BaseModel):
#     Name : str
#     Kingdom : str
#     Class : str
#     Family : str
#     Taxa : str
#     Count : int