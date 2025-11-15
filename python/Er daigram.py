# code for ER Daigram ----------------------------------------------------------------------------------------------------------------

Untitled3.ipynb
Untitled3.ipynb_
Files
..
Drop files to upload them to session storage.
Disk
69.49 GB available

[2]
0s
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
Generated diagram: as_is_process_map.png

[4]
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
Generated diagram: to_be_process_map.png

[5]
0s
import graphviz

# Create the Use Case Diagram
dot = graphviz.Graph('use_case_diagram')
dot.attr(label='LMS Scope - Use Case Diagram', fontsize='20', fontname='Inter')
dot.attr(rankdir='LR') # Left-to-Right ranking

# Define node attributes
dot.node_attr.update(fontname='Inter', shape='box')

# Define Actors (outside the system boundary)
with dot.subgraph(name='cluster_Actors') as c:
    c.attr(label='Actors', style='dashed')
    c.node('A1', 'Student', shape='actor')
    c.node('A2', 'Library Staff', shape='actor')
    c.node('A3', 'Management', shape='actor')
    c.node('A4', 'RFID Gate', shape='box', style='filled', color='lightgrey')
    c.node('A5', 'Book Drop Box', shape='box', style='filled', color='lightgrey')
    c.node('A6', 'Email System', shape='box', style='filled', color='lightgrey')

# Define Use Cases (inside the system boundary)
with dot.subgraph(name='cluster_System') as c:
    c.attr(label='Stanford Library Management System (LMS)', style='solid', color='blue')
    c.node_attr.update(shape='ellipse', style='filled', color='white')
    c.node('UC1', 'Manage Materials')
    c.node('UC2', 'Checkout Material')
    c.node('UC3', 'Return Material (Counter)')
    c.node('UC4', 'Return Material (Book Drop)')
    c.node('UC5', 'Manage Fines')
    c.node('UC6', 'Search Catalogue')
    c.node('UC7', 'Generate Reports')
    c.node('UC8', 'Access Digital Resources')
    c.node('UC9', 'Check Loan Status Online')
    c.node('UC10', 'Send Email Notifications')
    c.node('UC11', 'Trigger Anti-Theft Alarm')

# Define relationships
dot.edge('A1', 'UC6')
dot.edge('A1', 'UC8')
dot.edge('A1', 'UC9')
dot.edge('A1', 'UC2') # Student participates in checkout
dot.edge('A1', 'UC3') # Student participates in counter return
dot.edge('A1', 'UC4') # Student initiates book drop return

dot.edge('A2', 'UC1')
dot.edge('A2', 'UC2') # Staff initiates checkout
dot.edge('A2', 'UC3') # Staff initiates counter return
dot.edge('A2', 'UC5')
dot.edge('A2', 'UC6')
dot.edge('A2', 'UC11') # Staff is alerted

dot.edge('A3', 'UC7')

# System-to-System interactions
dot.edge('A5', 'UC4') # Book Drop Box provides data to this use case
dot.edge('A4', 'UC11') # RFID Gate provides data to this use case
dot.edge('UC10', 'A6') # System sends instructions to Email System
dot.edge('UC10', 'A1') # Notification is for the student

# Render the graph
dot.format = 'png'
file_path = 'use_case_diagram'
try:
    dot.render(file_path, cleanup=True)
    print(f"Generated diagram: {file_path}.png")
except Exception as e:
    print(f"Error generating diagram: {e}")
Warning: using box for unknown shape actor
Generated diagram: use_case_diagram.png

[6]
0s
import graphviz

# Create the Data Flow Diagram (Level 0 - Context)
dot = graphviz.Digraph('dfd_level_0')
dot.attr(label='LMS - Data Flow Diagram (Level 0)', fontsize='20', fontname='Inter', rankdir='TB')
dot.node_attr.update(fontname='Inter')
dot.edge_attr.update(fontname='Inter')

# 1. Define the Central Process
dot.node('P1', 'Library Management System', shape='circle', style='filled', color='lightblue')

# 2. Define External Entities
dot.node('E1', 'Student', shape='box', style='filled', color='lightgrey')
dot.node('E2', 'Library Staff', shape='box', style='filled', color='lightgrey')
dot.node('E3', 'Management', shape='box', style='filled', color='lightgrey')
dot.node('E4', 'RFID Hardware\n(Scanners, Gates, Book Drop)', shape='box', style='filled', color='lightgrey')
dot.node('E5', 'Email System', shape='box', style='filled', color='lightgrey')

# 3. Define Data Flows (Inputs to System)
dot.edge('E1', 'P1', label='Student ID, Search Query, Digital Content Request')
dot.edge('E2', 'P1', label='Staff Login, New Material Data, Search Query')
dot.edge('E3', 'P1', label='Management Login, Report Request')
dot.edge('E4', 'P1', label='RFID Tag Data, Return Confirmation')

