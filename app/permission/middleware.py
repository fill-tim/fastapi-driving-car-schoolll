from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware
import jwt
from app.main import app

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8080/user/list",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

secret_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InVzZXIiLCJleHAiOjE2MjU0NjQwNzN9.3Y8b4y7l7gYm1xHgXoWZL3Z8fZ1vQn9hRrZ1l0f5GZk"


@app.middleware("http")
async def check_jwt(request: Request, call_next):
    response = await call_next(request)
    # token = request.headers["authorization"].split(" ")[1]
    # data = jwt.encode({"id": token}, secret_key, algorithm="HS256")
    # print(data)
    # data1 = jwt.decode(data, secret_key, algorithms=["HS256"])
    # print(data1)

    return response
