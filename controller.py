# import sqlite3
import datetime
from sqlalchemy.orm import Session
from fastapi import Depends
from schema import User
from Model import UserModel
from database import get_db
from dependencies import Validation,Generator


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
    if not Validation.blank_field_check(
        request.username, request.email, request.phone, request.password
    ):
        return {"message":"Don't leave fields blank"}
    
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

    return {"message": "User registered successfully", "user": new_user}



"""

# from sqlalchemy.orm import Session
# from fastapi import Depends, HTTPException
# from passlib.hash import bcrypt
# from models import User  # Ensure User is imported from models, not schema
# from database import get_db


def register_user(
    request: User,  # Pydantic schema for input validation
    db: Session = Depends(get_db),
):
    try:
        # Check if user already exists
        existing_user = db.query(User).filter(User.username == request.username).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Username already taken")

        # Create a new user instance
        hashed_password = bcrypt.hash(request.password)
        new_user = User(
            username=request.username,
            name=request.name,
            age=request.age,
            email=request.email,
            password=hashed_password,
        )

        # Add and commit the user to the database
        db.add(new_user)
        db.commit()
        db.refresh(new_user)  # Get the latest data from the database

        return {"message": "User registered successfully", "user": new_user.username}
    except HTTPException as http_err:
        raise http_err
    except Exception as e:
        # Log the error (e.g., using logging module)
        return {"error": str(e)}

        # """