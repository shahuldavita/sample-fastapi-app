```python
import bcrypt
from datetime import datetime, timedelta
from jose import JWTError, jwt
from app.config import SECRET_KEY

class AuthService:
    def authenticate_user(self, email: str, password: str) -> bool:
        # Implementation here
        pass

    def create_jwt_token(self, user_id: int) -> str:
        # Implementation here
        pass
```