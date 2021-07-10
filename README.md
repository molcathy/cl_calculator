# cl_calculator

```sh
## install tkinter globally
brew install python-tk

## create & activate virtual environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

```s
when you have a line:
    y = mx + c
    the gradient and y intercept is a constant (m and c)
    x is a changing value

giving the graph the lines of:
    line 1 --> (550, 100, 550, 600)
    line 2 --> (100, 550, 600, 550)

scaling the line to the graph:
    figure out the smallest value of x and y within the graph:
        yco_ordinates = []
        xco_ordinates = []
        m = int(input('enter the gradient: '))
        c = int(input('enter the y intercept: '))
        for x in range(100, 600):
            y = (m * x) + c
            if y >= 100 and y <= 600:cccccclvtjdvnedldndhbrfljuetkltkutlcheefjbvr

                yco_ordinates.append(y)
                xco_ordinates.append(x)
        for i in range(0, len(yco_ordinates) - 1):
            canvas.create_line(xco_ordinates[i], yco_ordinates[i], xco_ordinates[i + 1], yco_ordinates[i + 1], width = 2, fill = "black")
```