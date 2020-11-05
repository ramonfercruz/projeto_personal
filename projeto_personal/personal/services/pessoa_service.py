from ..models import Pessoa


def listar_pessoas():
    pessoas = Pessoa.objects.all()
    return pessoas


def cadastrar_pessoa(pessoa):
    return Pessoa.objects.create(nome=pessoa.nome, cpf=pessoa.cpf, data_nascimento=pessoa.data_nascimento, email=pessoa.email,
                          telefone=pessoa.telefone, sexo=pessoa.sexo, password=pessoa.password)


def listar_pessoa_id(id_pessoa):
    cliente = Pessoa.objects.get(id_pessoa=id_pessoa)
    return cliente


def editar_pessoa(pessoa, pessoa_nova):
    pessoa.nome = pessoa_nova.nome
    pessoa.cpf = pessoa_nova.cpf
    pessoa.data_nascimento = pessoa_nova.data_nascimento
    pessoa.email = pessoa_nova.email
    pessoa.telefone = pessoa_nova.telefone
    pessoa.sexo = pessoa_nova.sexo
    pessoa.password = pessoa_nova.password
    pessoa.save(force_update=True)



