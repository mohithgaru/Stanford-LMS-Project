 use case daigram code ---------------------------------------------------------------------------------------------------------------------------

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


# Data Flow Daigram Code
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