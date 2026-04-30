from ninja import NinjaAPI

from app.api.cestas import router as cestas_router
from app.api.contato import router as contato_router
from app.api.perfil import router as perfil_router


# ============== API Instance ==============
api = NinjaAPI(
    title="Café com Pão API",
    version="1.0.0",
    description="API do projeto Café com Pão - Padarias, Cestas e Assinaturas",
)

# ============== Routers ==============
# App routers
api.add_router("/cestas", cestas_router)
api.add_router("/contato", contato_router)
api.add_router("/perfil", perfil_router)
