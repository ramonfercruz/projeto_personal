from ..forms.pessoa_forms import PessoaForm
from ..services import pessoa_service, endereco_service
from django.shortcuts import render, redirect
from ..forms.pessoa_forms import PessoaForm
from ..forms.endereco_forms import EnderecoForm
from ..entidades import pessoa, endereco


def home(request):
    return render(request, 'base.html')


def retorna_pessoa(form_pessoa):
    nome = form_pessoa.cleaned_data['nome']
    sexo = form_pessoa.cleaned_data['sexo']
    cpf = form_pessoa.cleaned_data['cpf']
    data_nascimento = form_pessoa.cleaned_data['data_nascimento']
    email = form_pessoa.cleaned_data['email']
    password = form_pessoa.cleaned_data['password1']
    telefone = form_pessoa.cleaned_data['telefone']
    data_cadastro = form_pessoa.cleaned_data["data_cadastro"]
    pessoa_nova = pessoa.Pessoa(nome=nome, cpf=cpf, data_nascimento=data_nascimento, email=email,
                                telefone=telefone, sexo=sexo, password=password, data_cadastro=data_cadastro)
    return pessoa_nova


def retorna_endereco(form_endereco, pessoa_db, tipo_endereco=1):
    rua = form_endereco.cleaned_data['rua']
    numero = form_endereco.cleaned_data['numero']
    complemento = form_endereco.cleaned_data['complemento']
    bairro = form_endereco.cleaned_data['bairro']
    cidade = form_endereco.cleaned_data['cidade']
    estado = form_endereco.cleaned_data['estado']
    pais = form_endereco.cleaned_data['pais']
    cep = form_endereco.cleaned_data["cep"]
    endereco_novo = endereco.Endereco(rua=rua, numero=numero, complemento=complemento, cidade=cidade,
                                      estado=estado, pais=pais, cep=cep, pessoa=pessoa_db,
                                      tipo_endereco=tipo_endereco, bairro=bairro)
    return endereco_novo


def listar_pessoas(request):
    pessoas = pessoa_service.listar_pessoas()
    return render(request, 'pessoas/listar_pessoas.html', {'pessoas': pessoas})


def cadastrar_pessoa(request):
    if request.method == 'POST':
        form_pessoa = PessoaForm(request.POST)
        form_endereco = EnderecoForm(request.POST)
        if form_pessoa.is_valid():
            if form_endereco.is_valid():
                pessoa_nova = retorna_pessoa(form_pessoa)
                tipo_endereco = 1
                pessoa_db = pessoa_service.cadastrar_pessoa(pessoa_nova)
                endereco_novo = retorna_endereco(form_endereco, pessoa_db, tipo_endereco)
                endereco_service.cadastrar_endereco(endereco_novo)
    else:
        form_pessoa = PessoaForm()
        form_endereco = EnderecoForm()
    return render(request, 'pessoas/form_pessoa.html', {'form_pessoa': form_pessoa, 'form_endereco': form_endereco})


def listar_pessoa_id(request, id):
    pessoa = pessoa_service.listar_pessoa_id(id)
    enderedo_id = pessoa.id_pessoa
    tipo_endereco = 1
    endereco = endereco_service.listar_endereco_id(enderedo_id, tipo_endereco)
    return render(request, 'pessoas/listar_pessoa.html', {'pessoa': pessoa, 'endereco': endereco})


def editar_pessoa(request, id_pessoa):
    pessoa_antiga = pessoa_service.listar_pessoa_id(id_pessoa)
    endereco_id = pessoa_antiga.id_pessoa
    tipo_endereco = 1
    endereco_antigo = endereco_service.listar_endereco_id(endereco_id, tipo_endereco)
    form_pessoa = PessoaForm(request.POST or None, instance=pessoa_antiga)
    form_endereco = EnderecoForm(request.POST or None, instance=pessoa_antiga)
    if form_pessoa.is_valid():
        pessoa_nova = retorna_pessoa(form_pessoa)
        if form_endereco.is_valid():
            endereco_novo = retorna_endereco(form_endereco, pessoa_antiga, tipo_endereco)
            pessoa_service.editar_pessoa(pessoa=pessoa_antiga, pessoa_nova=pessoa_nova)
            endereco_service.editar_endereco(endereco=endereco_antigo, endereco_novo=endereco_novo)
            return redirect('listar_clientes')
    return render(request, 'pessoas/form_pessoa.html', {'form_pessoa': form_pessoa, 'form_endereco': form_endereco})





