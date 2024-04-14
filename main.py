from PIL import Image, ImageTk
import tkinter as tk
from tkinter.filedialog import askopenfile
import os

# Create GUI window
root = tk.Tk()
root.geometry("800x500")
root.title("Image Color Changer")


def open_file():
    file = tk.filedialog.askopenfile(mode="r")
    if file:
        filepath = os.path.abspath(file.name)

    image = Image.open(filepath)
    image = ImageTk.PhotoImage(image)
    image_label = tk.Label(root, image=image)
    image_label.image = image
    image_label.pack()


# Add a Label widget
label = tk.Label(root, text="Click the Button to browse the Files")
label.pack(pady=10)

# Create a Button
tk.Button(root, text="Browse", command=open_file).pack(pady=20)

root.mainloop()
