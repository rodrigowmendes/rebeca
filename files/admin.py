from django.contrib import admin

from . import models


@admin.register(models.Record)
class RecordAdmin(admin.ModelAdmin):
    fieldsets = [
            ('Informações pessoais', {'fields': [
                'name',
                'date_of_birth',
                'neighborhood',
                'natural_from',
                'cpf',
                'scholarity'
                ]}),
            ('Informações socioeconômicas', {'fields': [
                'family_composition',
                'estimated_income',
                'source_of_income',
                'social_benefit',
                'debts',
                'housing_condition'
                ]}),
            ('Informações sobre saúde', {'fields': [
                'agreement',
                'treatment',
                'medication_origin'
                ]}),
            ('Informações adicionais', {'fields': [
                'diseases_in_family',
                'old_people_in_family',
                'disabled_in_family'
                ]})
            ]
    search_fields = ('name', 'cpf', 'neighborhood', 'natural_from')


admin.site.register(models.City)
admin.site.register(models.Neighborhood)
admin.site.register(models.SocialBenefit)
admin.site.register(models.Disease)
admin.site.register(models.PersonWithDisease)


