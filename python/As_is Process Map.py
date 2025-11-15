 # As_is Process Map -----------------------------------------------------------------------------------------------------------------

As_is Process Map
import graphviz

# Create the main graph
dot = graphviz.Digraph(comment='As-Is Process Map')
dot.attr(rankdir='TD', label='As-Is Process Map: Current Manual Library System', fontsize='20', fontname='Inter')

# --- Subgraph A: Manual Book Checkout ---
with dot.subgraph(name='cluster_A') as c:
    c.attr(label='A: Manual Book Checkout Process (As-Is)', style='filled', color='lightgrey', fontname='Inter')
    c.node_attr.update(style='filled', color='white', shape='box', fontname='Inter')

    # Define nodes for Subgraph A
    c.node('A_Start', 'Start: Student selects book', shape='ellipse')
    c.node('A_Queue', 'Student waits in queue at checkout counter')
    c.node('A_Present', 'Student presents book & library card to staff')
    c.node('A_Search', 'Staff manually searches for physical ledger/card')
    c.node('A_Record', 'Staff manually writes student\'s name & due date on book\'s card')
    c.node('A_File', 'Staff files the card alphabetically/by date')
    c.node('A_Stamp', 'Staff manually stamps due date in book')
    c.node('A_End', 'End: Student leaves with book', shape='ellipse')

    # Define edges for Subgraph A
    c.edge('A_Start', 'A_Queue')
    c.edge('A_Queue', 'A_Present')
    c.edge('A_Present', 'A_Search')
    c.edge('A_Search', 'A_Record')
    c.edge('A_Record', 'A_File')
    c.edge('A_File', 'A_Stamp')
    c.edge('A_Stamp', 'A_End')

# --- Subgraph B: Manual Book Return & Fine Process ---
with dot.subgraph(name='cluster_B') as c:
    c.attr(label='B: Manual Book Return & Fine Process (As-Is)', style='filled', color='lightgrey', fontname='Inter')
    c.node_attr.update(style='filled', color='white', shape='box', fontname='Inter')

    # Define nodes for Subgraph B
    c.node('B_Start', 'Start: Student returns book at counter', shape='ellipse')
    c.node('B_Time', 'Only possible during library timings', shape='box', style='filled', color='mistyrose')
    c.node('B_FindCard', 'Staff manually finds the book\'s checkout card')
    c.node('B_CheckDate', 'Staff compares return date to due date', shape='diamond')
    c.node('B_CalcFine', 'Staff manually calculates fine\n(Tedious & Time-Consuming)', shape='box', style='filled', color='mistyrose')
    c.node('B_Collect', 'Staff collects cash fine')
    c.node('B_RecordFine', 'Staff manually records fine in a separate ledger')
    c.node('B_Clear', 'Staff marks book as returned')
    c.node('B_Shelve', 'Book is placed aside for re-shelving')
    c.node('B_End', 'End: Process complete', shape='ellipse')

    # Define edges for Subgraph B
    c.edge('B_Start', 'B_FindCard')
    c.edge('B_Start', 'B_Time') # Showing this as a parallel constraint
    c.edge('B_FindCard', 'B_CheckDate')
    c.edge('B_CheckDate', 'B_CalcFine', label='Delayed')
    c.edge('B_CheckDate', 'B_Clear', label='On Time')
    c.edge('B_CalcFine', 'B_Collect')
    c.edge('B_Collect', 'B_RecordFine')
    c.edge('B_RecordFine', 'B_Clear')
    c.edge('B_Clear', 'B_Shelve')
    c.edge('B_Shelve', 'B_End') # Fixed typo: changed 'B_ShelV_End' to 'B_Shelve', 'B_End'

# Render the graph
dot.format = 'png'
file_path = 'as_is_process_map'
try:
    dot.render(file_path, cleanup=True)
    print(f"Generated diagram: {file_path}.png")
except Exception as e:
    print(f"Error generating diagram. Please ensure 'graphviz' is installed and accessible in your system's PATH. Error: {e}")
