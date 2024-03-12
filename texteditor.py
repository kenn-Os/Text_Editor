import tkinter as tk
from tkinter import filedialog
from tkinter import font
# tkinter is a module that makes it easier to create gui


def open_file():
    file_path = filedialog.askopenfilename()
    # for creating file/ directory selection windows
    with open(file_path, 'r') as file:
        content = file.read()
        text.delete(1.0, tk.END)
        text.insert(tk.END, content)

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    with open(file_path, 'w') as file:
        content = text.get(1.0, tk.END)
        file.write(content)
        # to write to an existing file

def underline_text():
    current_tags = text.tag_names(tk.SEL_FIRST)
    if 'underline' in current_tags:
        text.tag_remove('underline', tk.SEL_FIRST, tk.SEL_LAST)
        # sel_first is to return the position of the start of the current text selection
    else:
        text.tag_add('underline', tk.SEL_FIRST, tk.SEL_LAST)

def bold_text():
    current_tags = text.tag_names(tk.SEL_FIRST)
    if 'bold' in current_tags:
        text.tag_remove('bold', tk.SEL_FIRST, tk.SEL_LAST)
        # tags are used to apply formatting to specific ranges of texts
    else:
        text.tag_add('bold', tk.SEL_FIRST, tk.SEL_LAST)

def italicize_text():
    current_tags = text.tag_names(tk.SEL_FIRST)
    if 'italic' in current_tags:
        text.tag_remove('italic', tk.SEL_FIRST, tk.SEL_LAST)
    else:
        text.tag_add('italic', tk.SEL_FIRST, tk.SEL_LAST)

# Create the main window
root = tk.Tk()
root.title("Somaga\'s Document Editor")
# it creates the main window

# Create a text widget
text = tk.Text(root, wrap="word", undo=True)
text.pack(expand="yes", fill="both")
# the text widget is used to display text

# Create a menu
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)
# it creates the menu bar

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)
# these are the things in the file menu

format_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Format", menu=format_menu)
format_menu.add_command(label="Underline", command=underline_text)
format_menu.add_command(label="Bold", command=bold_text)
format_menu.add_command(label="Italic", command=italicize_text)
# these are the things under the format menu

# Configure tags for formatting
text.tag_configure('underline', underline=True)
text.tag_configure('bold', font=('TkDefaultFont', 10, 'bold'))
text.tag_configure('italic', font=('TkDefaultFont', 10, 'italic'))

# Run the application
root.mainloop()
# you can't run the program without calling the function
