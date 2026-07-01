```python
from fastapi import APIRouter, Depends, HTTPException
from app.services.auth_service import AuthService
from app.models.user import User

router = APIRouter()

@router.post('/login')
def login(user: User, auth_service: AuthService = Depends()):
    if not auth_service.authenticate_user(user.email, user.password):
        raise HTTPException(status_code=401, detail='Invalid credentials')
    token = auth_service.create_jwt_token(user.id)
    return {'token': token}
```