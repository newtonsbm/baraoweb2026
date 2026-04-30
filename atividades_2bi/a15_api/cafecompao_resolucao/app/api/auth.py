from ninja import Router
from django.contrib.auth.models import User

from app.models import Perfil
from app.api.schemas import UserRegisterSchema, UserSchema, MessageSchema

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
