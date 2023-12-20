import tkinter as tk
root = tk.Tk()
canvas = tk.Canvas(root, width=800, height=800, bg='black')
canvas.pack()
def koberec(x, y, d, depth):
    if depth > 0:
        depth -= 1
        canvas.create_line(x, y, x+d, y, fill='green')
        canvas.create_line(x+d, y, x+d, y-d, fill='green')
        canvas.create_line(x, y-d, x+d, y-d, fill='green')
        canvas.create_line(x, y, x, y-d, fill='green')
        koberec(x, y, d//3, depth)
        koberec(x+d//3, y, d//3, depth)
        koberec(x+2*(d//3), y, d//3, depth)
        koberec(x, y-d//3, d//3, depth)
        koberec(x, y-2*(d//3), d//3, depth)
        koberec(x+d//3, y-2*(d//3), d//3, depth)
        koberec(x+2*(d//3), y-2*(d//3), d//3, depth)
        koberec(x+2*(d//3), y-d//3, d//3, depth)
koberec(50, 750, 700, 6)
root.mainloop()
