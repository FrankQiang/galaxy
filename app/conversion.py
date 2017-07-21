import re
from .constant import RE_ROMAN, ROMAN_PATTERN


def conversion_to_num(roman_numerals):
    if RE_ROMAN.search(roman_numerals):
        num_dict = {"pattern": '^', "num": 0}
        i = 3
        roman_items = sorted(ROMAN_PATTERN.items())
        for roman_item in roman_items:
            if roman_item[0] != '0':
                handle_not_succession(num_dict, roman_item, roman_numerals)
            handle_succession(num_dict, roman_item, roman_numerals, i)
            i -= 1
        return num_dict["num"]
    else:
        print("Oops invalid roman numerals")
        return 0


def handle_succession(num_dict, roman_item, roman_numerals, i):
    temp_pattern_str = ''
    num = 0
    for k in range(4):
        pattern_str = "{0}{1}{2}".format(num_dict["pattern"],
                                         roman_item[1][3], '{'+str(k)+'}')
        if re.search(pattern_str, roman_numerals):
            num = k*(10**i)
            temp_pattern_str = pattern_str
    if temp_pattern_str:
        num_dict["pattern"] = temp_pattern_str
    num_dict["num"] += num


def handle_not_succession(num_dict, roman_item, roman_numerals):
    pattern_str = num_dict["pattern"]+roman_item[1][0]
    if re.search(pattern_str, roman_numerals):
        num_dict["num"] += 9*roman_item[1][4]
        num_dict["pattern"] = pattern_str
    else:
        pattern_str = num_dict["pattern"]+roman_item[1][1]
        if re.search(pattern_str, roman_numerals):
            num_dict["num"] += 4*roman_item[1][4]
            num_dict["pattern"] = pattern_str
        else:
            pattern_str = num_dict["pattern"]+roman_item[1][2]
            if re.search(pattern_str, roman_numerals):
                num_dict["num"] += 5*roman_item[1][4]
                num_dict["pattern"] = pattern_str
