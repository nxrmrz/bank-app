"""
A file for storing utility functions for data validation or otherwise
"""

from typing import Union

def validate_amount(amount: Union[float, int]):
    """
    Validator for a bank transaction amount. 
    Validates that it is non negative and a number
    """
    assert(amount >0)
    assert(isinstance(amount, (float, int)))
