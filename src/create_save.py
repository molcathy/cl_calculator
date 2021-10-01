# How do I know where the files go, where do I put them.
def how_many_check(list):
    if len(list) <= 5:
        return True
    else:
        return False


def save_upto5(formula, formulas):
    fs = formulas
    if how_many_check(formulas) == True:
        fs.append(formula)
    return fs


def delete_upto5(formulas, place):
    fs = formulas
    fs.clear(place)
    return fs


def main():
    pass


if __name__ == "__main__":
    main()
