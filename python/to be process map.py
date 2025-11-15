# to be process map --------------------------------------------------------------------------------------------------------------------------------------

 import graphviz

# Create the main graph
dot = graphviz.Digraph(comment='To-Be Process Map')
dot.attr(rankdir='TD', label='To-Be Process Map: New Automated Library System', fontsize='20', fontname='Inter')
dot.node_attr.update(fontname='Inter')
dot.edge_attr.update(fontname='Inter')

# --- Subgraph A: Automated RFID Checkout ---
with dot.subgraph(name='cluster_A') as c:
    c.attr(label='A: Automated RFID Checkout Process (To-Be)', style='filled', color='lightcyan')
    c.node_attr.update(style='filled', color='white', shape='box')
    
    c.node('A_Start', 'Start: Student brings material to counter', shape='ellipse')
    c.node('A_ScanBook', 'Staff scans material\'s RFID tag')
    c.node('A_ScanID', 'Staff scans student\'s ID card')
    c.node('A_System', 'System retrieves book & student details')
    c.node('A_CheckType', 'System checks material type', shape='diamond')
    c.node('A_SetDate3W', 'System applies 3-week issue period')
    c.node('A_SetDate1W', 'System applies 1-week issue period')
    c.node('A_Block', 'System flags: "Cannot be issued"', style='filled', color='mistyrose')
    c.node('A_Link', 'System links book to student profile & records dates')
    c.node('A_End', 'End: Checkout complete', shape='ellipse')
    
    c.edge('A_Start', 'A_ScanBook')
    c.edge('A_ScanBook', 'A_ScanID')
    c.edge('A_ScanID', 'A_System')
    c.edge('A_System', 'A_CheckType')
    c.edge('A_CheckType', 'A_SetDate3W', label='Book')
    c.edge('A_CheckType', 'A_SetDate1W', label='Magazine')
    c.edge('A_CheckType', 'A_Block', label='Newspaper')
    c.edge('A_SetDate3W', 'A_Link')
    c.edge('A_SetDate1W', 'A_Link')
    c.edge('A_Link', 'A_End')
    c.edge('A_Block', 'A_End')

# --- Subgraph B: Automated RFID Book Drop Return ---
with dot.subgraph(name='cluster_B') as c:
    c.attr(label='B: Automated RFID Book Drop Return (To-Be)', style='filled', color='lightcyan')
    c.node_attr.update(style='filled', color='white', shape='box')
    
    c.node('B_Start', 'Start: Student deposits material in Book Drop (24/7)', shape='ellipse')
    c.node('B_Read', 'Internal RFID reader scans tag')
    c.node('B_Identify', 'System identifies material & loan record')
    c.node('B_Cancel', 'System immediately cancels student\'s loan')
    c.node('B_CheckDate', 'System checks return date vs. due date', shape='diamond')
    c.node('B_CalcFine', 'System automatically calculates fine')
    c.node('B_AddFine', 'System adds fine to student\'s account')
    c.node('B_Notify', 'System sends automated email with fine details')
    c.node('B_End', 'End: Loan record closed', shape='ellipse')
    
    c.edge('B_Start', 'B_Read')
    c.edge('B_Read', 'B_Identify')
    c.edge('B_Identify', 'B_Cancel')
    c.edge('B_Cancel', 'B_CheckDate')
    c.edge('B_CheckDate', 'B_CalcFine', label='Delayed')
    c.edge('B_CheckDate', 'B_End', label='On Time')
    c.edge('B_CalcFine', 'B_AddFine')
    c.edge('B_AddFine', 'B_Notify')
    c.edge('B_Notify', 'B_End')

# --- Subgraph C: Automated Background Processes ---
with dot.subgraph(name='cluster_C') as c:
    c.attr(label='C: Automated Background Processes (To-Be)', style='filled', color='lightcyan')
    c.node_attr.update(style='filled', color='white', shape='box')

    # C1: Anti-Theft
    c.node('C1_Start', 'Student walks towards exit gate')
    c.node('C1_Gate', 'Exit gate RFID readers scan student')
    c.node('C1_Check', 'System checks if material is "Issued"', shape='diamond')
    c.node('C1_Pass', 'Student passes silently')
    c.node('C1_Alarm', 'System triggers loud alarm', style='filled', color='mistyrose')
    c.node('C1_End', 'End', shape='ellipse')
    
    c.edge('C1_Start', 'C1_Gate')
    c.edge('C1_Gate', 'C1_Check')
    c.edge('C1_Check', 'C1_Pass', label='Yes')
    c.edge('C1_Check', 'C1_Alarm', label='No (Unissued)')
    c.edge('C1_Pass', 'C1_End')
    c.edge('C1_Alarm', 'C1_End')

    # C2: Email Reminder
    c.node('C2_Start', 'Daily scheduled task runs')
    c.node('C2_Scan', 'System scans all "Issued" loan records')
    c.node('C2_Check', 'Finds loans due in 3 days?', shape='diamond')
    c.node('C2_Email', 'System sends reminder email to student')
    c.node('C2_End', 'End', shape='ellipse')

    c.edge('C2_Start', 'C2_Scan')
    c.edge('C2_Scan', 'C2_Check')
    c.edge('C2_Check', 'C2_Email', label='Yes')
    c.edge('C2_Check', 'C2_End', label='No')
    c.edge('C2_Email', 'C2_End')

# Render the graph
dot.format = 'png'
file_path = 'to_be_process_map'
try:
    dot.render(file_path, cleanup=True)
    print(f"Generated diagram: {file_path}.png")
except Exception as e:
    print(f"Error generating diagram: {e}")

