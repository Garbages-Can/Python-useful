from tkinter import *


class SierpinskiTriangle:
    def __init__(self):
        window = Tk()
        window.title("Sierpinski Triangle")

        self.width, self.height = (200, 200)
        self.canvas = Canvas(window, width=self.width, height=self.height)
        self.canvas.pack()

        frame = Frame(window)
        frame.pack()

        Label(frame, text="Enter an order: ").pack(side=LEFT)
        self.order = StringVar()
        Entry(frame, textvariable=self.order, justify=RIGHT).pack(side=LEFT)
        Button(frame, text="display", command=self.display).pack(side=LEFT)

        window.mainloop()

    def display(self):
        self.canvas.delete("line")
        p1 = [self.width / 2, 10]
        p2 = [10, self.height - 10]
        p3 = [self.width - 10, self.height - 10]
        self.display_triangles(int(self.order.get()), p1, p2, p3)

    def display_triangles(self, order, p1, p2, p3):
        if order == 0:
            self.drawline(p1, p2)
            self.drawline(p2, p3)
            self.drawline(p3, p1)
        else:
            p12 = self.midpoint(p1, p2)
            p23 = self.midpoint(p2, p3)
            p31 = self.midpoint(p3, p1)

            self.display_triangles(order - 1, p1, p12, p31)
            self.display_triangles(order - 1, p12, p2, p23)
            self.display_triangles(order - 1, p31, p23, p3)

    def drawline(self, p1, p2):
        self.canvas.create_line(p1[0], p1[1], p2[0], p2[1], tags="line")

    def midpoint(self, p1, p2):
        p = 2 * [0]
        p[0] = (p1[0] + p2[0]) / 2
        p[1] = (p1[1] + p2[1]) / 2
        return p


if __name__ == '__main__':
    SierpinskiTriangle()
