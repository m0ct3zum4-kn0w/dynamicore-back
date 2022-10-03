from typing import Dict, List
from fastapi import Depends
from pydantic import Json
from controllers.UsersController import Users
from controllers.DirectoryController import Directory
from controllers.AuthController import AuthController
from models.Users import UserBase, newUser
from models.Auth import loginModel
from models.Contacts import ContactBase

class Api:
    def __init__(self, app, bearer_access):
        @app.get("/api/v1/usuarios", 
            tags=["Usuarios"],
            response_model = List[UserBase],
            dependencies = [Depends(bearer_access)])  
        def listUsuarios(payload = Depends(bearer_access)) : return Users.index(payload)

        @app.get("/api/v1/usuarios/{uid}", tags=["Usuarios"])
        def getUsuario(uid : str):
            return {"result" : True}

        @app.post("/api/v1/usuarios", 
            tags = ["Usuarios"], 
            response_model = Dict)
        def setUsuario(user : newUser): return Users.store(user)

        @app.put("/api/v1/usuarios/{uid}", tags=["Usuarios"])
        def updateUsuario(uid : str):
            return {"result" : True}

        @app.delete("/api/v1/usuarios/{uid}", tags=["Usuarios"])
        def dropUsuario(uid : str):
            return {"result" : True}

        @app.get('/api/v1/usuarios/{uid}/directorio', 
            tags=["Directorio"],
            # response_model=List[ContactBase],
            dependencies = [Depends(bearer_access)])
        def listDirectorio(uid : str): return Directory.index(uid)

        @app.get('/api/v1/usuarios/{uid}/directorio/{name_contact}', tags=["Directorio"])
        def getDirectorio(uid : str, name_contact : str):
            return {"result" : uid}

        @app.post('/api/v1/usuarios/{uid}/directorio', 
            tags=["Directorio"], 
            response_model=Dict,
            dependencies = [Depends(bearer_access)])
        def setDirectorio(uid, contact : ContactBase, payload = Depends(bearer_access)): return Directory.store(uid, contact, payload)
        
        @app.put('/api/v1/usuarios/{uid}/directorio/{directory_id}', tags=["Directorio"])
        def updateDirectorio(uid : str, directory : str):
            return {"result" : True}

        @app.delete('/api/v1/usuarios/{uid}/directorio/{directory_id}', 
            tags=["Directorio"],
            dependencies = [Depends(bearer_access)])
        def dropDirectorio(uid : str, directory_id : int, payload = Depends(bearer_access)): return Directory.destroy(uid, directory_id, payload)

        @app.post('/api/v1/login')
        def login(auth : loginModel): return AuthController.login(auth)