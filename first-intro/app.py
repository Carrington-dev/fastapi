from typing import Union
import uuid
from fastapi import FastAPI

from enum import Enum
from typing import Optional, List, Dict
from uuid import UUID, uuid1

from fastapi import FastAPI, Form, Cookie, Header, Response
from pydantic import BaseModel

from bcrypt import hashpw, gensalt, checkpw
from datetime import date, datetime

from string import ascii_lowercase
from random import random


app = FastAPI()

valid_users = dict()
valid_profiles = dict()
pending_users = dict()
discussion_posts = dict()
request_headers = dict()
cookies = dict()


class User(BaseModel):
    username: str
    password: str

class ValidUser(BaseModel):
    id: UUID
    username: str
    password: str
    passphrase: str

class UserType(str, Enum):
    admin = "admin"
    teacher = "teacher"
    alumni = "alumni"
    student = "student"
    
class UserProfile(BaseModel):
    firstname: str
    lastname: str
    middle_initial: str
    age: Optional[int] = 0
    salary: Optional[int] = 0
    birthday: date
    user_type: UserType
  
class PostType(str, Enum):
    information = "information" 
    inquiry = "inquiry"
    quote = "quote"
    twit = "twit"
    
class Post(BaseModel):
    topic: Optional[str] = None
    message: str
    date_posted: datetime
    
class ForumPost(BaseModel):
    id: UUID
    topic: Optional[str] = None
    message: str
    post_type: PostType
    date_posted: datetime
    username: str

class ForumDiscussion(BaseModel):
    id: UUID
    main_post: ForumPost
    replies: Optional[List[ForumPost]] = None
    author: UserProfile

@app.get("/")
def main():
    return { "message": "it's running" }

@app.get("/login/")
def login(email: str, password: str):
    if email == None or password == None:
        return { "message": "Invalid login details" }
    if email == "" or password == "":
        return { "message": "Invalid login details" }
    if email and password:
        return { "email": email, "password": password }
    return {"message": "it's running",}

@app.get("/ch01/login/")
def signin(username: str, password: str):
    if valid_users.get(username) == None:
        return {"message": "user does not exist"}
    else:
        user = valid_users.get(username)
        if checkpw(password.encode(), user.passphrase.encode()):
            return user
        else:
            return {"message": "invalid user"}
        
@app.post("/ch01/login/signup")
def signup(uname: str, passwd: str):
    if (uname == None and passwd == None):
        return {"message": "invalid user"}
    elif not valid_users.get(uname) == None:
        return {"message": "user exists"}
    else:
        user = User(username=uname, password=passwd)
        pending_users[uname] = user
        return user

@app.get("/admin")
def admin():
    return { "message": "it's running" }

@app.get("/items/{item_id}")
def read_item(item_id: uuid.UUID, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/products/{product_id}")
def read_item_int(product_id: int, q: Union[str, None] = None):
    return {"product_id": product_id, "q": q}

@app.put("/ch01/account/profile/update/{username}")
def update_profile(username: str, id: UUID, 
    new_profile: UserProfile):
    if valid_users.get(username) == None:
        return {"message": "user does not exist"}
    else:
        user = valid_users.get(username)
        if user.id == id:
            valid_profiles[username] = new_profile
            return {"message": "successfully updated"}
        else:
            return {"message": "user does not exist"}
        
@app.patch("/ch01/account/profile/update/names/{username}")
def update_profile_names(username: str, id: UUID, 
    new_names: Dict[str, str]):
    if valid_users.get(username) == None:
        return {"message": "user does not exist"}
    elif new_names == None:
        return {"message": "new names are required"}
    else:
        user = valid_users.get(username)
        if user.id == id:
            profile = valid_profiles[username]
            profile.firstname = new_names['fname']
            profile.lastname = new_names['lname']
            profile.middle_initial = new_names['mi']
            valid_profiles[username] = profile
            return {"message": "successfully updated"}
        else:
            return {"message": "user does not exist"}

@app.delete("/ch01/discussion/posts/remove/{username}")
def delete_discussion(username: str, id: UUID):
    if valid_users.get(username) == None:
        return {"message": "user does not exist"}
    elif discussion_posts.get(id) == None:
        return {"message": "post does not exist"}
    else:
        del discussion_posts[id] 
        return {"message": "main post deleted"}


@app.delete("/ch01/login/remove/{username}")
def delete_user(username: str):
    if username == None:
        return {"message": "invalid user"}
    else:
        del valid_users[username]
        return {"message": "deleted user"}
