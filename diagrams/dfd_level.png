# data flow daigram -----------------------------------------------------------------------------------------------------------------------

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
