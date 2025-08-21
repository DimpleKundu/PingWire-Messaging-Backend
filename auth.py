import os
from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from models import User
from database import user_collection

router = APIRouter()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 100


# 🔒 Password hashing
# 📩 Token creation
# 🔐 Register & Login routes


# 🔧 Add Password Utilities
pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


# 🔐 Token Generator
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.now() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm = ALGORITHM)

# REGISTER ROUTE
@router.post("/register")
def register(user: User):
    if user_collection.find_one({"username": user.username}):
        raise HTTPException(status_code=400, detail="User already exists")
    
    hashed_pw = hash_password(user.password)
    user_collection.insert_one({"username": user.username, "password": hashed_pw})

    return{"msg": "User registered successfully"}


# 🔐 Login Route with JWT
@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    db_user = user_collection.find_one({"username": form_data.username})
    if not db_user or not verify_password(form_data.password, db_user["password"]):
        raise HTTPException(status_code=401, detail= "Invalid Crendentials")
    
    access_token = create_access_token(data={"sub": form_data.username})
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
# #  Note: OAuth2PasswordRequestForm expects form data like:

# username=dimple
# password=123

# NEXT: protect routes using JWT 💂‍♀️ — so only users with a valid token can access them.

outh2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(outh2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        user = user_collection.find_one({"username": username})
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except JWTError:
        raise HTTPException(status_code=401, detail= "Invalid or expired token" )

#  add this directly to auth.py for now to test:
@router.get("/protected")
def protected_route(current_user: dict = Depends(get_current_user)):
    return {"msg": f"Hello, {current_user['username']}! This route is protected."}
