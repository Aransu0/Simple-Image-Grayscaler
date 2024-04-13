from PIL import Image, ImageTk
import tkinter as tk
import tkinterdnd2 as tkdnd


def directory_drop(event):
    image_directory = directory.insert("end", event.data)

    image = Image.open(image_directory)
    image = ImageTk.PhotoImage(image)

    image_label = tk.Label(root, image=image)
    image_label.pack()


root = tkdnd.Tk()
root.geometry("800x500")
root.title("Image Color Changer")

directory = tk.Listbox(root, selectmode=tk.SINGLE)
directory.pack()
directory.drop_target_register(tkdnd.DND_FILES)
directory.dnd_bind("<<Drop>>", directory_drop)

root.mainloop()
