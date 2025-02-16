import tkinter as Tkinter

root = Tkinter.Tk()
canvas = Tkinter.Canvas(root, width=500, height=500)
canvas.pack()

rects = []

def r(x: int, y: int, w: int, h: int):
    return {
        'x': x,
        'y': y,
        'w': w,
        'h': h
    }

r(0.03, 0, 3, 2)

def rect_intesection_with_rect(a: dict, b: dict):
    a = not ((a['x'] >= b['x'] + b['w'] or b['x'] >= a['x'] + a['w']) or (a['y'] >= b['y'] + b['h'] or b['y'] >= a['y'] + a['h']))

    return a

def rect_intersects_with_any_rect(a: dict, b: list):
    for i in b:
        if rect_intesection_with_rect(a, i):
            return True

    return False

def move_rect(events):
    fill = "green"
    for i in rects:
        if rect_intesection_with_rect(
            i,
            r(events.x, events.y, 50, 50)
        ):
            fill = "red"
    canvas.create_rectangle(events.x, events.y, events.x + 50, events.y + 50, fill=fill)

canvas.bind("<B1-Motion>", move_rect)

for i in rects:
    canvas.create_rectangle(i['x'], i['y'], i['x']+i['w'], i['y']+i['h'], outline='blue')


rects.append(r(0, 0, 10, 10))
rects.append(r(50, 20, 400, 120))
rects.append(r(15, 15, 120, 400))

def generate_rects(sX: int, sY: int, w: int, h: int):
    new_rects = []

    checkX = 0
    checkY = 0
    gx = 0
    nX = w // sX
    nY = h // sY
    n = 0
    while True:
        lastRect = None
        for y in range(1, nY + 1):
            for x in range(1, nX + 1):
                nr = r(checkX * sX, checkY * sY, x * sX, y * sY)
                if not (rect_intersects_with_any_rect(nr, new_rects) or rect_intersects_with_any_rect(nr, rects) or (checkX + x) * sX > w or (checkY + y) * sY > h):
                    if lastRect is None or nr['w'] * nr['h'] > lastRect['area']:
                        lastRect = nr
                        lastRect['area'] = nr['w'] * nr['h']

        gx = gx + 1
        checkX = gx % nX
        checkY = gx // nX

        if checkY > nY:
            break

        if lastRect is not None:
            new_rects.append(lastRect)
        
        n = n + 1
        
        

    return new_rects

d = generate_rects(50, 50, 500, 500)

import random

c = ['blue', 'green', 'red', 'yellow']
for i in d:
    random.shuffle(c)
    canvas.create_rectangle(i['x'], i['y'], i['x']+i['w'], i['y']+i['h'], fill=c[0], outline='black')

root.mainloop()