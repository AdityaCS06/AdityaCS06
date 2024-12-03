from pydantic import BaseModel
from typing import List, Optional


class UserResponseSchema(BaseModel):
    username: Optional[str] = None  
    email: Optional[str] = None           
    phone: Optional[int] = None    
    message: Optional[str] = None