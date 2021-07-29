# TODO:
# * comment function
# * establish if formula I used in `main` & tests is mathematically valid; if not replace it
# * latter implement user input validation checks e.g check for non alphanumeric characters, make sure string contains x
# * sanitize data before processing e.g.: lower case anything
# * for each token evaluate the value of its components:
#   - the constant (e.g. a)
#   - the powers of x
# * implement quadratic formula
"""
x = -b + math.sqrt(b^2 - 4ac) / 2a
x = -b - math.sqrt(b^2 - 4ac) / 2a
"""

# ?
# * per https://en.wikipedia.org/wiki/Quadratic_formula it seems has only *3* tokens/members at the left of the equal
"""
ax^2       + bx + c = 0
ax^2 + ... + bx + c = 0 # can it have multiple (undetermined ) tokens/members at the left of the equal ?
"""
"""Asking about direction what I plan to do after I finish this problem"""


def get_tokens(formula):
    tokenized = []
    tokens = formula.split(" ")

    for token in tokens:
        if token == "+" or token == "-":
            sign = token
        elif token[0] == "+" or token[0] == "-":
            tokenized.append(token)
        elif tokens.index(token) == 0:
            tokenized.append("+" + token)
        else:
            tokenized.append(sign + token)

    return tokenized


def get_constant_power(tokens):
    constants = []
    powers = []

    for token in tokens:
        if "x" in token:
            temp = token.split("x")
            if "0123456789" in temp[0]:
                constants.append(float(temp[0]))
            elif "+" in temp[0]:
                constants.append(1)
            elif "-" in temp[0]:
                constants.append(-1)

            if "^" in temp[1]:
                temp2 = temp[1].split("^")
                if "0123456789" in temp2[1]:
                    powers.append(float(temp2[1]))
        elif "0123456789" in temp:
            constants.append(float(temp))

    return constants, powers


def main():
    formula = "5x^3 + 4x^2 - 4x - 4"
    tokens = get_tokens(formula)

    print(formula)
    print(get_tokens(formula))
    print(get_constant_power(tokens))


if __name__ == "__main__":
    main()
