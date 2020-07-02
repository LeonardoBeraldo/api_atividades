from models import Pessoas

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

if __name__ == '__main__':
    insere_pessoas()
    #altera_pessoas()
    #exclui_pessoas()
    consulta_pessoas()
