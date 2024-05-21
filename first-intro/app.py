from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def main():
    return {
        "message": "it's running"
    }

@app.get("/login/")
def login(email: str, password: str):
    return {
        "message": "it's running"
    }

@app.get("/admin")
def admin():
    return {
        "message": "it's running"
    }