from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal, engine, Base
from . import schemas, crud, logger

app = FastAPI()
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/api/elements/")
def create_elements(payload: schemas.Payload, db: Session = Depends(get_db)):
    try:
        crud.create_elements(payload, db)
        return {"message": "Elements saved"}
    except Exception as e:
        logger.logger.error(str(e))
        raise HTTPException(status_code=400, detail="Invalid payload")

@app.get("/api/elements/", response_model=list[schemas.ElementOut])
def list_elements(db: Session = Depends(get_db), avg_before_gt: float = None):
    filters = {"avg_before_gt": avg_before_gt} if avg_before_gt else {}
    return crud.list_elements(db, filters)

@app.get("/api/elements/{id}", response_model=schemas.ElementOut)
def get_element(id: str, db: Session = Depends(get_db)):
    element = crud.get_element(db, id)
    if not element:
        raise HTTPException(status_code=404, detail="Not found")
    return element

@app.put("/api/elements/{id}")
def update_element(id: str, update: schemas.UpdateElement, db: Session = Depends(get_db)):
    return crud.update_element(db, id, update)

@app.delete("/api/elements/{id}")
def delete_element(id: str, db: Session = Depends(get_db)):
    crud.delete_element(db, id)
    return {"message": "Deleted"}