# 4. Define Data Flows (Outputs from System)
dot.edge('P1', 'E1', label='Loan Status, Search Results, Digital Content, Due Date')
dot.edge('P1', 'E2', label='Search Results, Fine Details, Alarm Trigger')
dot.edge('P1', 'E3', label='Generated Reports')
dot.edge('P1', 'E4', label='Alarm Trigger Signal')
dot.edge('P1', 'E5', label='Reminder/Fine Email Content')

# Render the graph
dot.format = 'png'
file_path = 'dfd_level_0_diagram'
try:
    dot.render(file_path, cleanup=True)
    print(f"Generated diagram: {file_path}.png")
except Exception as e:
    print(f"Error generating diagram: {e}")
Generated diagram: dfd_level_0_diagram.png

[11]
import graphviz

# Create the Entity-Relationship Diagram
dot = graphviz.Digraph('er_diagram')
dot.attr(label='LMS - Entity-Relationship Diagram (Crow\'s Foot)', fontsize='20', fontname='Inter')
dot.node_attr.update(shape='record', fontname='Inter')
dot.edge_attr.update(fontname='Inter', dir='both') # 'both' allows arrowheads on both ends

# Define Entities (Tables) using HTML-like labels for structure
node_student = '''<
<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4">
  <TR><TD BGCOLOR="lightblue"><B>STUDENT</B></TD></TR>
  <TR><TD ALIGN="LEFT">studentID (PK)</TD></TR>
  <TR><TD ALIGN="LEFT">name</TD></TR>
  <TR><TD ALIGN="LEFT">email</TD></TR>
</TABLE>>'''

node_material = '''<
<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4">
  <TR><TD BGCOLOR="lightblue"><B>MATERIAL</B></TD></TR>
  <TR><TD ALIGN="LEFT">rfidTag (PK)</TD></TR>
  <TR><TD ALIGN="LEFT">title</TD></TR>
  <TR><TD ALIGN="LEFT">author</TD></TR>
  <TR><TD ALIGN="LEFT">publisher</TD></TR>
  <TR><TD ALIGN="LEFT">publicationDate</TD></TR>
  <TR><TD ALIGN="LEFT">materialType (FK)</TD></TR>
  <TR><TD ALIGN="LEFT">subject</TD></TR>
  <TR><TD ALIGN="LEFT">cost</TD></TR>
  <TR><TD ALIGN="LEFT">purchaseDate</TD></TR>
  <TR><TD ALIGN="LEFT">status</TD></TR>
</TABLE>>'''

node_rule = '''<
<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4">
  <TR><TD BGCOLOR="lightblue"><B>ISSUANCE_RULE</B></TD></TR>
  <TR><TD ALIGN="LEFT">materialType (PK)</TD></TR>
  <TR><TD ALIGN="LEFT">issuePeriodDays</TD></TR>
  <TR><TD ALIGN="LEFT">canBeIssued</TD></TR>
</TABLE>>'''

node_loan = '''<
<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4">
  <TR><TD BGCOLOR="lightblue"><B>LOAN</B></TD></TR>
  <TR><TD ALIGN="LEFT">loanID (PK)</TD></TR>
  <TR><TD ALIGN="LEFT">rfidTag (FK)</TD></TR>
  <TR><TD ALIGN="LEFT">studentID (FK)</TD></TR>
  <TR><TD ALIGN="LEFT">issueDate</TD></TR>
  <TR><TD ALIGN="LEFT">returnDate</TD></TR>
  <TR><TD ALIGN="LEFT">actualReturnDate</TD></TR>
</TABLE>>'''

node_fine = '''<
<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4">
  <TR><TD BGCOLOR="lightblue"><B>FINE</B></TD></TR>
  <TR><TD ALIGN="LEFT">fineID (PK)</TD></TR>
  <TR><TD ALIGN="LEFT">loanID (FK)</TD></TR>
  <TR><TD ALIGN="LEFT">studentID (FK)</TD></TR>
  <TR><TD ALIGN="LEFT">amount</TD></TR>
  <TR><TD ALIGN_LEFT">status (Pending/Paid)</TD></TR>
</TABLE>>'''

# Add nodes to the graph
dot.node('STUDENT', label=node_student)
dot.node('MATERIAL', label=node_material)
dot.node('ISSUANCE_RULE', label=node_rule)
dot.node('LOAN', label=node_loan)
dot.node('FINE', label=node_fine)

# Define Relationships with Crow's Foot Notation
# Key: arrowhead=none (One), odot (Zero), crow (Many)
#      arrowtail=... (Same as arrowhead)

