# [PY-A01] Faça um programa em python que determine 
# em duas variáveis (senha e email) e que contenha 
# uma senha e um email cadastrados antecipadamente, 
# em seguida solicite ao usuário uma senha e um email 
# e utilize o laço de repetição juntamente com a estrutura 
# de condição para verificar se o email e a senha 
# digitado pelo usuário é igual ao email e senha cadastrados 
# antecipadamente. E enquanto a senha e o email que o usuário 
# digitou não for igual ao email e senha cadastrados ele continue em um loop.

# A resposta deve ser enviada em uma das seguintes formas:

# Arquivo Zipado
# Link do GitHub (Repositório Público)
# Link do Drive (Acesso para qualquer pessoa com o link)

print("Cadastre Senha e Email")

senha = 1234

email = "prova@infinity.com"

while True:
    senha_usuario = int(input ("Senha: "))
    email_usuario = input ("Email: ")
    
    if senha_usuario == senha and email_usuario == email:
        print("Autenticado!")
        break
    else:
        print("Senha ou login errados. Tente novamente")
    

