import tkinter as tk
from tkinter import filedialog

def open_file_dialog():
    file_path = filedialog.askopenfilename(title="File Selection", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        selected_file_label.config(text=f"Selected File: {file_path}")
        process_file(file_path)

def process_file(file_path):
    # Implement your file processing logic here
    # For demonstration, let's just display the contents of the selected file
    try:
        with open(file_path, 'r') as file:
            file_contents = file.read()
            file_text.delete('1.0', tk.END)
            file_text.insert(tk.END, file_contents)
    except Exception as e:
        selected_file_label.config(text=f"Error: {str(e)}")

root = tk.Tk()
root.title("File Dialog")

open_button = tk.Button(root, text="Select and Open File", command=open_file_dialog)
open_button.pack(padx=30, pady=30)

selected_file_label = tk.Label(root, text="Selected File:")
selected_file_label.pack()

file_text = tk.Text(root, wrap=tk.WORD, height=20, width=50)
file_text.pack(padx=30, pady=30)

root.mainloop()
