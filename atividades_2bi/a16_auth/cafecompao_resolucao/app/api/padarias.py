from ninja import Router
from django.shortcuts import get_object_or_404
from typing import List

from app.models import Padaria
from app.api.schemas import PadariaSchema, PadariaDetailSchema

router = Router(tags=["Padarias"])


@router.get("/", response=List[PadariaSchema])
def padarias_list(request):
    """Listar todas as padarias"""
    return Padaria.objects.all()


@router.get("/{padaria_id}/", response=PadariaDetailSchema)
def padaria_detail(request, padaria_id: int):
    """Detalhe de uma padaria com endereço e cestas"""
    padaria = get_object_or_404(Padaria, id=padaria_id)
    return padaria

