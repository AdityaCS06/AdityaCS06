import base64
import random
import re

class Validation:
    def blank_field_check(
        username:str,
        email:str,
        phone:str,
        password:str
    ):
        phone_no=str(phone)
        
        if not username.strip():
            return {"message": "Username is invalid"}
        if not email.strip():
            return {"message":"Email is invalid"}
        if not password.strip():
            return {"message": "Password is invalid"}
        if not phone_no.strip():
            return {"message": "Phone is invalid"}
        return True
    
    def email_validate(email):
        email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(email_regex, email)
    
    def phone_validate(phone):
        pho=str(phone)
        phone_regex = r"^\d{10}$" 
        return re.match(phone_regex, pho)




    

class Generator:
    def hash_generator(input_string):
        input_bytes=input_string.encode('utf-8')
        encoded_bytes=base64.b64encode(input_bytes)
        encoded_string= encoded_bytes.decode('utf-8')
        return encoded_string
    
    def hash_convertor(encoded_string):
        decode_bytes=base64.b64decode(encoded_string)
        decode_string=decode_bytes.decode('utf-8')
        return decode_string
    
    def fuid_generator():
        random_integer=str(random.randint(1,10000))
        random_bytes=random_integer.encode('utf-8')
        hashcode=base64.b64encode(random_bytes).decode('utf-8')
        return hashcode