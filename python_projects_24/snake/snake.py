from tkinter import *
import random

root = Tk()
root.title("Anaconda")
root.mainloop()

WIDTH = 800
HEIGHT = 600
SEG_SIZE = 20
IN_GAME = True

c = Canvas(root, width=WIDTH, height=HEIGHT, bg="#ffffff")
c.grid()
c.focus_set()


# def create_block():
#     global BLOCK
#     posx = SEG_SIZE * random.randint(1, (WIDTH-SEG_SIZE) / SEG_SIZE)
#     posy = SEG_SIZE * random.randint(1, (WIDTH-SEG_SIZE) / SEG_SIZE)
#     BLOCK = c.create_oval(posx, posy, posx+SEG_SIZE, posy+SEG_SIZE, fill="red")


class Segment(object):

    def __init__(self, x, y):
        self.instance = c.create_rectangle(x, y, x+SEG_SIZE, y+SEG_SIZE, fill="green")


class Snake(object):
    def __init__(self, segments):
        self.segments = segments
        # списък с допустимите посоки за джижение на змията
        self.mapping = {"Down": (0, 1), "Up": (0, -1), "Left": (-1, 0), "Right": (1, 0)}
        # отначало змията се джижи надясно
        self.vector = self.mapping["Right"]

    def move(self):
        """Джижи змията хазад"""
        #обхождаме жсички сегменти без първи
        for index in range(len(self.segments) -1):
            segment = self.segments[index].instance
            x1, y1, x2, y2 = c.coords(self.segments[index+1].instance)
            # задажамее на всеки сегмент позицията на сегмента, стоящ след него
            c.coords(segment, x1, y1, x2, y2)
            # получаваме координатите на сегмента преди главата
            x1, y1, x2, y2 = c.coords(self.segments[-2].instance)
            # поставяме главата в посоката, указана във вектора на движение
            c.coords(self.segments[-1].instance,
                     x1 + self.vector[0]*SEG_SIZE,
                     y1 + self.vector[1]*SEG_SIZE,
                     x2 + self.vector[0]*SEG_SIZE,
                     y2 + self.vector[1]*SEG_SIZE)

    def change_direction(self, event):
        """промяна посоката на движение на змията"""

        # evwent предава символа на натиснатия клавиш
        # и ако този калвиш е в допустимите посоки променя посоката

        if event.keysum in self.mapping:
            self.vector = self.mapping[event.keysum]

    def add_segment(self):
        """добавя сегмент на змията"""
        # определяме последния сегмент
        last_seg = c.coords(self.segments[0].instance)

        # определяме координатите къде да поставят следващия елемент
        x  = last_seg[2] - SEG_SIZE
        y = last_seg[3] - SEG_SIZE

        # добавя

