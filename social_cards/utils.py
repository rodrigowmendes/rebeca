from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from validate_docbr import CPF

cpf = CPF()


def validate_cpf(value):
    result = cpf.validate(value)
    if not result:
        raise ValidationError(
            _('%(value)s não é um CPF válido'),
            params={'value': value},
        )
