from django.core.exceptions import ValidationError
from br_cpf_cnpj import is_valid_cpf
import re


def validate_cpf(value):
    cpf = re.sub(r'\D', '', value)

    if len(cpf) != 11:
        raise ValidationError("Invalid CPF")

    if not is_valid_cpf(cpf):
        raise ValidationError("Invalid CPF")
