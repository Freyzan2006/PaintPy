from tkinter import *
from PIL import Image, ImageDraw
from random import randint 
from tkinter import colorchooser, messagebox

def draw(event):
    x1, y1 = (event.x - brush_size), (event.y - brush_size)
    x2, y2, = (event.x + brush_size), (event.y + brush_size)
    canvas.create_oval(x1, y1, x2, y2, fill = color, width = 0)
    draw_img.ellipse((x1, y1, x2, y2), fill = color, width = 0)


def chooseColor():
    global color
    (rgb, hx) = colorchooser.askcolor()
    color = hx
    color_lab["bg"] = hx

def select(value):
    global brush_size
    brush_size = int(value)

def pour():
    canvas.delete("all")
    canvas["bg"] = color
    draw_img.rectangle((0, 0, 800, 700), width = 0, fill = color)
    draw_img.rectangle((0, 0, 800, 700), width = 0, fill = color)

def clear_canvas():
    canvas.delete("all")
    canvas["bg"] = "white"
    draw_img.rectangle((0, 0, 800, 700), width = 0, fill = "white")

def save_img():
    filename = f"image_{randint(0, 10000)}.png"
    image1.save(filename)
    messagebox.showinfo("Сохранение", "Сохранено по названием %s" % filename)

def popup(event):
    global x, y
    x = event.x
    y = event.y
    menu.post(event.x_root, event.y_root)

def square():
    canvas.create_rectangle(x, y, x + brush_size, y + brush_size, fill = color, width = 0)
    draw_img.polygon((x, y, x + brush_size, y, x + brush_size, y + brush_size, x, y + brush_size), fill = color)

def circle():
    canvas.create_oval(x, y, x + brush_size, y + brush_size, fill = color, width = 0)
    draw_img.ellipse((x, y, x + brush_size, y + brush_size), fill = color)


x = 0
y = 0

win = Tk()
win.title("Paint")
win.geometry("800x700")
win.resizable(False, False)

brush_size = 10
color = "black"

win.columnconfigure(6, weight = 1)
win.rowconfigure(2, weight = 1)

canvas = Canvas(win, background = "white")
canvas.grid(row = 2, column = 0, columnspan = 7, padx = 5, pady = 5, sticky = E + W + S + N)

canvas.bind("<B1-Motion>", draw)
canvas.bind("<Button-3>", popup)

menu = Menu(tearoff=0)
menu.add_command(label = "Квадрат", command = square)
menu.add_command(label = "Круг", command = circle)
image1 = Image.new("RGB", (800, 700), 'white')
draw_img = ImageDraw.Draw(image1)

Label(win, text = "Параметры").grid(row = 0, column = 0, padx = 6)

Button(win, text = "Выбрать цвет", width = 11, command = chooseColor).grid(row = 0, column = 1, padx = 6)

color_lab = Label(win, bg = color, width = 10)
color_lab.grid(row = 0, column = 2, padx = 6)

v = IntVar(value = 10)
Scale(win, variable = v, from_ = 1, to = 100, orient = HORIZONTAL, command = select).grid(row = 0, column = 3, padx = 6)

Label(win, text = "Действие: ").grid(row = 1, column = 0, padx = 6)

Button(win, text = "Заливка", width = 10, command = pour).grid(row = 1, column = 1)

Button(win, text = "Очистка: ", width = 10, command = clear_canvas).grid(row = 1, column = 2)

Button(win, text = "Сохранить", width = 10, command = save_img).grid(row = 1, column = 6)




if __name__ == "__main__":
    win.mainloop()