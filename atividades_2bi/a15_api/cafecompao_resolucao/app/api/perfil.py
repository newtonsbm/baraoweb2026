from ninja import Router
from ninja_jwt.authentication import JWTAuth

from app.models import Perfil
from app.api.schemas import PerfilSchema, PerfilUpdateSchema

router = Router(tags=["Perfil"], auth=JWTAuth())


@router.get("/", response=PerfilSchema)
def perfil_detail(request):
    """Ver perfil do usuário autenticado"""
    perfil, _ = Perfil.objects.get_or_create(user=request.auth)
    return perfil


@router.put("/", response=PerfilSchema)
def perfil_update(request, payload: PerfilUpdateSchema):
    """Atualizar perfil do usuário autenticado"""
    perfil, _ = Perfil.objects.get_or_create(user=request.auth)

    for attr, value in payload.dict(exclude_unset=True).items():
        setattr(perfil, attr, value)

    perfil.save()
    return perfil
