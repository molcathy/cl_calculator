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
