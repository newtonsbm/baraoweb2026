from typing import List

from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from ninja import NinjaAPI, Router
from ninja_jwt.authentication import JWTAuth
from ninja_jwt.routers.obtain import obtain_pair_router
from ninja_jwt.routers.verify import verify_router

from app.models import Cesta, Feedback, Perfil
from app.api.schemas import (
    CestaSchema,
    CestaDetailSchema,
    ContatoSchema,
    MessageSchema,
    UserSchema,
    UserRegisterSchema,
    PerfilSchema,
    PerfilUpdateSchema,
)


# ============== API Instance ==============
api = NinjaAPI(
    title="Cafe com Pao API",
    version="1.0.0",
    description="API do projeto Cafe com Pao - Cestas, Contato e Perfil",
)


# ============== Routers ==============
cestas_router = Router(tags=["Cestas"])
contato_router = Router(tags=["Contato"])
auth_router = Router(tags=["Auth"])
perfil_router = Router(tags=["Perfil"], auth=JWTAuth())


@cestas_router.get("/", response=List[CestaSchema])
def cestas_list(request):
    """Listar todas as cestas"""
    return Cesta.objects.all()


@cestas_router.get("/{cesta_id}/", response=CestaDetailSchema)
def cesta_detail(request, cesta_id: int):
    """Detalhe de uma cesta com produtos"""
    cesta = get_object_or_404(Cesta, id=cesta_id)
    return cesta


@contato_router.post("/", response={200: MessageSchema})
def contato_create(request, payload: ContatoSchema):
    """Enviar mensagem de contato (apenas log no console)"""
    # create Feedback object in database
    Feedback.objects.create(
        nome=payload.name,
        email=payload.email,
        telefone=payload.telephone,
        assunto=payload.subject,
        avaliacao=payload.rating,
        mensagem=payload.message
    )
    print(f"[API] Contato de {payload.name} ({payload.email})")
    print(f"[API] Telefone: {payload.telephone}")
    print(f"[API] Assunto: {payload.subject}")
    print(f"[API] Avaliacao: {payload.rating} estrelas")
    print(f"[API] Mensagem: {payload.message}")

    return 200, {
        "message": f"Obrigado por entrar em contato, {payload.name}! Recebemos sua mensagem."
    }


# ============== Auth Endpoints ==============
@auth_router.post("/register", response={201: UserSchema, 400: MessageSchema})
def register(request, payload: UserRegisterSchema):
    """Registrar um novo usuario"""
    if User.objects.filter(username=payload.email).exists():
        return 400, {"message": "Este email ja esta registrado."}

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


# ============== Perfil Endpoints ==============
@perfil_router.get("/", response=PerfilSchema)
def perfil_detail(request):
    """Ver perfil do usuario autenticado"""
    perfil, _ = Perfil.objects.get_or_create(user=request.auth)
    return perfil


# ============== Register Routers ==============
# JWT Token - Routers automaticos do ninja-jwt
# - POST /auth/token/pair -> Fazer login (username + password) e receber tokens
# - POST /auth/token/verify -> Verificar se um token eh valido
# - POST /auth/token/refresh -> Renovar o access token usando refresh token
api.add_router("/auth/token", tags=["Auth"], router=obtain_pair_router)
api.add_router("/auth/token", tags=["Auth"], router=verify_router)

# App routers customizados
api.add_router("/auth", auth_router)
api.add_router("/cestas", cestas_router)
api.add_router("/contato", contato_router)
api.add_router("/perfil", perfil_router)
