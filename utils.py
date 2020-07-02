from models import Pessoas, Usuarios

# Insere dados na tabela Pessoaas
def insere_pessoas():
    pessoa = Pessoas(nome='Leonardo',idade=44)
    print(pessoa)
    pessoa.save()

# Consulta dados na tabela Pessoas
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Leonardo').first()
    print(pessoa.idade)

# Altera dados na tabela Pessoas
def altera_pessoas():
    pessoa = Pessoas.query.filter_by(nome='Leonardo').first()
    pessoa.idade = 21
    pessoa.save()

# Exclui dados na tabela Pessoas
def exclui_pessoas():
    pessoa = Pessoas.query.filter_by(nome='Mari').first()
    pessoa.delete()

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

if __name__ == '__main__':
    #insere_pessoas()
    #altera_pessoas()
    #exclui_pessoas()
    #consulta_pessoas()
    insere_usuario('leonardo','123')
    insere_usuario('beraldo', '123')
    consulta_todos_usuarios()
