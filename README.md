# Validador de Senhas em Python

Um programa simples desenvolvido em python para validar se uma senha atende os requisitos básicos de segurança

O projeto utiliza expressões regulares para validar se a senha possuí no mínimo 8 dígitos, Pelo menos uma Letra maiúscula, pelo menos uma letra minúscula, pelo ménos um dígito.

## Requisitos

A senha deve conter:

- Ter no mínimo **8 caracteres**
- Conter pelo menos **uma letra maiúscula**
- Conter pelo menos **uma letra minúscula**
- Conter pelo menos **um número**

## Tecnologias utilizadas

- Python 3
- `re` -- Módulo para utilização de expressões regulares
- `getpass` --Permite o usuário digitar a senha sem exibir os caracteres no terminal

## Como executar
1 git clone https://github.com/DiegoVinc/validPassword
2 entre na pasta cd X
3 execute o programa python `valid_password.py`

## Funcionamento
Ao executar o programa será exigido uma senha, a senha não será exibida no terminal, caso a senha corresponda 
aos requisitos, o sistema irá retornar que a senha está valida. Caso não, será exibido o motivo da rejeição.
