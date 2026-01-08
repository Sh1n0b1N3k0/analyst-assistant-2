"""
Роутер для экспорта требований
"""
from fastapi import APIRouter, Depends, Query, HTTPException
from fastapi.responses import StreamingResponse, JSONResponse
from sqlalchemy.orm import Session
from typing import List, Optional
import json
import csv
from io import StringIO

from database import get_db
from models.requirement import Requirement
from schemas.requirement import RequirementResponse

router = APIRouter()


@router.get("/json", response_model=List[RequirementResponse])
async def export_to_json(
    category: Optional[str] = Query(None, description="Фильтр по категории"),
    status: Optional[str] = Query(None, description="Фильтр по статусу"),
    priority: Optional[str] = Query(None, description="Фильтр по приоритету"),
    db: Session = Depends(get_db)
):
    """
    Экспорт требований в JSON формате
    """
    query = db.query(Requirement)
    
    # Применяем фильтры
    if category:
        query = query.filter(Requirement.category == category)
    if status:
        query = query.filter(Requirement.status == status)
    if priority:
        query = query.filter(Requirement.priority == priority)
    
    requirements = query.all()
    return requirements


@router.get("/json/file")
async def export_to_json_file(
    category: Optional[str] = Query(None, description="Фильтр по категории"),
    status: Optional[str] = Query(None, description="Фильтр по статусу"),
    priority: Optional[str] = Query(None, description="Фильтр по приоритету"),
    db: Session = Depends(get_db)
):
    """
    Экспорт требований в JSON файл для скачивания
    """
    query = db.query(Requirement)
    
    # Применяем фильтры
    if category:
        query = query.filter(Requirement.category == category)
    if status:
        query = query.filter(Requirement.status == status)
    if priority:
        query = query.filter(Requirement.priority == priority)
    
    requirements = query.all()
    
    # Преобразуем в JSON
    requirements_data = []
    for req in requirements:
        req_dict = {
            "requirement_id": req.requirement_id,
            "title": req.title,
            "description": req.description,
            "priority": req.priority,
            "status": req.status,
            "category": req.category,
            "source": req.source,
            "stakeholder": req.stakeholder,
            "created_at": req.created_at.isoformat(),
            "updated_at": req.updated_at.isoformat(),
            "attributes": [
                {
                    "attribute_name": attr.attribute_name,
                    "attribute_value": attr.attribute_value
                }
                for attr in req.attributes
            ]
        }
        requirements_data.append(req_dict)
    
    json_content = json.dumps(requirements_data, ensure_ascii=False, indent=2)
    
    return StreamingResponse(
        iter([json_content]),
        media_type="application/json",
        headers={"Content-Disposition": "attachment; filename=requirements.json"}
    )


@router.get("/csv/file")
async def export_to_csv_file(
    category: Optional[str] = Query(None, description="Фильтр по категории"),
    status: Optional[str] = Query(None, description="Фильтр по статусу"),
    priority: Optional[str] = Query(None, description="Фильтр по приоритету"),
    db: Session = Depends(get_db)
):
    """
    Экспорт требований в CSV файл для скачивания
    """
    query = db.query(Requirement)
    
    # Применяем фильтры
    if category:
        query = query.filter(Requirement.category == category)
    if status:
        query = query.filter(Requirement.status == status)
    if priority:
        query = query.filter(Requirement.priority == priority)
    
    requirements = query.all()
    
    # Создаем CSV
    output = StringIO()
    fieldnames = [
        "requirement_id", "title", "description", "priority", 
        "status", "category", "source", "stakeholder",
        "created_at", "updated_at"
    ]
    
    writer = csv.DictWriter(output, fieldnames=fieldnames)
    writer.writeheader()
    
    for req in requirements:
        writer.writerow({
            "requirement_id": req.requirement_id,
            "title": req.title,
            "description": req.description,
            "priority": req.priority or "",
            "status": req.status,
            "category": req.category or "",
            "source": req.source or "",
            "stakeholder": req.stakeholder or "",
            "created_at": req.created_at.isoformat(),
            "updated_at": req.updated_at.isoformat()
        })
    
    csv_content = output.getvalue()
    output.close()
    
    return StreamingResponse(
        iter([csv_content]),
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=requirements.csv"}
    )


@router.get("/filters")
async def get_export_filters(db: Session = Depends(get_db)):
    """
    Получить доступные значения для фильтров экспорта
    """
    categories = db.query(Requirement.category).distinct().all()
    statuses = db.query(Requirement.status).distinct().all()
    priorities = db.query(Requirement.priority).distinct().all()
    
    return {
        "categories": [cat[0] for cat in categories if cat[0]],
        "statuses": [stat[0] for stat in statuses if stat[0]],
        "priorities": [pri[0] for pri in priorities if pri[0]]
    }
