from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, constr
from datetime import datetime
from typing import List

login = FastAPI()

class Usuario(BaseModel):
    name: constr(min_length=2)
    birth: str
    cpf: constr(min_length=11, max_length=11)  
    email: EmailStr
    password: constr(min_length=8, max_length=8)

usuarios_db: List[Usuario] = []
@login.post("/login/usuario")
async def cadastrar_usuario(usuario: Usuario):

    try:
        datetime.strptime(usuario.birth, "%Y-%m-%d")
    except ValueError:
        raise HTTPException(status_code=400, detail="Data de nascimento inválida. Use YYYY-MM-DD.")
    if any(u.cpf == usuario.cpf for u in usuarios_db):
        raise HTTPException(status_code=400, detail="CPF já cadastrado.")   

    usuarios_db.append(usuario)
    return {"mensagem": "Usuário cadastrado com sucesso!", "usuario": usuario}

@login.get("/login/usuarios")
async def listar_usuarios():
    return usuarios_db
