import os
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine
from passlib.context import CryptContext

pwdContext = CryptContext(schemes=["bcrypt"], deprecated="auto")

Base = automap_base()

engine = create_engine("mysql+pymysql://{}:{}@{}:{}/{}".format(
    os.environ.get('MYSQL_USER'),
    os.environ.get('MYSQL_PASS'),
    os.environ.get('MYSQL_HOST'),
    os.environ.get('MYSQL_PORT'),
    os.environ.get('MYSQL_DB')
))

Base.prepare(engine, reflect = True)

tbUsers = Base.classes.usuarios
tbDirectory = Base.classes.contactos