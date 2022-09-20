from datetime import datetime, timedelta

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from . import database, models, schemas
from .config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl = 'login')
# secret key
# Algorithm
# Expriation time

SECREY_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes

def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode,SECREY_KEY,algorithm=ALGORITHM)
    from sqlalchemy.orm import Session

    return encoded_jwt

def verify_access_token(token:str, creadential_exception):
    try:
        payload = jwt.decode(token, SECREY_KEY, algorithms=[ALGORITHM])
        id : str =  payload.get("user_id")

        if id is None:
            raise creadential_exception
        token_data = schemas.TokenData(id=id)
    except JWTError:
        raise creadential_exception
    return token_data

def get_current_user(token:str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)):
    creadential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail = f"could not validate credentials", headers={"WWW-Authenticate": "Bearer"})
    token = verify_access_token(token, creadential_exception) 
    user = db.query(models.User).filter(models.User.id ==token.id).first()

    return user
