from passlib.context import CryptContext
from backend.database import SessionLocal
from backend.models import User  # or wherever your User model is

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
hashed_password = pwd_context.hash("test123")

db = SessionLocal()
user = User(username="samuel", email="samuel@example.com", hashed_password=hashed_password, is_admin=True)
db.add(user)
db.commit()
db.close()
