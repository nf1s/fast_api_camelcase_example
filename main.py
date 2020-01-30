import uvicorn
from fastapi import FastAPI
from models import User


app = FastAPI()


@app.post("/user/", response_model=User)
async def create_user(user: User):
    return user


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
