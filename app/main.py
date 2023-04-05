from fastapi import FastAPI
from routes.task_route import router

app = FastAPI()

app.include_router(router)