from ninja import Router
from django.contrib.auth.models import User
from ninja_jwt.authentication import JWTAuth
from ninja_jwt.tokens import RefreshToken

from app.models import Perfil
from app.api.schemas import UserRegisterSchema, UserSchema, MessageSchema, LogoutSchema

router = Router(tags=["Auth"])


@router.post("/register", response={201: UserSchema, 400: MessageSchema})
def register(request, payload: UserRegisterSchema):
    """Registrar um novo usuário"""
    if User.objects.filter(username=payload.email).exists():
        return 400, {"message": "Este email já está registrado."}

    user = User.objects.create_user(
        username=payload.email,
        email=payload.email,
        password=payload.password,
        first_name=payload.first_name,
        last_name=payload.last_name,
    )

    # Cria perfil automaticamente
    Perfil.objects.get_or_create(user=user)

    return 201, user


@router.post("/logout", response={200: MessageSchema, 400: MessageSchema}, auth=JWTAuth())
def logout(request, payload: LogoutSchema):
    """
    Fazer logout invalidando o refresh token.
    
    Para invalidar o token, é necessário enviar o refresh token no body.
    O access token será automaticamente invalidado quando o refresh token
    for colocado na blacklist.
    
    Body:
    {
        "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
    }
    """
    try:
        # Criar objeto RefreshToken e colocá-lo na blacklist
        token = RefreshToken(payload.refresh)
        token.blacklist()
        
        return 200, {"message": "Logout realizado com sucesso. Token invalidado."}
    except Exception as e:
        return 400, {"message": f"Erro ao fazer logout: {str(e)}"}
