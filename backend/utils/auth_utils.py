from datetime import datetime, timedelta
from typing import Optional, Dict



from fastapi import Depends, HTTPException, status

from jose import JWTError, jwt
from passlib.context import CryptContext
import os

# ------------------------------------------------
# CONFIGURATION
# ------------------------------------------------

# Secret key — in production, use environment variable
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")  # 🔐 Use a secure method in prod
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

# Toggle for dev vs prod mode (use plain text passwords in dev)
USE_HASHING = False  # Set to True when ready for production

# ------------------------------------------------
# PASSWORD UTILS
# ------------------------------------------------

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    """
    Hashes the given password using bcrypt (if hashing is enabled).
    """
    return pwd_context.hash(password) if USE_HASHING else password

def require_admin(current_user: User = Depends(get_current_user)):
    if not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required"
        )
    return current_user


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifies a plain password against a hashed password or compares directly if hashing is disabled.
    """
    if USE_HASHING:
        return pwd_context.verify(plain_password, hashed_password)
    return plain_password == hashed_password

# ------------------------------------------------
# JWT TOKEN CREATION
# ------------------------------------------------

def create_access_token(data: Dict[str, str], expires_delta: Optional[timedelta] = None) -> str:
    """
    Creates a JWT token containing the given data and expiration time.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> models.User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = db.query(models.User).filter(models.User.email == email).first()
    if user is None:
        raise credentials_exception
    return user
