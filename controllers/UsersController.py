from http.client import HTTPException
from uuid import uuid4 as uuid
from models.Users import UserBase
from models.database import engine, tbUsers, pwdContext
from sqlalchemy.orm import Session

class Users:
    def index(payload):
        with Session(engine) as session :
            usersBase = []
            if payload['scope'] == 'admin' :
                users = session.query( tbUsers ).all()
                for user in users :
                    usersBase.append( UserBase.from_orm( user ) )
            return usersBase

    def store(user):
        with Session(engine) as session :
            insert = user.dict()
            hasUser = session.query( tbUsers ).filter( tbUsers.email == insert['email'] ).first()
            if hasUser == None :
                insert['password'] = pwdContext.hash( insert['password'] )
                session.add( tbUsers(**insert, uid = uuid()) )
                session.commit()
                return {"result" : True}
            return {"result" : False}

    def show():
        return {"result" : True}
    
    def update():
        return {"result" : True}

    def destroy():
        return {"result" : True}