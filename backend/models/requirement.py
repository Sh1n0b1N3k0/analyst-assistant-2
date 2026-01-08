"""
Модель требования SRS
"""
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base


class Requirement(Base):
    """
    Модель требования в стандарте SRS
    """
    __tablename__ = "requirements"

    id = Column(Integer, primary_key=True, index=True)
    requirement_id = Column(String, unique=True, index=True, nullable=False)  # Уникальный ID требования
    title = Column(String, nullable=False)  # Название требования
    description = Column(Text, nullable=False)  # Описание требования
    priority = Column(String, nullable=True)  # Приоритет (High, Medium, Low)
    status = Column(String, default="Draft")  # Статус (Draft, Approved, Rejected, etc.)
    category = Column(String, nullable=True)  # Категория требования
    source = Column(String, nullable=True)  # Источник требования
    stakeholder = Column(String, nullable=True)  # Заинтересованное лицо
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Связь с атрибутами требования
    attributes = relationship("RequirementAttribute", back_populates="requirement", cascade="all, delete-orphan")


class RequirementAttribute(Base):
    """
    Модель атрибута требования (для расширяемости)
    """
    __tablename__ = "requirement_attributes"

    id = Column(Integer, primary_key=True, index=True)
    requirement_id = Column(Integer, ForeignKey("requirements.id"), nullable=False)
    attribute_name = Column(String, nullable=False)  # Название атрибута
    attribute_value = Column(Text, nullable=True)  # Значение атрибута
    created_at = Column(DateTime, default=datetime.utcnow)

    # Связь с требованием
    requirement = relationship("Requirement", back_populates="attributes")
