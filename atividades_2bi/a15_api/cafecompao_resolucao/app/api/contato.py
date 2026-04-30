from ninja import Router

from app.api.schemas import ContatoSchema, MessageSchema

router = Router(tags=["Contato"])


@router.post("/", response={200: MessageSchema})
def contato_create(request, payload: ContatoSchema):
    """Enviar mensagem de contato (apenas log no console)"""
    print(f"[API] Contato de {payload.name} ({payload.email})")
    print(f"[API] Telefone: {payload.telephone}")
    print(f"[API] Assunto: {payload.subject}")
    print(f"[API] Avaliação: {payload.rating} estrelas")
    print(f"[API] Mensagem: {payload.message}")

    return 200, {"message": f"Obrigado por entrar em contato, {payload.name}! Recebemos sua mensagem."}
