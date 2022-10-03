from sqlalchemy.orm import Session
from models.database import engine, tbDirectory
from controllers.AuthController import AuthController

class Directory:
    def index(uid):
        with Session(engine) as session :
            contacts = session.query( tbDirectory ).filter(tbDirectory.uid_fk == uid).all()
            return [contacts]

    def store(uid, contact, payload):
        with Session(engine) as session :
            insert = contact.dict()
            session.add( tbDirectory(**insert, uid_fk = uid) )
            session.commit()
            token = AuthController.getJWT( payload )
            return {"result" : True, "token" : token}

    def show():
        return {"result" : True}
    
    def update():
        return {"result" : True}

    def destroy(uid, id, payload):
        with Session(engine) as session :
            session.query( tbDirectory ).filter( tbDirectory.id == id, tbDirectory.uid_fk == uid).delete()
            session.commit()
            token = AuthController.getJWT( payload )
            return {"result" : True, "token" : token}