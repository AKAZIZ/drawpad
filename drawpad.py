from tkinter import *


class DrawPad:
    def __init__(self):
        self.drawing_color = '#007acc'  # Could be expressed with Hex color codes
        self.background_color = 'white'
        self.width = 1000
        self.hight = 500
        self.old_x = None
        self.old_y = None
        self.penWidth = 2
        self.root_window = Tk()  # Create the root Window
        self.root_window.geometry(f'{self.width}x{self.hight}')  # Set the size of the root window
        self.canvas = Canvas(self.root_window, width=self.width, height=self.hight, bg=self.background_color)  # Create the Canvas Window
        self.canvas.pack(fill=BOTH, expand=True)
        self.canvas.bind('<B1-Motion>', self.draw_line)  # Draw the line when the mouse button is pressed and the mouse is moved
        self.canvas.bind('<ButtonRelease-1>', self.reset)  # Reset the coordinates when the mouse button is released

    def draw_line(self, e):
        if self.old_x and self.old_y:
            self.canvas.create_line(self.old_x, self.old_y, e.x, e.y, width=self.penWidth, fill=self.drawing_color,
                                    capstyle=ROUND, smooth=True)
        self.old_x = e.x
        self.old_y = e.y

    def reset(self, e):  # Resetting or cleaning the canvas
        self.old_x = None
        self.old_y = None


if __name__ == '__main__':
    drawPad = DrawPad()
    drawPad.root_window.title("Draw Pad ✏️")
    drawPad.root_window.mainloop()
