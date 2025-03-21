import tkinter as tk

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

def erase_objects(canvas, eraser, event):
    x, y = event.x, event.y
    overlap = canvas.find_overlapping(x, y, x + ERASER_SIZE, y + ERASER_SIZE)
    for obj in overlap:
        if obj != eraser:
            canvas.delete(obj)

def main():
    root = tk.Tk()
    root.title("Grid Eraser")
    
    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
    canvas.pack()
    
    for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
        for col in range(0, CANVAS_WIDTH, CELL_SIZE):
            canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE, fill="red")
    

    eraser = canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill="blue")
    
    def on_mouse_move(event):
        canvas.coords(eraser, event.x, event.y, event.x + ERASER_SIZE, event.y + ERASER_SIZE)
        erase_objects(canvas, eraser, event)
    
    canvas.bind("<Motion>", on_mouse_move)
    
    root.mainloop()

if __name__ == '__main__':
    main()
