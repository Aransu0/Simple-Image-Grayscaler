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
            # Check if an image is already displayed
            filepath
        except:
            # If not, do not replace
            replace = False
        else:
            # If so, replace the image
            replace = True
        finally:
            # Get directory of selected file and display it
            filepath = os.path.abspath(file.name)
            display_image(filepath, replace)


def display_image(directory, replace, grayscale=False):
    """Displays image on window with fixed height"""
    global image_label
    global new_image

    if replace == True:
        # If an image is already displayed, remove it
        image_label.pack_forget()

    if grayscale == True:
        # Get image from file
        image = Image.open(directory).convert("L")
    else:
        image = Image.open(directory)

    # Resize images to a fixed height
    aspect_ratio = image.width / image.height
    new_width = int(625 * aspect_ratio)
    resized = image.resize((new_width, 625), Image.Resampling.LANCZOS)

    if grayscale == True:
        image = image.save("image_exports/new_image.png", "PNG")

    # Replace old image with the resized version
    new_image = ImageTk.PhotoImage(resized)

    # Display the image
    image_label = tk.Label(root, image=new_image)
    image_label.image = new_image
    image_label.pack()


def grayscale():
    display_image(filepath, True, True)


# Create a button
button = tk.Button(root, text="Browse", command=get_directory).pack(pady=10)

grayscale_button = tk.Button(root, text="Grayscale", command=grayscale).pack(pady=10)

root.mainloop()
