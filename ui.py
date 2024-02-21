from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

from main import encode, decode
from main import *
from PIL import Image, ImageTk

IMAGE_WIDTH = 650
IMAGE_HEIGHT = 400
IMAGE_PATH = ""


def switch_mode():
    current_mode = mode_var.get()
    if current_mode == "Encode":
        message_entry.config(state="normal")
    else:
        message_entry.delete(0, END)
        message_entry.config(state="disabled")


def upload_image():
    filename = filedialog.askopenfilename()
    with Image.open(filename) as img:
        img = img.resize((IMAGE_WIDTH, IMAGE_HEIGHT))
        img = ImageTk.PhotoImage(img)

        current_image_label = Label(right_frame, image=img, bg="grey")
        current_image_label.image = img
        current_image_label.grid(row=0, column=0, padx=5, pady=5)

        global IMAGE_PATH
        IMAGE_PATH = filename


def proceed():
    mode = mode_var.get()
    message = message_entry.get() if mode == "Encode" else None
    delimiter = delimiter_entry.get() if delimiter_entry == "" else "###END###"

    # check if user has imported image
    if IMAGE_PATH is None or IMAGE_PATH == "":
        messagebox.showerror("Error", "Please upload an image.")
        return

    elif mode.lower() == "encode" and not message:
        messagebox.showerror("Error", "Please enter a message.")
        return

    print(delimiter)
    if mode.lower() == "encode":
        encode(IMAGE_PATH, message, delimiter, "output")
        messagebox.showinfo("Completed", "Message encoded")
    if mode.lower() == "decode":
        message = decode(IMAGE_PATH, delimiter)
        messagebox.showinfo("Password", f"Your password: {message}")



root = Tk()  # create root window
root.title("Basic GUI Layout")  # title of the GUI window
root.maxsize(900, 600)  # specify the max size the window can expand to
root.config(bg="skyblue")  # specify background color

mode_var = StringVar()
mode_var.set("Encode")

# Create left and right frames
left_frame = Frame(root, width=200, height=400, bg='grey')
left_frame.grid(row=0, column=0, padx=10, pady=5)

right_frame = Frame(root, width=IMAGE_WIDTH, height=IMAGE_HEIGHT, bg='grey')
right_frame.grid(row=0, column=1, padx=10, pady=5)

# ------------------------------ LEFT FRAME -----------------------------------

# Mode selection
mode_label = Label(left_frame, text="Mode:", bg="grey")
mode_label.grid(row=0, column=0, padx=5, pady=5)

encode_radio = Radiobutton(left_frame, text="Encode", variable=mode_var, value="Encode", command=switch_mode, bg="grey")
encode_radio.grid(row=0, column=1, padx=5, pady=5)

decode_radio = Radiobutton(left_frame, text="Decode", variable=mode_var, value="Decode", command=switch_mode, bg="grey")
decode_radio.grid(row=0, column=2, padx=5, pady=5)

# Message entry
message_label = Label(left_frame, text="Message:", bg="grey")
message_label.grid(row=1, column=0, padx=5, pady=5)

message_entry = Entry(left_frame, width=20)
message_entry.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

# Delimiter entry
delimiter_label = Label(left_frame, text="Delimiter:", bg="grey")
delimiter_label.grid(row=2, column=0, padx=5, pady=5)

delimiter_entry = Entry(left_frame, width=20)
delimiter_entry.grid(row=2, column=1, columnspan=2, padx=5, pady=5)

# Image import
image_label = Label(left_frame, text="Import Image:", bg="grey")
image_label.grid(row=3, column=0, padx=5, pady=5)

image_button = Button(left_frame, text="Browse...", command=upload_image)
image_button.grid(row=3, column=1, columnspan=2, padx=5, pady=5)

# Proceed button
proceed_button = Button(left_frame, text="Proceed", command=proceed)
proceed_button.grid(row=5, column=0, columnspan=3, padx=5, pady=5, sticky="ew")

switch_mode()  # Call switch_mode initially to set up the interface

# ------------------------------ RIGHT FRAME -----------------------------------


root.mainloop()