# STUDENT (1) -- (0,M) LOAN
dot.edge('STUDENT', 'LOAN',
         arrowhead='crowodot', # Zero or Many (o{)
         arrowtail='none',     # One (|)
         label=' has')

# STUDENT (1) -- (0,M) FINE
dot.edge('STUDENT', 'FINE',
         arrowhead='crowodot', # Zero or Many (o{)
         arrowtail='none',     # One (|)
         label=' owes')

# MATERIAL (1) -- (0,M) LOAN
dot.edge('MATERIAL', 'LOAN',
         arrowhead='crowodot', # Zero or Many (o{)
         arrowtail='none',     # One (|)
         label=' is on')

# MATERIAL (M) -- (1) ISSUANCE_RULE
dot.edge('ISSUANCE_RULE', 'MATERIAL',
         arrowhead='crow',     # Many (})
         arrowtail='none',     # One (|)
         label=' governs')

# LOAN (1) -- (0,1) FINE
dot.edge('LOAN', 'FINE',
         arrowhead='odot',     # Zero or One (o|)
         arrowtail='none',     # One (|)
         label=' results in')

# Render the graph
dot.format = 'png'
file_path = 'er_diagram'
try:
    dot.render(file_path, cleanup=True)
    print(f"Generated diagram: {file_path}.png")
except Exception as e:
    print(f"Error generating diagram: {e}")
Error: not well-formed (invalid token) in line 1 
... <TR><TD ALIGN_LEFT"> ...
in label of node FINE
Error generating diagram: Command '[PosixPath('dot'), '-Kdot', '-Tpng', '-O', 'er_diagram']' returned non-zero exit status 1. [stderr: b'Error: not well-formed (invalid token) in line 1 \n... <TR><TD ALIGN_LEFT"> ...\nin label of node FINE\n']

[8]
0s
import graphviz

dot = graphviz.Digraph('use_case_diagram')
dot.attr(label='LMS Scope - Use Case Diagram', fontsize='20', fontname='Inter')
dot.attr(rankdir='LR', splines='ortho')  # Cleaner straight lines

# ----- Actors (Left side) -----
dot.attr('node', shape='none', fontname='Inter')

dot.node('A1', '👤 Student')
dot.node('A2', '👤 Library Staff')
dot.node('A3', '👤 Management')

# External systems (Right side)
dot.node('A4', 'RFID Gate', shape='box', style='filled', color='lightgrey')
dot.node('A5', 'Book Drop Box', shape='box', style='filled', color='lightgrey')
dot.node('A6', 'Email System', shape='box', style='filled', color='lightgrey')

# ----- System Boundary -----
with dot.subgraph(name='cluster_System') as c:
    c.attr(label='Stanford Library Management System (LMS)', color='blue')
    c.attr(style='rounded')
    c.node_attr.update(shape='ellipse', style='filled', color='white', fontname='Inter')

    c.node('UC1', 'Manage Materials')
    c.node('UC2', 'Checkout Material')
    c.node('UC3', 'Return Material (Counter)')
    c.node('UC4', 'Return Material (Book Drop)')
    c.node('UC5', 'Manage Fines')
    c.node('UC6', 'Search Catalogue')
    c.node('UC7', 'Generate Reports')
    c.node('UC8', 'Access Digital Resources')
    c.node('UC9', 'Check Loan Status Online')
    c.node('UC10', 'Send Email Notifications')
    c.node('UC11', 'Trigger Anti-Theft Alarm')

# ----- Actor → Use Case Edges -----
# Students
dot.edge('A1', 'UC6')
dot.edge('A1', 'UC8')
dot.edge('A1', 'UC9')
dot.edge('A1', 'UC2')
dot.edge('A1', 'UC3')
dot.edge('A1', 'UC4')

# Staff
dot.edge('A2', 'UC1')
dot.edge('A2', 'UC2')
dot.edge('A2', 'UC3')
dot.edge('A2', 'UC5')
dot.edge('A2', 'UC6')
dot.edge('A2', 'UC11')

# Management
dot.edge('A3', 'UC7')

# External systems
dot.edge('A5', 'UC4')
dot.edge('A4', 'UC11')
dot.edge('UC10', 'A6')
dot.edge('UC10', 'A1')

# ----- Output -----
dot.format = 'png'
dot.render('use_case_diagram', cleanup=True)
print("Generated diagram: use_case_diagram.png")

Generated diagram: use_case_diagram.png

[9]
0s
import graphviz

dot = graphviz.Digraph('dfd_level_0')

dot.attr(
    label='LMS - Data Flow Diagram (Level 0)',
    fontsize='22',
    fontname='Inter',
    rankdir='TB',
    splines='ortho',          # 🟢 Straight clean lines
    nodesep='1.0',
    ranksep='1.2'
)

dot.node_attr.update(fontname='Inter')
dot.edge_attr.update(fontname='Inter')

