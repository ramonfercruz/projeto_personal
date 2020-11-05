from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.


class Pessoa(AbstractBaseUser):

    SEXO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('N', 'Nenhuma das opções')
    )

    id_pessoa = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, null=False, blank=False)
    cpf = models.CharField(max_length=14, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)
    data_cadastro = models.DateField(default=timezone.now)
    email = models.EmailField(unique=True, max_length=100, null=False, blank=False)
    telefone = models.CharField(max_length=50, null=False, blank=False)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=False, null=False, default='M')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome', 'cpf', 'data_nascimento', 'cpf', 'email', 'telefone']

    def __str__(self):
        return self.nome


class Endereco(models.Model):
    RESIDENCIAL_CHOICES = (
        (1, 'Residencial'),
        (2, 'Aula')
    )

    STATE_CHOICES = (
    ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'),
    ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'),
    ('SE', 'Sergipe'), ('TO', 'Tocantins'))

    id_endereco = models.AutoField(primary_key=True)
    pessoa = models.ForeignKey("Pessoa", on_delete=models.SET_NULL, null=True)
    rua = models.CharField(max_length=200, null=False, blank=False)
    numero = models.IntegerField(null=False, blank=False)
    complemento = models.CharField(max_length=200, null=False, blank=False)
    cep = models.CharField(max_length=9, null=False, blank=False)
    bairro = models.CharField(max_length=50, null=False, blank=False)
    cidade = models.CharField(max_length=50, null=False, blank=False)
    estado = models.CharField(choices=STATE_CHOICES, max_length=2, null=False, blank=False)
    pais = models.CharField(max_length=50, null=False, blank=False)
    tipo_endereco = models.IntegerField(choices=RESIDENCIAL_CHOICES, blank=False, null=False, default=1)
    data_cadastro = models.DateField(default=timezone.now)


    def __str__(self):
        return self.rua


class Aluno(models.Model):
    id_aluno = models.AutoField(primary_key=True)
    Pessoa = models.OneToOneField(Pessoa, on_delete=models.SET_NULL, null=True)
    data_cadastro = models.DateField(default=timezone.now)

    def __str__(self):
        return self.Pessoa


class Personal(models.Model):
    id_personalr = models.AutoField(primary_key=True)
    Pessoa = models.OneToOneField(Pessoa, on_delete=models.SET_NULL, null=True)
    data_cadastro = models.DateField(default=timezone.now)

    def __str__(self):
        return self.Pessoa


class UnidadeMedida(models.Model):
    id_unidade_medida = models.AutoField(primary_key=True)
    unidade_medida = models.CharField(max_length=20, null=False, blank=False)
    sigla_unidade_medida = models.CharField(max_length=10, null=False, blank=False)

    def __str__(self):
        return  self.sigla_unidade_medida


class TipoMedida(models.Model):
    id_tipo_medida = models.AutoField(primary_key=True)
    tipo_medida = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.tipo_medida


class PersonalAluno(models.Model):
    id_personal_aluno = models.AutoField(primary_key=True)
    aluno = models.ForeignKey("Aluno", on_delete=models.SET_NULL, null=True)
    personal = models.ForeignKey("Personal", on_delete=models.SET_NULL, null=True)


class MedidaAluno(models.Model):
    id_medida_aluno = models.AutoField(primary_key=True)
    personal_aluno = models.ForeignKey("PersonalAluno", on_delete=models.SET_NULL, null=True)
    aluno = models.ForeignKey("Aluno", on_delete=models.SET_NULL, null=True)
    tipo_medida = models.ForeignKey("TipoMedida", on_delete=models.SET_NULL, null=True)
    valor_medida = models.FloatField(null=False, blank=False)
    unidade_medida = models.ForeignKey("UnidadeMedida", on_delete=models.SET_NULL, null=True)
    data_registro = models.DateField(null=False, blank=False)

