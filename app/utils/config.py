from redis_om import get_redis_connection
import os

redis_db = get_redis_connection(
    host=os.getenv("REDIS_HOST","localhost"),
    port=os.getenv("REDIS_PORT","6379")
)