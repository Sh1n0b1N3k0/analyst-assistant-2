"""
Pydantic схемы для валидации данных требований
"""
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class RequirementAttributeCreate(BaseModel):
    """Схема для создания атрибута требования"""
    attribute_name: str = Field(..., description="Название атрибута")
    attribute_value: Optional[str] = Field(None, description="Значение атрибута")


class RequirementAttributeResponse(BaseModel):
    """Схема для ответа с атрибутом требования"""
    id: int
    requirement_id: int
    attribute_name: str
    attribute_value: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True


class RequirementCreate(BaseModel):
    """Схема для создания требования"""
    requirement_id: str = Field(..., description="Уникальный ID требования")
    title: str = Field(..., description="Название требования")
    description: str = Field(..., description="Описание требования")
    priority: Optional[str] = Field(None, description="Приоритет")
    status: Optional[str] = Field("Draft", description="Статус")
    category: Optional[str] = Field(None, description="Категория")
    source: Optional[str] = Field(None, description="Источник")
    stakeholder: Optional[str] = Field(None, description="Заинтересованное лицо")
    attributes: Optional[List[RequirementAttributeCreate]] = Field(default=[], description="Атрибуты требования")


class RequirementUpdate(BaseModel):
    """Схема для обновления требования"""
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None
    status: Optional[str] = None
    category: Optional[str] = None
    source: Optional[str] = None
    stakeholder: Optional[str] = None


class RequirementResponse(BaseModel):
    """Схема для ответа с требованием"""
    id: int
    requirement_id: str
    title: str
    description: str
    priority: Optional[str]
    status: str
    category: Optional[str]
    source: Optional[str]
    stakeholder: Optional[str]
    created_at: datetime
    updated_at: datetime
    attributes: List[RequirementAttributeResponse] = []

    class Config:
        from_attributes = True
