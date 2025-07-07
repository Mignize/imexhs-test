from sqlalchemy.orm import Session
from . import models, schemas, utils
from fastapi import HTTPException
from fastapi import Depends
from .database import get_db

def get_or_create_device(db: Session, device_name: str):
    device = db.query(models.Device).filter_by(device_name=device_name).first()
    if not device:
        device = models.Device(device_name=device_name)
        db.add(device)
        db.commit()
        db.refresh(device)
    return device

def create_elements(payload: schemas.Payload, db: Session = Depends(get_db)):
    for key, element in payload.root.items():
        avg_before, avg_after, size = utils.validate_and_normalize(element.data)
        device = get_or_create_device(db, element.device_name)

        db_element = models.Element(
            id=element.id,
            device_id=device.id,
            avg_before_norm=avg_before,
            avg_after_norm=avg_after,
            data_size=size
        )
        db.merge(db_element)
    db.commit()

def list_elements(db: Session, filters: dict):
    query = db.query(models.Element).join(models.Device)
    if "created_from" in filters:
        query = query.filter(models.Element.created_date >= filters["created_from"])
    if "avg_before_gt" in filters:
        query = query.filter(models.Element.avg_before_norm > filters["avg_before_gt"])

    elements = query.all()

    return [
    schemas.ElementOut(
        id=el.id,
        device_id=el.device_id,
        device_name=el.device.device_name,
        avg_before_norm=el.avg_before_norm,
        avg_after_norm=el.avg_after_norm,
        data_size=el.data_size,
        created_at=el.created_at,
        updated_at=el.updated_at,
    )
    for el in elements
    ]


def get_element(db: Session, id: str):
    element = db.query(models.Element).filter_by(id=id).join(models.Device).first()

    return schemas.ElementOut(
        id=element.id,
        device_name=element.device.device_name,
        avg_before_norm=element.avg_before_norm,
        avg_after_norm=element.avg_after_norm,
        data_size=element.data_size,
        created_at=element.created_at,
        updated_at=element.updated_at
    ) if element else None

def update_element(db: Session, id: str, update: schemas.UpdateElement):
    element = db.query(models.Element).filter_by(id=id).join(models.Device).first()

    if not element:
        raise HTTPException(status_code=404, detail="Not found")
    if update.device_name:
        device = get_or_create_device(db, update.device_name)
        element.device_id = device.id
    if update.new_id:
        element.id = update.new_id
    db.commit()
    return element

def delete_element(db: Session, id: str):
    element = db.query(models.Element).filter_by(id=id).first()
    if not element:
        raise HTTPException(status_code=404, detail="Not found")
    db.delete(element)
    db.commit()
