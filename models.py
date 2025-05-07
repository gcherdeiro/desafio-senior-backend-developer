from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    hashed_password = Column(String(255))
    
    documents = relationship("Documents", back_populates="user")

class Cpf(Base):
    __tablename__ = "cpf"

    id = Column(Integer, primary_key=True, index=True)
    number = Column(String(11), unique=True, index=True)
    name = Column(String(50))
    issued_by = Column(String(50))
    issued_date = Column(Date)

class Rg(Base):
    __tablename__ = "rg"

    id = Column(Integer, primary_key=True, index=True)
    number = Column(String(10), unique=True, index=True)
    name = Column(String(50))
    issued_by = Column(String(50))
    issued_date = Column(Date)

class Cnh(Base):
    __tablename__ = "cnh"

    id = Column(Integer, primary_key=True, index=True)
    number = Column(String(11), unique=True, index=True)
    name = Column(String(50))
    uf = Column(String(2))
    issued_by = Column(String(50))
    issued_date = Column(Date)
    expiration_date = Column(Date)
    category = Column(String(2))

class VaccinationCard(Base):
    __tablename__ = "vaccination_card"

    id = Column(Integer, primary_key=True, index=True)
    number = Column(String(11), unique=True, index=True)
    name = Column(String(50))
    birth_date = Column(Date)
    issued_date = Column(Date)
    expiration_date = Column(Date)
    gender = Column(String(1))

class Documents(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    cpf_id = Column(Integer, ForeignKey("cpf.id"), nullable=True)
    rg_id = Column(Integer, ForeignKey("rg.id"), nullable=True)
    cnh_id = Column(Integer, ForeignKey("cnh.id"), nullable=True)
    vaccination_card_id = Column(Integer, ForeignKey("vaccination_card.id"), nullable=True)

    user = relationship("Users", back_populates="documents")
    cpf = relationship("Cpf", backref="documents")
    rg = relationship("Rg", backref="documents")
    cnh = relationship("Cnh", backref="documents")
    vaccination_card = relationship("VaccinationCard", backref="documents")