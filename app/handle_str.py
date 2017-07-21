from .conversion import conversion_to_num
from .constant import ROMAN_NUMERALS, SENTENCE_ERROR


word_dict = {}
coin_dict = {}


def handle_sentence(sentence):
    words = sentence.split(' ')
    words_len = len(words)
    if words[-1] in ROMAN_NUMERALS:
        add_word(words)
    elif words[-1] == "Credits":
        add_coin(words, words_len)
    elif words[-1] == '?':
        result = answer_question(words, words_len)
        return result
    else:
        print(SENTENCE_ERROR)
        return 0


def add_word(words):
    word_dict[words[0]] = words[-1]


def add_coin(words, words_len):
    roman_numerals = ''
    for i in range(words_len-4):
        roman_numerals += word_dict[words[i]]
    num = conversion_to_num(roman_numerals)
    coin_dict[words[-4]] = int(words[-2])//int(num)


def answer_question(words, words_len):
    roman_numerals = ''
    result = ''
    if words[1] == "much":
        for i in range(3, words_len-1):
            result += words[i]+' '
            roman_numerals += word_dict[words[i]]
        num = conversion_to_num(roman_numerals)
        result = "{0}is {1}".format(result, num)
    elif words[1] == "many":
        for i in range(4, words_len-2):
            result += words[i]+' '
            roman_numerals += word_dict[words[i]]
        num = conversion_to_num(roman_numerals)
        result = "{0}{1} is {2} Credits".format(result, words[-2],
                                                coin_dict[words[-2]]*num)
    else:
        print(SENTENCE_ERROR)
        result = 0
    return result
