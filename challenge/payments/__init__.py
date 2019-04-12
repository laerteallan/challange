from abc import ABC, abstractclassmethod
import re


class AbstractTypePayment(ABC):
    """Class Abstract Type Payment."""
    __type__ = 'abstract'

    def __init__(self):
        super(AbstractTypePayment, self).__init__()

    @abstractclassmethod
    def create(self):
        raise NotImplementedError

    def validar_cpf(cpf: str) -> bool:
        if not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
            return False
        numbers = [int(digit) for digit in cpf if digit.isdigit()]

        if len(numbers) != 11:
            return False

        sum_of_products = sum(a * b for a, b in zip(numbers[0:9], range(10, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if numbers[9] != expected_digit:
            return False

        sum_of_products = sum(a * b for a, b in zip(numbers[0:10], range(11, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if numbers[10] != expected_digit:
            return False

        return True
