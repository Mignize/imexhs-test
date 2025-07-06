from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base
from datetime import timezone

class Device(Base):
    __tablename__ = "devices"
    id = Column(Integer, primary_key=True, index=True)
    device_name = Column(String, unique=True)

class Element(Base):
    __tablename__ = "elements"
    id = Column(String, primary_key=True, index=True)
    device_id = Column(Integer, ForeignKey("devices.id"))
    avg_before_norm = Column(Float)
    avg_after_norm = Column(Float)
    data_size = Column(Integer)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    device = relationship("Device")
