from ..models import Endereco


def cadastrar_endereco(endereco):
    Endereco.objects.create(rua=endereco.rua, numero=endereco.numero, complemento=endereco.complemento, bairro=endereco.bairro,
                            cidade=endereco.cidade, estado=endereco.estado, pais=endereco.pais, cep=endereco.cep,
                            pessoa=endereco.pessoa, tipo_endereco=endereco.tipo_endereco)


def listar_endereco_id(pessoa_id, tipo_endereco):
    endereco = Endereco.objects.get(pessoa_id=pessoa_id, tipo_endereco=tipo_endereco)
    return endereco


def editar_endereco(endereco, endereco_novo):
    endereco.rua = endereco_novo.rua
    endereco.numero = endereco_novo.numero
    endereco.complemento = endereco_novo.complemento
    endereco.bairro = endereco_novo.bairro
    endereco.cidade = endereco_novo.cidade
    endereco.estado = endereco_novo.estado
    endereco.pais = endereco_novo.pais
    endereco.cep = endereco_novo.cep
    endereco.pessoa = endereco_novo.pessoa
    endereco.tipo_endereco_novo = endereco_novo.tipo_endereco
    endereco.save(force_update=True)