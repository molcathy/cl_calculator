

def get_coordinates(x_start, x_end, y_start, y_end, equation):
    """get_coordinates takes x and y starting and ending coordinates,
    calculates coordinates that are inside the graph
    and returns them as two lists of values"""
    x_coordinates = []
    y_coordinates = []
    while x_start <= x_end:
        # maybe y must be replaced with what actually the equation does to x_start
        y = equation(x_start)
        if y >= y_start and y <= y_end:
            x_coordinates.append(x_start)
            y_coordinates.append(y)
        # add a really small amount so it looks like a curve
        x_start += 0.01
    return x_coordinates, y_coordinates

#This might not even work, there are no 0 values in the list,you need access to the equation
def xy_intercept(x_start, x_end, y_start, y_end, equation):
    x_coordinates, y_coordinates = get_coordinates(
        x_start, x_end, y_start, y_end, equation
    )
    x_intercept = []
    y_intercept = []
    for x in x_coordinates:
        for y in y_coordinates:
            if y == 0 and x != 0:
                x_intercept.append(x)
            elif x == 0 and y != 0:
                y_intercept.append(y)
            elif x == 0 and y == 0:
                y_intercept.append(y)
                x_intercept.append(x)


def main():
    pass


if __name__ == "__main__":
    main()
