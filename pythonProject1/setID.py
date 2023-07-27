from tags import *
from symbols import *

def setID(token):
    for key in tags.keys():
        if token in symbols:
            print(f"token: tag: {tags['letters']} lexeme: {token}")
            return

        if token in onlyoperators and token != "=":
            print(f"token: tag: {tags['onlyoperators']} lexeme: {token}")
            return

        if token in multioperators:
            print(f"token: tag: {tags['multioperators']} lexeme: {token}")
            return

        if token in reservedwords:
            if token == key:
                print(f"token: tag: {tags[key]}")
                return

        if token.isdigit():
            print(f"token: tag: {tags['value']} lexeme: {token}")
            return

        if token in letters:
            print(f"token: tag: {tags['letters']} lexeme: {token}")
            return

        if token == "=":
            print(f"token: {tags['eq']}")
            return










