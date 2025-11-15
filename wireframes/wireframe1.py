# wire Frame 1 Code --------------------------------------------------------------------------------------------------------------------------------------------------------

import tkinter as tk
from tkinter import ttk

# Create the main application window
root = tk.Tk()
root.title("Wireframe 1: Book Record Creation")

# Create a frame to hold the content
main_frame = ttk.Frame(root, padding="20")
main_frame.grid(row=0, column=0, sticky="nsew")

# --- Title Header ---
title_label = ttk.Label(main_frame, text="CREATE NEW MATERIAL RECORD", font=("Inter", 14, "bold"))
title_label.grid(row=0, column=0, columnspan=3, pady=(0, 15))

# --- Form Fields ---
# We use .grid() for easy label-and-entry alignment
# sticky='e' (east) aligns labels to the right
row_index = 1

# RFID Tag
ttk.Label(main_frame, text="RFID Tag ID:").grid(row=row_index, column=0, sticky="e", padx=5, pady=5)
ttk.Entry(main_frame, width=30).grid(row=row_index, column=1, padx=5, pady=5)
ttk.Button(main_frame, text="<Scan RFID>").grid(row=row_index, column=2, padx=5, pady=5)
row_index += 1

# Title
ttk.Label(main_frame, text="Title:").grid(row=row_index, column=0, sticky="e", padx=5, pady=5)
ttk.Entry(main_frame, width=40).grid(row=row_index, column=1, columnspan=2, sticky="w", padx=5, pady=5)
row_index += 1

# Author
ttk.Label(main_frame, text="Author:").grid(row=row_index, column=0, sticky="e", padx=5, pady=5)
ttk.Entry(main_frame, width=40).grid(row=row_index, column=1, columnspan=2, sticky="w", padx=5, pady=5)
row_index += 1

# Publisher
ttk.Label(main_frame, text="Publisher:").grid(row=row_index, column=0, sticky="e", padx=5, pady=5)
ttk.Entry(main_frame, width=40).grid(row=row_index, column=1, columnspan=2, sticky="w", padx=5, pady=5)
row_index += 1

# Publication Date
ttk.Label(main_frame, text="Publication Date:").grid(row=row_index, column=0, sticky="e", padx=5, pady=5)
ttk.Entry(main_frame, width=20).grid(row=row_index, column=1, sticky="w", padx=5, pady=5)
row_index += 1

# Edition
ttk.Label(main_frame, text="Edition:").grid(row=row_index, column=0, sticky="e", padx=5, pady=5)
ttk.Entry(main_frame, width=10).grid(row=row_index, column=1, sticky="w", padx=5, pady=5)
row_index += 1

# Material Type (Dropdown)
ttk.Label(main_frame, text="Material Type:").grid(row=row_index, column=0, sticky="e", padx=5, pady=5)
material_types = ["Book", "Magazine", "Journal", "Research Paper", "Newspaper"]
ttk.Combobox(main_frame, values=material_types, state="readonly", width=18).grid(row=row_index, column=1, sticky="w", padx=5, pady=5)
row_index += 1

# Subject
ttk.Label(main_frame, text="Subject:").grid(row=row_index, column=0, sticky="e", padx=5, pady=5)
ttk.Entry(main_frame, width=20).grid(row=row_index, column=1, sticky="w", padx=5, pady=5)
row_index += 1

# Cost
ttk.Label(main_frame, text="Cost: $").grid(row=row_index, column=0, sticky="e", padx=5, pady=5)
ttk.Entry(main_frame, width=10).grid(row=row_index, column=1, sticky="w", padx=5, pady=5)
row_index += 1

# Purchase Date
ttk.Label(main_frame, text="Purchase Date:").grid(row=row_index, column=0, sticky="e", padx=5, pady=5)
ttk.Entry(main_frame, width=20).grid(row=row_index, column=1, sticky="w", padx=5, pady=5)
row_index += 1

# --- Separator and Buttons ---
ttk.Separator(main_frame, orient="horizontal").grid(row=row_index, column=0, columnspan=3, sticky="ew", pady=10)
row_index += 1

# Button Frame
button_frame = ttk.Frame(main_frame)
button_frame.grid(row=row_index, column=0, columnspan=3, sticky="e")

ttk.Button(button_frame, text="SAVE").pack(side="left", padx=5)
ttk.Button(button_frame, text="CLEAR").pack(side="left", padx=5)
ttk.Button(button_frame, text="CANCEL").pack(side="left", padx=5)

# --- Start the application ---
root.mainloop()

