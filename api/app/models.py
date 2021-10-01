import sqlalchemy as sqa
from sqlalchemy import Integer, String, Numeric
from sqlalchemy.sql.schema import Column
from .database import Base

    
class Morth(Base):
    __tablename__ = 'morth'
    id = Column(Integer, primary_key=True)
    Name = Column(String, nullable=False)
    Date = Column(sqa.Date, nullable=False)
    PolygonId = Column(Integer, nullable=False)
    ZeroZero = Column(Numeric, nullable=False)
    ZeroOne = Column(Numeric, nullable=False)
    OneZero = Column(Numeric, nullable=False)
    OneOne = Column(Numeric, nullable=False)


class Otherinsect(Base):
    __tablename__ = 'otherinsect'
    id = Column(Integer, primary_key=True)
    Name = Column(String, nullable=False)
    Date = Column(sqa.Date, nullable=False)
    PolygonId = Column(Integer, nullable=False)
    ZeroZero = Column(Numeric, nullable=False)
    ZeroOne = Column(Numeric, nullable=False)
    OneZero = Column(Numeric, nullable=False)
    OneOne = Column(Numeric, nullable=False)


class Butterfly(Base):
    __tablename__ = 'butterfly'
    id = Column(Integer, primary_key=True)
    Name = Column(String, nullable=False)
    Date = Column(sqa.Date, nullable=False)
    PolygonId = Column(Integer, nullable=False)
    ZeroZero = Column(Numeric, nullable=False)
    ZeroOne = Column(Numeric, nullable=False)
    OneZero = Column(Numeric, nullable=False)
    OneOne = Column(Numeric, nullable=False)


class Spider(Base):
    __tablename__ = 'spider'
    id = Column(Integer, primary_key=True)
    Name = Column(String, nullable=False)
    Date = Column(sqa.Date, nullable=False)
    PolygonId = Column(Integer, nullable=False)
    ZeroZero = Column(Numeric, nullable=False)
    ZeroOne = Column(Numeric, nullable=False)
    OneZero = Column(Numeric, nullable=False)
    OneOne = Column(Numeric, nullable=False)


class Odonata(Base):
    __tablename__ = 'odonata'
    id = Column(Integer, primary_key=True)
    Name = Column(String, nullable=False)
    Date = Column(sqa.Date, nullable=False)
    PolygonId = Column(Integer, nullable=False)
    ZeroZero = Column(Numeric, nullable=False)
    ZeroOne = Column(Numeric, nullable=False)
    OneZero = Column(Numeric, nullable=False)
    OneOne = Column(Numeric, nullable=False)


class Coleoptera(Base):
    __tablename__ = 'coleoptera'
    id = Column(Integer, primary_key=True)
    Name = Column(String, nullable=False)
    Date = Column(sqa.Date, nullable=False)
    PolygonId = Column(Integer, nullable=False)
    ZeroZero = Column(Numeric, nullable=False)
    ZeroOne = Column(Numeric, nullable=False)
    OneZero = Column(Numeric, nullable=False)
    OneOne = Column(Numeric, nullable=False)

    
class Info(Base):
    __tablename__ = 'info'
    id = Column(Integer, primary_key=True)
    Name = Column(String, nullable=False)
    Kingdom = Column(String, nullable=False)
    Class = Column(String, nullable=False)
    Family = Column(String, nullable=False)
    Taxa = Column(String, nullable=False)
    Count = Column(Integer, nullable=False)