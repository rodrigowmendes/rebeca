from django.db import models
from .utils import validate_cpf
from datetime import datetime
from django.utils.translation import gettext_lazy as _


class City(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome da cidade', unique=True, null=False)
    federal_unit = models.CharField(max_length=2, verbose_name='UF', choices=FEDERAL_UNITS, null=False)

    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'

    def __str__(self):
        return '{0}.{1}'.format(
            self.name,
            self.federal_unit
        )


class Neighborhood(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome do bairro', unique=True, null=False)

    class Meta:
        verbose_name = 'Bairro'
        verbose_name_plural = 'Bairros'

    def __str__(self):
        return self.name


class SocialBenefit(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True, verbose_name='Nome')

    class Meta:
        verbose_name = 'Benefício social'
        verbose_name_plural = 'Benefícios sociais'

    def __str__(self):
        return self.name


class Record(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome usuário', null=False)
    date_of_birth = models.DateField(verbose_name='Data de nascimento')
    neighborhood = models.ForeignKey(Neighborhood, verbose_name='Bairro', on_delete=models.CASCADE, null=False)
    natural_from = models.ForeignKey(City, verbose_name='Naturalidade', on_delete=models.CASCADE, null=False)
    cpf = models.CharField(max_length=11, verbose_name='CPF ', unique=True, null=False, validators=[validate_cpf])
    gender = models.CharField(max_length=20, verbose_name='Gênero')
    race = models.CharField(max_length=20, verbose_name='Raça', null=False)
    scholarity = models.CharField(max_length=30, verbose_name='Escolaridade', null=False)
    debts = models.CharField(max_length=3, verbose_name='Dídivas')
    agreement = models.CharField(max_length=3, verbose_name='Possui convênio')
    family_composition = models.IntegerField(verbose_name='Composição familiar', null=False)
    estimated_income = models.CharField(max_length=32, verbose_name='Renda estimada')
    source_of_income = models.CharField(max_length=30, verbose_name='Fonte da renda')
    social_benefits = models.ManyToManyField(SocialBenefit, verbose_name='Benefícios sociais', blank=True)
    housing_condition = models.CharField(max_length=30, verbose_name='Condição de moradia', null=False)
    treatment = models.CharField(max_length=30, verbose_name='Tempo de tratamento', null=False)
    # Uso de medicação
    medication_origin = models.CharField(max_length=30, verbose_name='Origem da medicação', null=False)
    health_problems_in_family = models.CharField(max_length=30, verbose_name="Doenças na família", null=False)
    old_people_in_family = models.CharField(max_length=3, verbose_name="Idosos na família")
    disabled_in_family = models.CharField(max_length=3, verbose_name="Deficientes na família")
    early_pregnancy = models.CharField(max_length=3, verbose_name="Gravidez precoce")
    pregnant_or_lactating = models.CharField(max_length=3, verbose_name="Gestante ou lactante")
    alcohol_or_drug_user = models.CharField(max_length=3, verbose_name="Usuário de álcool ou drogas")

    class Meta:
        verbose_name = 'Questionário'
        verbose_name_plural = 'Questionários'

    def __str__(self):
        return '{0}.{1}'.format(
            self.name,
            self.neighborhood,
            self.gender,
            self.race,
            self.scholarity,
            self.estimated_income,
            self.treatment,
        )
