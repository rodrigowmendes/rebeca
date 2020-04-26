from django.db import models
from .utils import validate_cpf
from datetime import datetime


# Opções
FEDERAL_UNITS = (
    ('AC', 'Acre (AC)'),
    ('AL', 'Alagoas (AL)'),
    ('AP', 'Amapá (AP)'),
    ('AM', 'Amazonas (AM)'),
    ('BA', 'Bahia (BA)'),
    ('CE', 'Ceará (CE)'),
    ('DF', 'Distrito Federal (DF)'),
    ('ES', 'Espírito Santo (ES)'),
    ('GO', 'Goiás (GO)'),
    ('MA', 'Maranhão (MA)'),
    ('MT', 'Mato Grosso (MT)'),
    ('MS', 'Mato Grosso do Sul (MS)'),
    ('MG', 'Minas Gerais (MG)'),
    ('PA', 'Pará (PA)'),
    ('PB', 'Paraíba (PB)'),
    ('PR', 'Paraná (PR)'),
    ('PE', 'Pernambuco (PE)'),
    ('PI', 'Piauí (PI)'),
    ('RJ', 'Rio de Janeiro (RJ)'),
    ('RN', 'Rio Grande do Norte (RN)'),
    ('RS', 'Rio Grande do Sul (RS)'),
    ('RO', 'Rondônia (RO)'),
    ('RR', 'Roraima (RR)'),
    ('SC', 'Santa Catarina (SC)'),
    ('SP', 'São Paulo (SP)'),
    ('SE', 'Sergipe (SE)'),
    ('TO', 'Tocantins (TO)'),
    )

SCHOLARITY = (
    ('Ensino Fundamental incompleto', 'Ensino Fundamental incompleto'),
    ('Ensino Fundamental em andamento', 'Ensino Fundamental em andamento'),
    ('Ensino Fundamental completo', 'Ensino Fundamental completo'),
    ('Ensino Médio incompleto', 'Ensino Médio incompleto'),
    ('Ensino Médio em andamento', 'Ensino Médio em andamento'),
    ('Ensino Médio completo', 'Ensino Médio completo'),
    ('Ensino Superior incompleto', 'Ensino Superior incompleto'),
    ('Ensino Superior em andamento', 'Ensino Superior em andamento'),
    ('Ensino Superior completo', 'Ensino Superior completo'),
)

GENRES = (
    ('Masculino', 'Masculino'),
    ('Feminino', 'Feminino'),
    ('Transgênero', 'Transgênero'),
    ('Não binário', 'Não binário'),
    ('Outros', 'Outros'),
)

RACES_COLORS = (
    ('Branca', 'Branca'),
    ('Negra', 'Negra'),
    ('Parda', 'Parda'),
    ('Amarela', 'Amarela'),
    ('Indígena', 'Indígena'),
)

SOURCES_OF_INCOME = (
    ('Informal apenas', 'Informal apenas'),
    ('Formal apenas', 'Formal apenas'),
    ('Ambas', 'Ambas'),
)

HOUSING_CONDITIONS = (
    ('Própria', 'Pŕopria'),
    ('Alugada', 'Alugada'),
    ('Cedida', 'Cedida'),
    ('Financiada', 'Financiada'),
)

TREATMENT_TIMES = (
    ('Até um ano', 'Até um ano'),
    ('Um a dois anos', 'Um a dois anos'),
    ('Dois a três anos', 'Dois a três anos'),
    ('Mais de três anos', 'Mais de três anos'),
)

MEDICATION_ORIGINS = (
    ('Farmácia municipal', 'Farmácia municipal'),
    ('Compra', 'Compra'),
    ('Farmácia municipal e compra', 'Farmácia municipal e compra'),
    ('Outros', 'Outros'),
)

ESTIMATED_INCOME = (
    ('Até um salário mínimo', 'Até um salário mínimo'),
    ('De um a dois salários mínimos', 'De um a dois salários mínimos'),
    ('De dois a três salários mínimos', 'De dois a três salários mínimos'),
    ('Mais de três salários mínimos', 'Mais de três salários mínimos'),
)

HEALTH_PROBLEMS_IN_FAMILY = (
    ('Não', 'Não'),
    ('Sim, são tratados', 'Sim, são tratados'),
    ('Sim, não são tratados', 'Sim, não são tratados'),
)

