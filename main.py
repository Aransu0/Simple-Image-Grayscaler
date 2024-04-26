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


def display_image(directory, replace):
    """Displays image on window with fixed height"""
    global image_label

    if replace == True:
        # If an image is already displayed, remove it
        image_label.pack_forget()

    # Get image from file
    image = Image.open(directory)

    # Resize images to a fixed height
    aspect_ratio = image.width / image.height
    new_width = int(650 * aspect_ratio)
    resized = image.resize((new_width, 650), Image.Resampling.LANCZOS)

    # Replace old image with the resized version
    new_image = ImageTk.PhotoImage(resized)

    # Display the image
    image_label = tk.Label(root, image=new_image)
    image_label.image = new_image
    image_label.pack()


# Add a label widget
label = tk.Label(root, text="Click the Button to browse the Files")
label.pack(pady=10)

# Create a button
button = tk.Button(root, text="Browse", command=get_directory).pack(pady=20)

root.mainloop()
