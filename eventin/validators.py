from django.core.exceptions import ValidationError
from br_cpf_cnpj import is_valid_cpf
import phonenumbers
import re


def validate_cpf(value):
    # Normalize CPF by removing non-digit characters before validation
    cpf = re.sub(r'\D', '', value)

    if len(cpf) != 11:
        raise ValidationError("Invalid CPF")

    if not is_valid_cpf(cpf):
        raise ValidationError("Invalid CPF")

    return cpf


def validate_name(name):
    # Enforce basic name rules: minimum length and only alphabetic characters/spaces
    name = name.strip()

    if len(name) < 3:
        raise ValidationError(
            "Name must have at least 3 characters.")

    if not all(char.isalpha() or char.isspace() for char in name):
        raise ValidationError(
            "Name must contain only letters and spaces.")

    return name


def validate_phone(phone):
    # Enforce basic name rules: minimum length and only alphabetic characters/spaces
    phone = re.sub(r'\D', '', phone)

    if len(phone) < 11:
        raise ValidationError("Invalid phone number")

    phone = phonenumbers.parse(phone, "BR")
    if not phonenumbers.is_valid_number(phone):
        raise ValidationError("Invalid phone number")

    return phonenumbers.format_number(phone, phonenumbers.PhoneNumberFormat.E164)
