# Домашнее задание по теме "Основы Fast Api и маршрутизация"

from fastapi import FastAPI


app = FastAPI()
# !pip install fastapi uvicorn
# cd modules
# uvicorn module_16_1:app --reload
# or
# uvicorn module_16_1:app --reload --host 0.0.0.0
# uvicorn module_16_1:app --reload --port 8080


@app.get("/")
async def root() -> str:
    return "Главная страница"


@app.get("/user/admin")
async def entrance_call_admin() -> str:
    return "Вы вошли как администратор"


# user/127
# user?username=qw&age=7

@app.get("/user/{user_id}")
async def get_user(user_id: int) -> str:
    return f"Вы вошли как пользователь № {user_id}"


@app.get("/user")
async def get_user_info(username: str = "unknown", age: int = 0) -> str:
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"


