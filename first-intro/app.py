from typing import Union
import uuid
from fastapi import FastAPI

app = FastAPI()

valid_users = dict()
valid_profiles = dict()
pending_users = dict()
discussion_posts = dict()
request_headers = dict()
cookies = dict()

@app.get("/")
def main():
    return {
        "message": "it's running"
    }

@app.get("/login/")
def login(email: str, password: str):
    if email == None or password == None:
        return {
            "message": "Invalid login details"
        }
    if email == "" or password == "":
        return {
            "message": "Invalid login details"
        }
    if email and password:
        return {
            "email": email,
            "password": password
        }
    
    return {
        "message": "it's running",
        "email": email,
        "password": password
    }

@app.get("/admin")
def admin():
    return {
        "message": "it's running"
    }

@app.get("/items/{item_id}")
def read_item(item_id: uuid.UUID, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/products/{item_id}")
def read_item_int(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}