# ---- TOP RANK (External Entities) ----
with dot.subgraph() as top:
    top.attr(rank='same')
    top.node('E1', 'Student', shape='box', style='filled', color='lightgrey')
    top.node('E2', 'Library Staff', shape='box', style='filled', color='lightgrey')
    top.node('E3', 'Management', shape='box', style='filled', color='lightgrey')


# ---- CENTRAL PROCESS ----
dot.node('P1', 'Library\nManagement\nSystem', shape='circle', style='filled', color='lightblue', width='2')

# ---- BOTTOM RANK (External Systems) ----
with dot.subgraph() as bottom:
    bottom.attr(rank='same')
    bottom.node('E4', 'RFID Hardware\n(Scanners / Gates / Drop Box)', shape='box', style='filled', color='lightgrey')
    bottom.node('E5', 'Email System', shape='box', style='filled', color='lightgrey')


# ---------------- DATA FLOWS ----------------

# Inputs to LMS
dot.edge('E1', 'P1', label='Student ID\nSearch Request\nDigital Request')
dot.edge('E2', 'P1', label='Staff Login\nMaterial Entry\nSearch Query')
dot.edge('E3', 'P1', label='Mgmt Login\nReport Request')
dot.edge('E4', 'P1', label='RFID Events')

# Outputs
dot.edge('P1', 'E1', label='Loan Status\nDigital Content\nSearch Results')
dot.edge('P1', 'E2', label='Search Results\nFine Data\nAlarm Alerts')
dot.edge('P1', 'E3', label='Reports')
dot.edge('P1', 'E4', label='Alarm Signal')
dot.edge('P1', 'E5', label='Email Content')

# ---- Export ----
dot.format = 'png'
file_path = 'dfd_level_0_diagram'

try:
    dot.render(file_path, cleanup=True)
    print(f"Generated: {file_path}.png")
except Exception as e:
    print(f"Error: {e}")

Warning: Orthogonal edges do not currently handle edge labels. Try using xlabels.
Generated: dfd_level_0_diagram.png

[18]
0s
import graphviz

dot = graphviz.Digraph('dfd_level_0')
dot.attr(label='LMS - Data Flow Diagram (Level 0)', fontsize='20', fontname='Inter', rankdir='TB')
dot.node_attr.update(fontname='Inter')
dot.edge_attr.update(fontname='Inter')

# 1. Central Process
dot.node('P1', 'Library Management System', shape='circle', style='filled', color='lightblue')

# 2. External Entities
dot.node('E1', 'Student', shape='box', style='filled', color='lightgrey')
dot.node('E2', 'Library Staff', shape='box', style='filled', color='lightgrey')
dot.node('E3', 'Management', shape='box', style='filled', color='lightgrey')
dot.node('E4', 'RFID Hardware\n(Scanners, Gates, Book Drop)', shape='box', style='filled', color='lightgrey')
dot.node('E5', 'Email System', shape='box', style='filled', color='lightgrey')

# -------------------
# INPUT DATA FLOWS
# -------------------
dot.edge('E1', 'P1', label='Student ID, Search Query, Digital Content Request')
dot.edge('E2', 'P1', label='Staff Login, New Material Data, Search Query')
dot.edge('E3', 'P1', label='Management Login, Report Request')
dot.edge('E4', 'P1', label='RFID Tag Data, Return Confirmation')

# -------------------
# OUTPUT DATA FLOWS
# -------------------
dot.edge('P1', 'E1', label='Loan Status, Search Results, Digital Content, Due Date')
dot.edge('P1', 'E2', label='Search Results, Fine Details, Alarm Trigger')
dot.edge('P1', 'E3', label='Generated Reports')
dot.edge('P1', 'E4', label='Alarm Trigger Signal')
dot.edge('P1', 'E5', label='Reminder/Fine Email Content')

# Render
dot.format = 'png'
file_path = 'dfd_level_0_diagram'

try:
    dot.render(file_path, cleanup=True)
    print(f"Generated diagram: {file_path}.png")
except Exception as e:
    print(f"Error generating diagram: {e}")

Generated diagram: dfd_level_0_diagram.png

[20]
0s
dot.edge('STUDENT', 'FINE', label='(1) to (0,M)', arrowhead='crow')
dot.edge('MATERIAL', 'LOAN', label='(1) to (0,M)', arrowhead='crow')
dot.edge('ISSUANCE_RULE', 'MATERIAL', label='(1) to (M)', arrowhead='crow')
dot.edge('LOAN', 'FINE', label='(1) to (0,1)', arrowhead='odot')

# Render
dot.format = 'png'
file_path = 'er_diagram'
try:
    dot.render(file_path, cleanup=True)

Generated diagram: er_diagram.png
Colab paid products - Cancel contracts here