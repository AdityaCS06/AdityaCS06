from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
import controller
from schema import User
from database import get_db
# from Model import UserModel
from response_schema import UserResponseSchema


app=FastAPI()

@app.post(
        "/register",
        response_model=UserResponseSchema
)
def register_user(
        request: User,
        sql: Session=Depends(get_db)
):
    return controller.register_user(request,sql)
