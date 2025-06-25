import os
from redis import Redis
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Read the environment variable USE_REDIS
USE_REDIS = os.getenv('USE_REDIS', 'False').lower() == 'true'

# Get Redis uri configuration from environment variables
REDIS_URI = os.getenv('REDIS_URI', 'rediss://default:AlgjAAIgcDHaXFFIC61XFs1CTIT61sjoHUFG20svV-MI34ilSGMu-Q@divine-rodent-22563.upstash.io:6379')

# Conditionally initialize Redis client
if USE_REDIS:
    redisClient = Redis.from_url(REDIS_URI)
else:
    redisClient = None