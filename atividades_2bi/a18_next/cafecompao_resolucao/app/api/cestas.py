from ninja import Router
from django.shortcuts import get_object_or_404
from typing import List

from app.models import Cesta
from app.api.schemas import CestaSchema, CestaDetailSchema

router = Router(tags=["Cestas"])


@router.get("/", response=List[CestaSchema])
def cestas_list(request):
    """Listar todas as cestas"""
    return Cesta.objects.all()


@router.get("/{cesta_id}/", response=CestaDetailSchema)
def cesta_detail(request, cesta_id: int):
    """Detalhe de uma cesta com produtos"""
    cesta = get_object_or_404(Cesta, id=cesta_id)
    return cesta
