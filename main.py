import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel


class User(BaseModel):
    first_name: str
    last_name: str = None
    age: float


app = FastAPI()


@app.post("/user/")
async def create_user(user: User):
    return user


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
