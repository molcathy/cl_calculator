# TODO:
# * comment function
# * establish if formula I used in `main` & tests is mathematically valid; if not replace it
# * for each token evaluate the value of its components:
#   - the constant (e.g. a)
#   - the power of x
# * implement quadratic formula
"""
x = -b + math.sqrt(b^2 - 4ac) / 2a
x = -b - math.sqrt(b^2 - 4ac) / 2a
"""

# ?
# * per https://en.wikipedia.org/wiki/Quadratic_formula it seems has only *3* tokens/members at the left of the equal; not
"""
ax^2       + bx + c = 0
ax^2 + ... + bx + c = 0 # can it have multiple (undetermined ) tokens/members at the left of the equal ?
"""


def get_tokens(formula):
    tokenized = []
    tokens = formula.split(" ")

    for token in tokens:
        if tokens.index(token) == 0:
            if token == "+" or token == "-":
                sign = token
            elif token[0] == "+" or token[0] == "-":
                tokenized.append(token)
            else:
                tokenized.append("+" + token)
        elif token == "+":
            sign = "+"
        elif token == "-":
            sign = "-"
        elif token[0] == "+" or token[0] == "-":
            tokenized.append(token)
        else:
            tokenized.append(sign + token)

    return tokenized


def main():
    formula = "5x^3 + 4x^2 - 4x - 4"
    print(formula)
    print(get_tokens(formula))


if __name__ == "__main__":
    main()
