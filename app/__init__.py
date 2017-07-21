import re
from .handle_str import handle_sentence
from .constant import FILE_PATH


def start():
    with open(FILE_PATH+"/data/sentences.txt", "r") as f:
        lines = f.readlines()
        print("INPUT:")
        for line in lines:
            line = re.sub(r'\n', '', line)
            print(line)
        print("\n"+"OUTPUT:")
        for line in lines:
            line = re.sub(r'\n', '', line)
            result = handle_sentence(line)
            if result:
                print(result)
