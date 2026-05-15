from ninja import NinjaAPI
from ninja_extra import exceptions
from ninja_jwt.routers.obtain import obtain_pair_router
from ninja_jwt.routers.verify import verify_router

from app.api.auth import router as auth_router
from app.api.padarias import router as padarias_router
from app.api.cestas import router as cestas_router
from app.api.contato import router as contato_router
from app.api.perfil import router as perfil_router


# ============== API Instance ==============
api = NinjaAPI(
    title="Café com Pão API",
    version="1.0.0",
    description="API do projeto Café com Pão - Padarias, Cestas e Assinaturas",
)


def api_exception_handler(request, exc):
    headers = {}
    if isinstance(exc.detail, (list, dict)):
        data = exc.detail
    else:
        data = {"detail": exc.detail}
    response = api.create_response(request, data, status=exc.status_code)
    for k, v in headers.items():
        response.setdefault(k, v)
    return response


api.exception_handler(exceptions.APIException)(api_exception_handler)


# ============== Routers ==============
# JWT Token (obtain pair + verify)
api.add_router("/auth/token", tags=["Auth"], router=obtain_pair_router)
api.add_router("/auth/token", tags=["Auth"], router=verify_router)

# App routers
api.add_router("/auth", auth_router)
api.add_router("/padarias", padarias_router)
api.add_router("/cestas", cestas_router)
api.add_router("/contato", contato_router)
api.add_router("/perfil", perfil_router)
