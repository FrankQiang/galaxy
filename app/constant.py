import os
import re

re_roman_str = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
FILE_PATH = os.path.split(os.path.realpath(__file__))[0]
RE_ROMAN = re.compile(re_roman_str)
ROMAN_PATTERN = {
    '0': ('', '', '', 'M'),
    '1': ("CM", "CD", 'D', 'C', 100),
    '2': ("XC", "XL", 'L', 'X', 10),
    '3': ("IX", "IV", 'V', 'I', 1)
}
ROMAN_NUMERALS = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
SENTENCE_ERROR = "It doesn't make sense"
