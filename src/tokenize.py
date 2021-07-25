def tokenize(formula):
    tokenized = []
    tokens = formula.split(" ")
    sign = "+"
    for token in tokens:
        if token == "-":
            sign = "-"
        if token == "+":
            sign = "+"
        else:
            if token != "+" and token != "-":
                tokenized.append(sign + token)
    return tokenized


def main():
    formula = "3x^2 + 4x - 4"
    print(formula)
    print(tokenize(formula))


if __name__ == "__main__":
    main()
