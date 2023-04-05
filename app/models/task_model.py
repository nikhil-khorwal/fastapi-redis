from redis_om import HashModel
from utils.config import redis_db

class Task(HashModel):
    name: str
    description: str

    class Meta:
        database: redis_db
