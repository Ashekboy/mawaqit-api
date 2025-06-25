import os
from redis import Redis
from dotenv import load_dotenv

load_dotenv()

USE_REDIS = os.getenv('USE_REDIS', 'False').lower() == 'true'
REDIS_URI = os.getenv('REDIS_URI')  # Remove hardcoded URI

if USE_REDIS:
    redisClient = Redis.from_url(
        REDIS_URI,
        ssl=True,
        decode_responses=True,
        socket_timeout=5,
        socket_connect_timeout=5,
        retry_on_timeout=True,
        max_connections=10
    )
else:
    redisClient = None