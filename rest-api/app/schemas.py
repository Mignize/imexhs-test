from pydantic import BaseModel, RootModel
from typing import List, Optional
from datetime import datetime
from typing import Dict

class ElementData(BaseModel):
    id: str
    data: List[str]
    device_name: str

class Payload(RootModel[Dict[str, ElementData]]):
    pass

class ElementOut(BaseModel):
    id: str
    device_name: str
    avg_before_norm: float
    avg_after_norm: float
    data_size: int
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }

class UpdateElement(BaseModel):
    device_name: Optional[str]
    new_id: Optional[str]
