import tkinter as tk
from tkinter import ttk, messagebox
import pyperclip



def generate_pattern(pattern_name):
    try:
        n = 5 
        pattern = ""
        code = ""

        if pattern_name == "Pyramid":
            pattern = "\n".join(" " * (n - i) + "* " * i for i in range(1, n + 1))
            code = (
                "n = 5\n"
                "for i in range(1, n + 1):\n"
                "    print(' ' * (n - i) + '* ' * i)"
            )
        elif pattern_name == "Reverse Pyramid":
            pattern = "\n".join(" " * i + "* " * (n - i) for i in range(n))
            code = (
                "n = 5\n"
                "for i in range(n):\n"
                "    print(' ' * i + '* ' * (n - i))"
            )
        elif pattern_name == "Rectangle":
            pattern = "\n".join("* " * 6 for _ in range(3))  # 10 columns wide and 3 rows high
            code = (
    "rows = int(input('Please Enter the Total Number of Rows  : '))\n"
    "columns = int(input('Please Enter the Total Number of Columns  : '))\n"
    "print('Rectangle Star Pattern')\n"
    "for i in range(rows):\n"
    "    for j in range(columns):\n"
    "        print('*', end='  ')\n"
    "    print()"
)

        elif pattern_name == "Butterfly":
            pattern = ""
            for i in range(1, n + 1):
                pattern += "* " * i + "  " * (2 * (n - i)) + "* " * i + "\n"
            for i in range(n, 0, -1):
                pattern += "* " * i + "  " * (2 * (n - i)) + "* " * i + "\n"
            code = (
    "r = 5\n"
    "\n"
   
    "for i in range(1, r + 1):\n"
    "    print('*' * i, end='')\n"
    "    print(' ' * (r - i) * 2, end='')\n"
    "    print('*' * i)\n"
    "\n"
    
    "for i in range(r, 0, -1):\n"
    "    print('*' * i, end='')\n"
    "    print(' ' * (r - i) * 2, end='')\n"
    "    print('*' * i)"
)

        elif pattern_name == "Hourglass":
            pattern = "\n".join("  " * (n - i) + "* " * (2 * i - 1) for i in range(n, 0, -1))
            pattern += "\n" + "\n".join("  " * (n - i) + "* " * (2 * i - 1) for i in range(2, n + 1))
            code = (
    "row = 4\n"
    "\n"
    "for i in range(row, 0, -1):\n"
    "    for j in range(row - i):\n"
    "        print(' ', end='')\n"
    "    for j in range(1, 2 * i):\n"
    "        print('*', end='')\n"
    "    print()\n"
    "\n"
    "for i in range(2, row + 1):\n"
    "    for j in range(row - i):\n"
    "        print(' ', end='')\n"
    "    for j in range(1, 2 * i):\n"
    "        print('*', end='')\n"
    "    print()"
)

        elif pattern_name == "Right Triangle":
            pattern = "\n".join("* " * i for i in range(1, n + 1))
            code = (
                "n = 5\n"
                "for i in range(1, n + 1):\n"
                "    print('* ' * i)"
            )
        else:
            pattern = "Pattern not found!"
            code = "N/A"

        return pattern, code
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
        return "", ""



def display_pattern():
    pattern_name = pattern_selector.get()
    pattern, code = generate_pattern(pattern_name)
    pattern_text.delete("1.0", tk.END)
    pattern_text.insert(tk.END, pattern)
    code_text.delete("1.0", tk.END)
    code_text.insert(tk.END, code)



def copy_code():
    code = code_text.get("1.0", tk.END).strip()
    if code:
        pyperclip.copy(code)
        messagebox.showinfo("Copied", "Code has been copied to the clipboard!")


# GUI setup
root = tk.Tk()
root.title("Star Pattern Generator")
root.geometry("800x650")
root.configure(bg="#FFFAE5") 


# Configure font globally
root.option_add("*Font", "Poppins 12")

# Header Label
header_label = tk.Label(
    root,
    text="Star Pattern Generator",
    font=("Poppins", 18, "bold"),
    bg="#0069D9",
    fg="white",
    pady=10,
    width=40
)
header_label.pack(pady=20)


patterns = [
    "Pyramid",
    "Reverse Pyramid",
    "Rectangle",
    "Butterfly",
    "Hourglass",
    "Right Triangle",
]
pattern_selector = ttk.Combobox(root, values=patterns, state="readonly", width=30)
pattern_selector.set("Select a pattern")
pattern_selector.pack(pady=10)

# Button to generate pattern
generate_button = tk.Button(
    root,
    text="Generate Pattern",
    command=display_pattern,
    bg="#28A745",
    fg="white",
    relief="flat",
    font=("Poppins", 14),
)
generate_button.configure(borderwidth=0)
generate_button.pack(pady=10)


pattern_label = tk.Label(
    root, text="Generated Pattern:", font=("Poppins", 16, "bold"), bg="#f1f1f1"
)
pattern_label.pack()
pattern_text = tk.Text(
    root, height=20, width=80, font=("Courier New", 12), relief="solid", bd=1
)
pattern_text.pack(pady=10)


code_label = tk.Label(
    root, text="Python Code:", font=("Poppins", 16, "bold"), bg="#f1f1f1"
)
code_label.pack()
code_text = tk.Text(
    root, height=20, width=80, font=("Courier New", 12), relief="solid", bd=1
)
code_text.pack(pady=10)


copy_button = tk.Button(
    root,
    text="Copy Code",
    command=copy_code,
    bg="#17A2B8",
    fg="white",
    relief="flat",
    font=("Poppins", 14),
)
copy_button.configure(borderwidth=0)
copy_button.pack(pady=10)


footer_label = tk.Label(
    root,
    text="Design and Implemented by Mohan (133) & Payel (176)",
    font=("Poppins", 10),
    bg="#f1f1f1",
    fg="#606060",
    anchor="se",
    padx=10,
    pady=5,
)
footer_label.place(relx=1.0, rely=1.0, anchor="se")


style = ttk.Style()
style.configure("TCombobox", borderwidth=5, relief="flat")


root.mainloop()
