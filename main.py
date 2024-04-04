from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None


class STask(STaskAdd):
    id: int


tasks = []


@app.post('/tasks')
async def add_task(
        task: STaskAdd,
):
    tasks.append(task)
    return {'ok': True}


# @app.get('/tasks')
# def get_tasks():
#     task = Task(name='Запиши это видео')
#     return {'data': task}
