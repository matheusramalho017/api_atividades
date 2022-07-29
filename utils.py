from models import Pessoas, Usuarios


def insere_pessoas():
    pessoa = Pessoas(nome="Matheus", idade=21)
    print(pessoa)
    pessoa.save()


def consulta():
    pessoa = Pessoas.query.all()
    print(pessoa)
    pessoa = Pessoas.query.filter_by(nome="Matheus").first()
    print(pessoa.idade)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome="Matheusa").first()
    pessoa.nome = "Angelino"
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome="Matheusa").first()
    pessoa.delete()

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

if __name__ == '__main__':
    # insere_usuario('mamatheus', '12345')
    # insere_usuario('astolfino', '12345')
    consulta_usuarios()
    # insere_pessoas()
    # exclui_pessoa()
    # consulta()
    # altera_pessoa()
