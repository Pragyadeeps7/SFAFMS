"""
API dependencies for authentication and database access
"""
from fastapi import Depends, HTTPException, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.db.session import AsyncSessionLocal
from app.core.security import SecurityUtils
from app.core.exceptions import AuthenticationException
from sqlalchemy.ext.asyncio import AsyncSession

security = HTTPBearer()

async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session

async def get_current_user(
    request: Request,
    credentials: HTTPAuthorizationCredentials = Depends(security)
) -> dict:
    try:
        payload = SecurityUtils.decode_token(credentials.credentials, token_type="access")
        user_id: str = payload.get("sub")
        role: str = payload.get("role")
        if user_id is None:
            raise AuthenticationException("Invalid token")
        return {
            "user_id": user_id,
            "email": payload.get("email"),
            "role": role
        }
    except Exception as e:
        raise AuthenticationException(str(e))

def require_roles(*allowed_roles: str):
    async def role_checker(current_user: dict = Depends(get_current_user)) -> dict:
        if current_user["role"] not in allowed_roles:
            raise HTTPException(status_code=403, detail="Insufficient permissions")
        return current_user
    return role_checker
