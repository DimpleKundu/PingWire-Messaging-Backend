from fastapi import FastAPI, APIRouter
from database import user_collection
from auth import router as auth_router
from chat import websocket_endpoint

app = FastAPI()
router = APIRouter()
# include the router from other files
app.include_router(auth_router)
from chat import router as chat_router
app.include_router(chat_router)

@app.get("/")
def read_root():
    return {"msg": "pingwire backend is up!"}

# @app.get("/test-db")
# def test_db():
#     return {"users_count": user_collection.count_documents({})}

# @app.get("/test-insert")
# def test_insert():
#     user_collection.insert_one({"username": "Dimple", "password": "1234"})
#     return {"msg": "Inserted"}

