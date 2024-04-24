from PIL import Image, ImageTk
import tkinter as tk
from tkinter.filedialog import askopenfile
import os

# Create GUI window
root = tk.Tk()
root.geometry("1400x800")
root.resizable(0, 0)
root.title("Simple Image Editor")


def get_directory():
    """Gets the directory of a selected image in file explorer"""
    global filepath

    file = tk.filedialog.askopenfile(mode="r")
    if file:
        try:
            filepath
        except:
            replace = False
        else:
            global replace
            replace = True
        finally:
            filepath = os.path.abspath(file.name)
            display_image(filepath, replace)


def display_image(directory, replace):
    """Displays image on window with fixed height"""
    global image_label

    if replace == True:
        image_label.pack_forget()

    image = Image.open(directory)

    aspect_ratio = image.width / image.height
    new_width = int(650 * aspect_ratio)
    resized = image.resize((new_width, 650), Image.Resampling.LANCZOS)

    new_image = ImageTk.PhotoImage(resized)

    image_label = tk.Label(root, image=new_image)
    image_label.image = new_image
    image_label.pack()


# Add a Label widget
label = tk.Label(root, text="Click the Button to browse the Files")
label.pack(pady=10)

# Create a Button
button = tk.Button(root, text="Browse", command=get_directory).pack(pady=20)

root.mainloop()
