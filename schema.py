from pydantic import BaseModel

class User(BaseModel):
    username : str
    first_name : str
    last_name : str
    email : str
    password : str
    phone : int


class LoginUser(BaseModel):
    username : str
    password : str