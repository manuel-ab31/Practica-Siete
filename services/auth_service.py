# services/auth_service.py
from dataclasses import dataclass

@dataclass(frozen=True)
class AuthResult:
    ok: bool
    message: str = ""
    user_type: str = ""

class AuthService:
    """
    Servicio de autenticación. Hoy: validación estática.
    Mañana: cambiar por BD/API.
    """
    def __init__(self, valid_password: str = "1234"):
        self._password = valid_password
        self._valid_users = {
            "admin": "admin",
            "estudiante": "student",
            "maestro": "teacher"
        }

    def login(self, username: str, password: str) -> AuthResult:
        if not username or not password:
            return AuthResult(False, "Usuario y contraseña son requeridos.", "")
        
        username_lower = username.lower()
        if username_lower in self._valid_users and password == self._password:
            user_type = self._valid_users[username_lower]
            return AuthResult(True, "Autenticación exitosa.", user_type)
        
        return AuthResult(False, "Usuario o contraseña incorrectos.", "")
