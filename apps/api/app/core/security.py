from datetime import datetime, timedelta, timezone

from jose import JWTError, jwt

from app.core.config import settings


ALGORITHM = "HS256"


def create_access_token(
    user_id: str,
    expires_minutes: int = 60,
) -> str:
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=expires_minutes
    )

    payload = {
        "sub": user_id,
        "exp": expire,
    }

    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=ALGORITHM,
    )


def decode_access_token(token: str) -> dict:
    return jwt.decode(
        token,
        settings.SECRET_KEY,
        algorithms=[ALGORITHM],
    )