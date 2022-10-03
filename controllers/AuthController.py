import os
from fastapi import status
from fastapi.responses import JSONResponse
from datetime import datetime, timedelta, timezone
from sqlalchemy.orm import Session
from models.database import tbUsers, engine, pwdContext
import jwt

class AuthController:
    def login(auth):
        with Session(engine) as session :
            e = JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST, 
                content={"result" : "Credenciales invalidas"})

            credentials = auth.dict()
            user = session.query( tbUsers ).filter( tbUsers.email == credentials['email'] ).first()
            
            if user == None :
                return e
            
            if pwdContext.verify( credentials['password'], user.password) :
                token = jwt.encode({
                        "scope" : user.role,
                        "uid" : user.uid,
                        "exp": datetime.now(tz=timezone.utc) + timedelta(minutes=1440)
                    }, 
                    str(os.environ.get('SECRET_KEY')), 
                    algorithm='HS256')
                return {"result" : "Authenticación exitosa ", "token" : token, "token_type" : "Bearer"}
            else : 
                return e

    def getJWT( payload ) :
        payload['exp'] = datetime.now(tz=timezone.utc) + timedelta(minutes=1440)
        return jwt.encode( payload, str(os.environ.get('SECRET_KEY')), algorithm='HS256')