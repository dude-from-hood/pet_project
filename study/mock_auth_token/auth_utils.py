import uuid
import time
from datetime import datetime, timedelta

def generate_fake_token(user_id=None):
    """Генерация фейкового Bearer токена"""
    timestamp = int(time.time())
    random_part = uuid.uuid4().hex[:8]
    user_part = user_id or "anonymous"
    return f"fake_{user_part}_{timestamp}_{random_part}"

def generate_expired_token():
    """Генерация просроченного токена"""
    past_time = int((datetime.now() - timedelta(days=1)).timestamp())
    return f"expired_token_{past_time}_{uuid.uuid4().hex[:8]}"
