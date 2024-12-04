# import sqlite3
import datetime
from sqlalchemy.orm import Session
from fastapi import Depends
from schema import User
from Model import UserModel
from database import get_db
from dependencies import Validation,Generator
from response_schema import UserResponseSchema


def register_user(
        request: User,
        sql: Session=Depends(get_db)
):

    import datetime
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from schema import User
from Model import UserModel
from database import get_db
from dependencies import Validation, Generator


def register_user(
    request: User,
    sql: Session = Depends(get_db),
): 
    # Check for blank fields
    Validation.blank_field_check(
        request.username, request.email, request.phone, request.password
    )
        # return {"message":"Don't leave fields blank"}
    
    if not Validation.email_validate(request.email):
        return {"message":"Email is invalid"}
    
    if not Validation.phone_validate(request.phone):
        return {"message":"Phone is invalid"}

    # Check if the username already exists
    if sql.query(UserModel).filter(UserModel.username == request.username).first():
        raise HTTPException(status_code=400, detail="User already exists")

    # Check if the email already exists
    if sql.query(UserModel).filter(UserModel.email == request.email).first():
        raise HTTPException(status_code=400, detail="Email already exists")

    # Create new user instance
    new_user = UserModel(
        username=request.username,
        first_name=request.first_name,
        last_name=request.last_name,
        email=request.email,
        password=Generator.hash_generator(request.password),
        phone=request.phone,
        fuid=Generator.fuid_generator(),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now(),
    )

    # Save to database
    sql.add(new_user)
    sql.commit()
    sql.refresh(new_user)

    return {
        "username":new_user.username,
        "email":new_user.email,
        "phone":new_user.phone,
        "message":"User successfully created."
    }