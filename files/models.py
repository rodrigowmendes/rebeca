from django.db import models
from djchoices import DjangoChoices, ChoiceItem


class City(models.Model):
    name = models.CharField(
        max_length=100, 
        verbose_name='Nome da cidade',
        unique=True,
        null=False
        )
    
    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'

    def __str__(self):
        return self.name


class Neighborhood(models.Model):
    name = models.CharField(
        max_length=100, 
        verbose_name='Nome do bairro',
        unique=True,
        null=False
        )

    class Meta:
        verbose_name = 'Bairro'
        verbose_name_plural = 'Bairros'

    def __str__(self):
        return self.name


class SocialBenefit(models.Model):
    name = models.CharField(
        max_length=100, 
        verbose_name='Nome do benefício',
        unique=True,
        null=False
        )
    
    class Meta:
        verbose_name = 'Benefício social'
        verbose_name_plural = 'Benefícios sociais'

    def __str__(self):
        return self.name 


class Disease(models.Model):
    name = models.CharField(
        max_length=100, 
        verbose_name='Nome da doença',
        unique=True,
        null=False
        )
    
    class Meta:
        verbose_name = 'Doença'
        verbose_name_plural = 'Doenças'

    def __str__(self):
        return self.name 

# yes or no choices
class YesOrNoChoices(DjangoChoices):
    yes_choice = ChoiceItem('y', 'Sim')
    no_choice = ChoiceItem('n', 'Não')


class Record(models.Model):
    class Meta:
        verbose_name = 'Questionário'
        verbose_name_plural = 'Questionários'

    # scholarity choices
    class Scholarity(DjangoChoices):
        first_choice = ChoiceItem('1', 'Ensino fundamental incompleto')
        second_choice = ChoiceItem('2', 'Ensino fundamental completo')
        third_choice = ChoiceItem('3', 'Ensino médio incompleto')
        fourth_choice = ChoiceItem('4', 'Ensino médio completo')
        fifth_choice = ChoiceItem('5', 'Ensino superior incompleto')
        sixth_choice = ChoiceItem('6', 'Ensino superior completo')

    # source of income choices
    class SourceOfIncome(DjangoChoices):
        first_choice = ChoiceItem('1', 'Informal apenas')
        second_choice = ChoiceItem('2', 'Formal apenas')
        third_choice = ChoiceItem('3', 'Ambas')

    # housing condition choices
    class HousingCondition(DjangoChoices):
        first_choice = ChoiceItem('1', 'Pŕopria')
        second_choice = ChoiceItem('2', 'Alugada')
        third_choice = ChoiceItem('3', 'Cedida')
        fourth_choice = ChoiceItem('4', 'Financiada')

    # treatment time choices
    class TreatmentTime(DjangoChoices):
        first_choice = ChoiceItem('1', 'Até um ano')
        second_choice = ChoiceItem('2', 'Um a dois anos')
        third_choice = ChoiceItem('3', 'Dois a três anos')
        fourth_choice = ChoiceItem('4', 'Mais de três anos')

    # medication origin choices
    class MedicationOrigin(DjangoChoices):
        first_choice = ChoiceItem('1', 'Farmácia municipal')
        second_choice = ChoiceItem('2', 'Compra')
        third_choice = ChoiceItem('3', 'Outros')
    
    # estimated income choices
    class EstimatedIncome(DjangoChoices):
        first_choice = ChoiceItem('1', 'Até um salário mínimo')
        second_choice = ChoiceItem('2', 'De um a dois salários mínimos')
        third_choice = ChoiceItem('3', 'De dois a três salários mínimos')
        fourth_choice = ChoiceItem('4', 'Mais de três salários mínimos')


    name = models.CharField(
        max_length=100, 
        verbose_name='Nome da pessoa usuária',
        null=False
        )
    date_of_birth = models.DateField(verbose_name='Data de nascimento')
    neighborhood = models.ForeignKey(
        Neighborhood,
        verbose_name='Bairro',
        on_delete=models.CASCADE,
        null=False
    )
    natural_from = models.ForeignKey(
        City, 
        verbose_name='Naturalidade', 
        on_delete=models.CASCADE
        )
    cpf = models.CharField(
        max_length=11, 
        verbose_name='CPF ', 
        unique=True,
        null=False
        )
    scholarity = models.CharField(
        max_length=1,
        verbose_name='Escolaridade',
        choices=Scholarity.choices,
        null=False
    )
    debts = models.CharField(
        max_length=1,
        verbose_name='Dídivas',
        choices=YesOrNoChoices.choices
        )
    agreement = models.CharField(
        max_length=1,
        verbose_name='Convênio',
        choices=YesOrNoChoices.choices
        )
    family_composition = models.IntegerField(
        verbose_name='Composição familiar',
        null=False
        )
    estimated_income = models.CharField(
        max_length=32,
        choices=EstimatedIncome.choices,
        verbose_name='Renda estimada',
        )
    source_of_income = models.CharField(
        max_length=32, 
        choices=SourceOfIncome.choices,
        verbose_name='Fonte da renda'
        )
    social_benefit = models.ManyToManyField(
        SocialBenefit,
        verbose_name='Benefício social',
        blank=True
        )
    housing_condition = models.CharField(
        max_length=32,
        choices=HousingCondition.choices,
        verbose_name='Condição de moradia',
        null=False
        )
    treatment = models.CharField(
        max_length=32,
        choices=TreatmentTime.choices,
        verbose_name='Tempo de tratamento',
        null=False
        )
    # use_of_medication 
    medication_origin = models.CharField(
        max_length=32,
        choices=MedicationOrigin.choices,
        verbose_name='Origem da medicação',
        null=False
        )
    health_problems_in_family = models.ManyToManyField(
            Disease,
            verbose_name="Problemas de saúde na família",
            blank=True
            )
    problems_are_treated = models.CharField(
            max_length=1,
            verbose_name="Problemas são tratados",
            choices=YesOrNoChoices.choices,
            blank=True
            )
    old_people_in_family = models.CharField(
            max_length=1,
            verbose_name="Idosos na família",
            choices=YesOrNoChoices.choices
            )
    disabled_in_family = models.CharField(
            max_length=1,
            verbose_name="Deficientes na família",
            choices=YesOrNoChoices.choices
            )
    early_pregnancy = models.CharField(
            max_length=1,
            verbose_name="Gravidez precoce",
            choices=YesOrNoChoices.choices
            )
    pregnant_or_lactating = models.CharField(
            max_length=1,
            verbose_name="Gestante ou lactante",
            choices=YesOrNoChoices.choices
            )
    alcohol_or_drug_user = models.CharField(
            max_length=1,
            verbose_name="Usuário de álcool ou drogas",
            choices=YesOrNoChoices.choices
            )
    
    # calculating the income per person
    def income_per_person(self):
        return str(self.estimated_income / self.family_composition)

    def __str__(self):
        return '{0}.{1}'.format(
            self.name,
            self.neighborhood,
            self.scholarity,
            self.estimated_income,
            self.treatment
        )




    





