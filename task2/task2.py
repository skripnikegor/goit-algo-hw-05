from typing import Callable
import re

def generator_numbers(text: str):
    """
    Extract and yield all decimal numbers found in a given text string.

    Args:
        text (str): Input string that may contain numeric values 
                    written with either a comma or a dot as a decimal separator.

    Yields:
        str: Each matched numeric value as a string.

    Returns:
        int: Returns 0 if no numeric values are found in the text.
    """
    # check if text is string
    if not isinstance(text, str):
        raise TypeError("Argument 'text' must be a string.")
    
    # find all numbers by match in the text
    match = re.findall("(\s+[0-9]+[,.]+[0-9]+\s)", text)
    
    # if no mathes return an empty generator
    if not match:
        return iter(())

    # create iterator for returning results from match
    for number in match:
        yield number


def sum_profit(text: str, func: Callable):
    """
    Calculate the total sum of all numeric values extracted from text 
    using a provided generator function.

    Args:
        text (str): Input string containing numeric values.
        func (Callable): A function (typically generator_numbers) 
                         that extracts numbers from text and yields them.

    Returns:
        float: The total sum of all extracted numeric values, 
               converted to float before summation.
    """
    # check if func is funcrtion
    if not callable(func):
        raise TypeError("Argument 'func' must be a callable generator function.")
    
    # Create variable for sum
    sum = 0

    # added sums in loop from generator
    for n in func(text):
        sum += float(n)
    
    return sum



text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
print(sum_profit(text, generator_numbers))

text2 = "124.123 Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
print(sum_profit(text2, generator_numbers))

text3 = ""
print(sum_profit(text3, generator_numbers))

text4 = "1234.23 12434.12"
print(sum_profit(text4, generator_numbers))