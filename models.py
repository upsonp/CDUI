from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String


class Base(DeclarativeBase):
    pass


# class Data(Base):
#     __tablename__ = 'DATA'
#
#
# class Cruise(Base):
#     __tablename__ = 'CRUISE'
#

class ChiefScientist(Base):
    __tablename__ = 'CHIEF_SCIENTIST'
    first_name: Mapped[str] = mapped_column(String(50), primary_key=True)
    last_name: Mapped[str] = mapped_column(String(200), primary_key=True)

    def __repr__(self):
        return f"{self.last_name}, {self.first_name}"
#
# class DataType(Base):
#     __tablename__ = 'DATA_TYPE'
#
#
# class DeliveryStage(Base):
#     __tablename__ = 'DELIVERY_STAGE'
#
#
# class ProcessState(Base):
#     __tablename__ = 'PROCESS_STATE'