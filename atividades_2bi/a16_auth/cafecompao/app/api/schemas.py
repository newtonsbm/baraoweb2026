from ninja import Schema
from typing import Optional, List
from datetime import date


# ============== Mensagem / Contato ==============
class MessageSchema(Schema):
    """Schema para mensagem de sucesso/erro"""
    message: str


# ============== Categorias ==============
class CategoriaSchema(Schema):
    id: int
    nome: str


# ============== Produtos ==============
class ProdutoSchema(Schema):
    id: int
    nome: str
    descricao: Optional[str] = None
    preco: float
    categoria: Optional[CategoriaSchema] = None


# ============== Endereço ==============
class EnderecoSchema(Schema):
    id: int
    rua: str
    numero: str
    complemento: Optional[str] = None
    bairro: Optional[str] = None
    cidade: str
    estado: str
    cep: str


# ============== Cestas ==============
class CestaSchema(Schema):
    id: int
    nome: str
    descricao: Optional[str] = None
    preco: float
    nivel: str
    image_url: Optional[str] = None


class CestaDetailSchema(Schema):
    id: int
    nome: str
    descricao: Optional[str] = None
    preco: float
    nivel: str
    image_url: Optional[str] = None
    produtos: List[ProdutoSchema]


# ============== User / Auth ==============
class UserSchema(Schema):
    id: int
    username: str
    email: str
    first_name: str
    last_name: str


class UserRegisterSchema(Schema):
    email: str
    password: str
    first_name: Optional[str] = ""
    last_name: Optional[str] = ""


# ============== Contato ==============
class ContatoSchema(Schema):
    name: str
    email: str
    subject: str
    message: str
    rating: Optional[int] = None
    telephone: Optional[str] = None


# ============== Perfil ==============
class PerfilSchema(Schema):
    id: int
    telefone: Optional[str] = None
    data_nascimento: Optional[date] = None
    cpf: Optional[str] = None
    user: UserSchema
