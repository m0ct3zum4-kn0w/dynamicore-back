import os, jwt
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi.middleware.cors import CORSMiddleware
from routes.api import Api
from starlette.responses import RedirectResponse

origins = [
    "http://localhost:3000",
    "https://dynamic-front.herokuapp.com"
]

security = HTTPBearer()

async def bearer_access(credentials: HTTPAuthorizationCredentials = Depends(security)):
    bearer_token = credentials.credentials
    try:
        return jwt.decode(bearer_token, str("{}".format(os.environ.get('SECRET_KEY'))), algorithms="HS256")
    except jwt.ExpiredSignatureError as e:
        raise HTTPException(
            status_code=401,
            detail=str(e))

# jwt_payload = jwt.encode(
#     {"exp": datetime.datetime.now(tz=timezone.utc) + datetime.timedelta(seconds=30)},
#     "secret",
# )

# time.sleep(32)

# # JWT payload is now expired
# # But with some leeway, it will still validate
# jwt.decode(jwt_payload, "secret", leeway=10, algorithms=["HS256"])

app = FastAPI(
        title = "Dynamicore Test", 
        version = "0.2", 
        description = "Prueba para vacante desarrollador FullStack",
        openapi_tags = [{
            "name" : "Usuarios",
            "description" : "Endpoints para usuarios"
        },{
            "name" : "Directorio",
            "description" : "Endpoins para los directorios de cada usuario"
        }]
    )

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/",include_in_schema=False)
async def main():
    return RedirectResponse(url="/docs")

Api( app, bearer_access)