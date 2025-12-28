from fastapi import FastAPI, HTTPException
from common.bindings.app.services.user_service import UserService

"""
main.py отвечает за маршрутизацию и обработку HTTP-запросов
"""

app = FastAPI()
user_service = UserService()

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    try:
        # 1. Получаем данные из внешнего API
        raw_user_data = user_service.get_user_from_external_api(user_id)

        # 2. Обрабатываем данные
        processed_data = user_service.process_user_data(raw_user_data)

        return {
            "status": "success",
            "data": processed_data
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))