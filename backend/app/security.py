import os
from datetime import datetime, timedelta
from typing import Optional

from dotenv import load_dotenv
from fastapi import Request, HTTPException
from jose import JWTError, jwt
from passlib.context import CryptContext

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", "fallback-secret-key-ganti-ini")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
TOKEN_EXPIRE_HOURS = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "480")) // 60 or 8

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_token(username: str) -> str:
    expire = datetime.utcnow() + timedelta(hours=TOKEN_EXPIRE_HOURS)
    return jwt.encode({"sub": username, "exp": expire}, SECRET_KEY, algorithm=ALGORITHM)


def get_current_admin(request: Request) -> Optional[str]:
    token = request.cookies.get("admin_token")
    if not token:
        return None
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("sub")
    except JWTError:
        return None


def require_admin(request: Request) -> str:
    user = get_current_admin(request)
    if not user:
        raise HTTPException(status_code=303, headers={"Location": "/admin/login"})
    return user
