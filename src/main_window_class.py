from tkinter import *
from graph_window_class import GraphWindow


class MainWindow(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.parent = parent

        self.extra_inputs = []

        btnIntegration = Button(self, text="Integrate", command=self.Integration)
        btnDifferentiation = Button(
            self, text="Differentiate", command=self.Differentiation
        )
        btnTurningPoint = Button(
            self, text="Curve Turning Point", command=self.TurningPoint
        )
        btnArea = Button(self, text="Area Underneath Curve", command=self.Area)
        btnMaxMin_TP = Button(
            self, text="Cubic Max or Min Turning Point", command=self.MaxMin_TP
        )
        btnComplete_the_Square = Button(
            self, text="Complete the Square", command=self.Complete_the_Square
        )
        btnTangent = Button(self, text="Tangent", command=self.Tangent)
        btnNormal = Button(self, text="Normal", command=self.Normal)
        btnPB = Button(self, text="Perpendicular Bisector", command=self.PB)
        btnXY_Intercept = Button(
            self, text="x and y intercepts", command=self.XY_Intercept
        )
        btnAsymptote = Button(self, text="Asymptote", command=self.Asymptote)
        btnLinesIntersect = Button(
            self, text="Lines Intersect", command=self.LinesIntersect
        )
        btn_showGraph = Button(
            self, text="show polynomial", command=self.handle_showGraph
        )
        btn_delete_answer = Button(
            self, text="show polynomial", command=self.btn_delete_answer
        )
        self.lblAnswer = Label(self, text=" ", relief=RAISED)

        btn_showGraph.grid()

        self.formulaEntry = Entry(self)

        self.formulaEntry.grid()
        self.create_extra_inputs(3)
        self.lblAnswer.grid()

        btnIntegration.grid()
        btnDifferentiation.grid()
        btnTurningPoint.grid()
        btnArea.grid()
        btnMaxMin_TP.grid()
        btnComplete_the_Square.grid()
        btnTangent.grid()
        btnNormal.grid()
        btnPB.grid()
        btnXY_Intercept.grid()
        btnAsymptote.grid()
        btnLinesIntersect.grid()
        btn_delete_answer.grid()

    def create_extra_inputs(self, num_imputs):
        for e in self.extra_inputs:
            e.grid_forget()

        self.extra_inputs = []
        for i in range(num_imputs):
            extra_input = Entry(self)
            extra_input.grid()
            self.extra_inputs.append(extra_input)

    def show_answer(self, answer):
        self.lblAnswer = self.lblAnswer.config(text=answer)

    def btn_delete_answer(self):
        self.formulaEntry.delete(0, END)

    def Integration(self):
        from integration_differentiation import integration
        from tokenizef import (
            get_tokens,
            get_constant_power,
            generate_equation,
            string_constant_power,
        )

        formulaText = self.formulaEntry.get()  # This returns the value
        constants, powers = get_constant_power(get_tokens(formulaText))
        intC, intP = integration(powers, constants)
        integrated_polynomial = string_constant_power(intC, intP)
        self.show_answer(integrated_polynomial)

    def Differentiation(self):
        from integration_differentiation import differentiation
        from tokenizef import (
            get_tokens,
            get_constant_power,
            generate_equation,
            string_constant_power,
        )

        formulaText = self.formulaEntry.get()
        constants, powers = get_constant_power(get_tokens(formulaText))
        diffC, diffP = differentiation(powers, constants)
        differentiated_polynomial = string_constant_power(diffC, diffP)
        self.show_answer(differentiated_polynomial)

    def TurningPoint(self):
        from get_tp_area_as import get_turning_point
        from tokenizef import (
            get_tokens,
            get_constant_power,
            generate_equation,
            string_constant_power,
        )

        formulaText = self.formulaEntry.get()
        constants, powers = get_constant_power(get_tokens(formulaText))
        tpX, tpY = get_turning_point(powers, constants)
        self.show_answer(("(", str(tpX) + " " + str(tpY), ")"))

    def Area(self):
        from get_tp_area_as import get_area
        from tokenizef import (
            get_tokens,
            get_constant_power,
            generate_equation,
            string_constant_power,
        )

        formulaText = self.formulaEntry.get()
        self.create_extra_inputs(2)
        x_start = float(self.extra_inputs[0].get())
        x_end = float(self.extra_inputs[1].get())
        constants, powers = get_constant_power(get_tokens(formulaText))
        area = get_area(powers, constants, x_start, x_end)
        self.show_answer(str(area))

    def MaxMin_TP(self):
        from get_tp_area_as import max_or_min
        from tokenizef import (
            get_tokens,
            get_constant_power,
            generate_equation,
            string_constant_power,
        )

        formulaText = self.formulaEntry.get()
        tp_x = self.tp_x.get()
        constants, powers = get_constant_power(get_tokens(formulaText))
        max = max_or_min(constants, powers, tp_x)
        if max == True:
            self.show_answer("It is a max turning point")
        else:
            self.show_answer("It is a min turning point")

    def Complete_the_Square(self):
        from get_tp_area_as import complete_the_square
        from tokenizef import (
            get_tokens,
            get_constant_power,
            generate_equation,
            string_constant_power,
        )

        formulaText = self.formulaEntry.get()
        constants, powers = get_constant_power(get_tokens(formulaText))

    def Tangent(self):
        from get_normal_tangent_pb import get_tangent
        from tokenizef import (
            get_tokens,
            get_constant_power,
            generate_equation,
            string_constant_power,
        )

        formulaText = self.formulaEntry.get()
        constants, powers = get_constant_power(get_tokens(formulaText))

    def Normal(self):
        from get_normal_tangent_pb import get_normal
        from tokenizef import (
            get_tokens,
            get_constant_power,
            generate_equation,
            string_constant_power,
        )

        formulaText = self.formulaEntry.get()
        constants, powers = get_constant_power(get_tokens(formulaText))

    def PB(self):
        from get_normal_tangent_pb import get_pb
        from tokenizef import (
            get_tokens,
            get_constant_power,
            generate_equation,
            string_constant_power,
        )

        formulaText = self.formulaEntry.get()
        constants, powers = get_constant_power(get_tokens(formulaText))

    def XY_Intercept(self):
        from get_intercept import get_x_y_intercept
        from tokenizef import (
            get_tokens,
            get_constant_power,
            generate_equation,
            string_constant_power,
        )

        formulaText = self.formulaEntry.get()
        constants, powers = get_constant_power(get_tokens(formulaText))

    def Asymptote(self):
        from get_asymptote import get_a_asymptote
        from tokenizef import (
            get_tokens,
            get_constant_power,
            generate_equation,
            string_constant_power,
        )

        formulaText = self.formulaEntry.get()
        constants, powers = get_constant_power(get_tokens(formulaText))

    def LinesIntersect(self):
        from get_lines_intersect import get_intersect
        from tokenizef import (
            get_tokens,
            get_constant_power,
            generate_equation,
            string_constant_power,
        )

        formulaText = self.formulaEntry.get()
        constants, powers = get_constant_power(get_tokens(formulaText))

    def handle_showGraph(self):
        graph_tk = Toplevel(self)
        graph_tk.wm_title = "Graph ..."
        graph_window = GraphWindow(graph_tk)
        graph_window.setEquation(self.formulaEntry.get())


def main():
    root = Tk()
    root.wm_title("cl_calculator")
    root.geometry("640x480")
    mw = MainWindow(root)
    mw.pack(side="top", fill=BOTH, expand=True)
    root.mainloop()

    x_start = -5
    x_end = 5

    y_start = -5
    y_end = 5


if __name__ == "__main__":
    main()
