import re
import getpass

def validPassword(senha):
    erros = []

    if len(senha) < 8:
        erros.append('A senha deve conter no mínimo 8 caracteres')
    if not re.search(r'[A-Z]', senha):
        erros.append('Nenhuma letra maiúscula encontrado')
    if not re.search(r'[a-z]', senha):
        erros.append("Nenhuma letra minúscula encontrada")
    if not re.search(r'[0-9]', senha):
        erros.append('Nehum dígito encontrado')
    if not erros:
        erros.append('Senha válida')

    return erros

password = getpass.getpass("Digite sua senha:")
resultado = validPassword(password)
for erro in resultado:
    print(erro)