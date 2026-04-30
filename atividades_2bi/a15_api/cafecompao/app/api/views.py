from typing import List

from django.shortcuts import get_object_or_404
from ninja import NinjaAPI, Router

from app.models import Cesta, Feedback
from app.api.schemas import (
    CestaSchema,
    CestaDetailSchema,
    ContatoSchema,
    MessageSchema,
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


api.add_router("/cestas", cestas_router)
api.add_router("/contato", contato_router)
