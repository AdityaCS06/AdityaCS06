from pydantic import BaseModel
from typing import List, Optional


class UserResponseSchema(BaseModel):
    username: Optional[List[str]] = None  # Optional field with default value None
    email: Optional[str] = None           # Optional field with default value None
    phone: Optional[int] = None    
