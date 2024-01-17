from redis.asyncio import Redis
from fastapi import APIRouter
from app.db.init_redis import get_redis_connection
from app.config import settings


router = APIRouter()