OPTIONS = (
    ('Sim', 'Sim'),
    ('Não', 'Não'),
)

    
class City(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name='Nome da cidade',
                            unique=True,
                            null=False)
    federal_unit = models.CharField(max_length=2,
                                    verbose_name='UF',
                                    choices = FEDERAL_UNITS,
                                    null=False)

    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'

    def __str__(self):
        return '{0}.{1}'.format(
            self.name,
            self.federal_unit
            )


class Neighborhood(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name='Nome do bairro',
                            unique=True,
                            null=False)

    class Meta:
        verbose_name = 'Bairro'
        verbose_name_plural = 'Bairros'

    def __str__(self):
        return self.name


class SocialBenefit(models.Model):
    name = models.CharField(max_length=100,
                            null=False,
                            unique=True,
                            verbose_name='Nome')

    class Meta:
        verbose_name = 'Benefício social'
        verbose_name_plural = 'Benefícios sociais'

    def __str__(self):
        return self.name


class Record(models.Model):
    name = models.CharField(max_length=100, 
                            verbose_name='Nome usuárix', 
                            null=False)
    date_of_birth = models.DateField(verbose_name='Data de nascimento')
    neighborhood = models.ForeignKey(Neighborhood,
                                     verbose_name='Bairro',
                                     on_delete=models.CASCADE,
                                     null=False)
    natural_from = models.ForeignKey(City,
                                     verbose_name='Naturalidade',
                                     on_delete=models.CASCADE,
                                     null=False)
    cpf = models.CharField(max_length=11,
                           verbose_name='CPF ',
                           unique=True,
                           null=False,
                           validators=[validate_cpf])
    gender = models.ForeignKey(Genre, 
                               verbose_name='Gênero',
                               on_delete=models.CASCADE,
                               null=False)
    race = models.ForeignKey(Race,
                            verbose_name='Raça',
                            on_delete=models.CASCADE,
                            null=False)
    scholarity = models.ForeignKey(Scolarity,
                                  verbose_name='Escolaridade',
                                  on_delete=models.CASCADE,
                                  null=False)
    debts = models.CharField(max_length=3, 
                             verbose_name='Dídivas', 
                             choices=OPTIONS)
    agreement = models.CharField(max_length=3, 
                                 verbose_name='Possui convênio', 
                                 choices=OPTIONS)
    family_composition = models.IntegerField(verbose_name='Composição familiar', 
                                             null=False)
    estimated_income = models.CharField(max_length=32, 
                                        choices=ESTIMATED_INCOME, 
                                        verbose_name='Renda estimada')
    source_of_income = models.CharField(max_length=30, 
                                        choices=SOURCES_OF_INCOME, 
                                        verbose_name='Fonte da renda')
    social_benefits = models.ManyToManyField(SocialBenefit, 
                                             verbose_name='Benefícios sociais', 
                                             blank=True)
    housing_condition = models.CharField(max_length=30,
                                         choices=HOUSING_CONDITIONS,
                                         verbose_name='Condição de moradia',
                                         null=False)
    treatment = models.CharField(max_length=30,
                                 choices=TREATMENT_TIMES,
                                 verbose_name='Tempo de tratamento',
                                 null=False)
    # Uso de medicação
    medication_origin = models.CharField(max_length=30,
                                         choices=MEDICATION_ORIGINS,
                                         verbose_name='Origem da medicação',
                                         null=False)
    health_problems_in_family= models.CharField(max_length=30,
                                                verbose_name="Doenças na família",
                                                choices=HEALTH_PROBLEMS_IN_FAMILY,
                                                null=False)
    old_people_in_family = models.CharField(max_length=3, 
                                            verbose_name="Idosos na família", 
                                            choices=OPTIONS)
    disabled_in_family = models.CharField(max_length=3, 
                                          verbose_name="Deficientes na família", 
                                          choices=OPTIONS)
    early_pregnancy = models.CharField(max_length=3, 
                                       verbose_name="Gravidez precoce", 
                                       choices=OPTIONS)
    pregnant_or_lactating = models.CharField(max_length=3, 
                                             verbose_name="Gestante ou lactante", 
                                             choices=OPTIONS)
    alcohol_or_drug_user = models.CharField(max_length=3, 
                                            verbose_name="Usuário de álcool ou drogas", 
                                            choices=OPTIONS)

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
