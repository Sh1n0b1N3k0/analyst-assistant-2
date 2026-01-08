"""
Роутер для импорта требований
"""
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from typing import List
import json
import csv
from io import StringIO

from database import get_db
from models.requirement import Requirement, RequirementAttribute
from schemas.requirement import RequirementCreate, RequirementResponse

router = APIRouter()


@router.post("/json", response_model=List[RequirementResponse])
async def import_from_json(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    """
    Импорт требований из JSON файла
    """
    try:
        content = await file.read()
        data = json.loads(content.decode("utf-8"))
        
        # Ожидаем список требований
        if not isinstance(data, list):
            data = [data]
        
        imported_requirements = []
        
        for req_data in data:
            # Проверяем, существует ли уже требование с таким ID
            existing = db.query(Requirement).filter(
                Requirement.requirement_id == req_data.get("requirement_id")
            ).first()
            
            if existing:
                raise HTTPException(
                    status_code=400,
                    detail=f"Требование с ID {req_data.get('requirement_id')} уже существует"
                )
            
            # Создаем требование
            requirement = Requirement(
                requirement_id=req_data.get("requirement_id"),
                title=req_data.get("title"),
                description=req_data.get("description"),
                priority=req_data.get("priority"),
                status=req_data.get("status", "Draft"),
                category=req_data.get("category"),
                source=req_data.get("source"),
                stakeholder=req_data.get("stakeholder")
            )
            
            db.add(requirement)
            db.flush()  # Получаем ID требования
            
            # Добавляем атрибуты, если они есть
            attributes = req_data.get("attributes", [])
            for attr_data in attributes:
                attribute = RequirementAttribute(
                    requirement_id=requirement.id,
                    attribute_name=attr_data.get("attribute_name"),
                    attribute_value=attr_data.get("attribute_value")
                )
                db.add(attribute)
            
            imported_requirements.append(requirement)
        
        db.commit()
        
        # Возвращаем созданные требования
        result = []
        for req in imported_requirements:
            db.refresh(req)
            result.append(req)
        
        return result
        
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Неверный формат JSON")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/csv", response_model=List[RequirementResponse])
async def import_from_csv(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    """
    Импорт требований из CSV файла
    """
    try:
        content = await file.read()
        csv_content = content.decode("utf-8")
        csv_reader = csv.DictReader(StringIO(csv_content))
        
        imported_requirements = []
        
        for row in csv_reader:
            requirement_id = row.get("requirement_id") or row.get("ID")
            if not requirement_id:
                continue  # Пропускаем строки без ID
            
            # Проверяем, существует ли уже требование
            existing = db.query(Requirement).filter(
                Requirement.requirement_id == requirement_id
            ).first()
            
            if existing:
                continue  # Пропускаем существующие требования
            
            # Создаем требование
            requirement = Requirement(
                requirement_id=requirement_id,
                title=row.get("title", ""),
                description=row.get("description", ""),
                priority=row.get("priority"),
                status=row.get("status", "Draft"),
                category=row.get("category"),
                source=row.get("source"),
                stakeholder=row.get("stakeholder")
            )
            
            db.add(requirement)
            imported_requirements.append(requirement)
        
        db.commit()
        
        # Обновляем объекты из БД
        for req in imported_requirements:
            db.refresh(req)
        
        return imported_requirements
        
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/manual", response_model=RequirementResponse)
async def import_manual(
    requirement: RequirementCreate,
    db: Session = Depends(get_db)
):
    """
    Ручной импорт одного требования через API
    """
    # Проверяем, существует ли уже требование с таким ID
    existing = db.query(Requirement).filter(
        Requirement.requirement_id == requirement.requirement_id
    ).first()
    
    if existing:
        raise HTTPException(
            status_code=400,
            detail=f"Требование с ID {requirement.requirement_id} уже существует"
        )
    
    # Создаем требование
    db_requirement = Requirement(
        requirement_id=requirement.requirement_id,
        title=requirement.title,
        description=requirement.description,
        priority=requirement.priority,
        status=requirement.status,
        category=requirement.category,
        source=requirement.source,
        stakeholder=requirement.stakeholder
    )
    
    db.add(db_requirement)
    db.flush()
    
    # Добавляем атрибуты
    for attr_data in requirement.attributes or []:
        attribute = RequirementAttribute(
            requirement_id=db_requirement.id,
            attribute_name=attr_data.attribute_name,
            attribute_value=attr_data.attribute_value
        )
        db.add(attribute)
    
    db.commit()
    db.refresh(db_requirement)
    
    return db_requirement
