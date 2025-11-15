# Wire frame 2 Code ----------------------------------------------------------------------------------------------------------------------------------

import tkinter as tk
from tkinter import ttk

# Create the main application window
root = tk.Tk()
root.title("Wireframe 2: Student Checkout")

# Create a main frame to hold all content
main_frame = ttk.Frame(root, padding="10")
main_frame.grid(row=0, column=0, sticky="nsew")

# Configure grid columns to have equal weight
main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)

# --- Left Column: Student Information ---
left_frame = ttk.LabelFrame(main_frame, text="STUDENT INFORMATION", padding="10")
left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# Student Scan
ttk.Label(left_frame, text="Scan Student ID:").grid(row=0, column=0, sticky="w", pady=2)
ttk.Entry(left_frame, width=30).grid(row=0, column=1, sticky="w", pady=2)

# Spacer
ttk.Separator(left_frame, orient="horizontal").grid(row=1, column=0, columnspan=2, sticky="ew", pady=10)

# Simulated Loaded Data
ttk.Label(left_frame, text="Name:").grid(row=2, column=0, sticky="e", padx=5)
ttk.Label(left_frame, text="John Stanford", font=("Inter", 10, "bold")).grid(row=2, column=1, sticky="w", padx=5)

ttk.Label(left_frame, text="ID:").grid(row=3, column=0, sticky="e", padx=5)
ttk.Label(left_frame, text="1234567").grid(row=3, column=1, sticky="w", padx=5)

ttk.Label(left_frame, text="Status:").grid(row=4, column=0, sticky="e", padx=5)
ttk.Label(left_frame, text="Active", foreground="green").grid(row=4, column=1, sticky="w", padx=5)

ttk.Label(left_frame, text="Fines:").grid(row=5, column=0, sticky="e", padx=5)
ttk.Label(left_frame, text="$0.00", foreground="green").grid(row=5, column=1, sticky="w", padx=5)


# --- Right Column: Materials to Check Out ---
right_frame = ttk.LabelFrame(main_frame, text="MATERIALS TO CHECK OUT", padding="10")
right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

# Material Scan
ttk.Label(right_frame, text="Scan RFID Tag:").grid(row=0, column=0, sticky="w", pady=2)
ttk.Entry(right_frame, width=25).grid(row=0, column=1, sticky="w", pady=2)
ttk.Button(right_frame, text="[ADD]").grid(row=0, column=2, sticky="w", pady=2, padx=5)

# Queue Title
ttk.Label(right_frame, text="--- Queue ---", font=("Inter", 10, "italic")).grid(row=1, column=0, columnspan=3, pady=5)

# Listbox for queued items
listbox = tk.Listbox(right_frame, height=10, width=50)
listbox.grid(row=2, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")

# Add scrollbar to listbox
scrollbar = ttk.Scrollbar(right_frame, orient="vertical", command=listbox.yview)
listbox.configure(yscrollcommand=scrollbar.set)
scrollbar.grid(row=2, column=3, sticky="ns")

# Populate with mock data
listbox.insert(tk.END, "1. The Laws of Physics")
listbox.insert(tk.END, "   Due: 2025-12-06 (3 weeks)")
listbox.insert(tk.END, "2. California Weekly")
listbox.insert(tk.END, "   Due: 2025-11-22 (1 week)")
listbox.insert(tk.END, "3. [RFID: 99887766]")
listbox.insert(tk.END, "   ERROR: Cannot be issued!")

# Configure the error item color
listbox.itemconfig(5, {'fg': 'red'})


# --- Bottom Row: Action Buttons ---
button_frame = ttk.Frame(main_frame, padding="10")
button_frame.grid(row=1, column=0, columnspan=2, sticky="e")

ttk.Button(button_frame, text="COMPLETE CHECKOUT (2 Items)").pack(side="left", padx=10)
ttk.Button(button_frame, text="CANCEL ALL").pack(side="left", padx=1An0)

# --- Start the application ---
root.mainloop()