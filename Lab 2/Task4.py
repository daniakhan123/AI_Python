import random

# Define system components
components = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
vulnerability_levels = ['Safe', 'Low Risk Vulnerable', 'High Risk Vulnerable']

# Initialize system with random vulnerabilities
system_state = {comp: random.choice(vulnerability_levels) for comp in components}

def display_system_state(state, message):
    print(f"\n{message}")
    for comp, status in state.items():
        print(f"Component {comp}: {status}")

def scan_system(state):
    print("\nSystem Scan:")
    for comp, status in state.items():
        if status == 'Safe':
            print(f"[SUCCESS] Component {comp} is Safe.")
        else:
            print(f"[WARNING] Component {comp} has a {status}.")

def patch_system(state):
    print("\nPatching Vulnerabilities:")
    for comp, status in state.items():
        if status == 'Low Risk Vulnerable':
            state[comp] = 'Safe'
            print(f"[PATCHED] Component {comp} - Low Risk Vulnerability patched.")
        elif status == 'High Risk Vulnerable':
            print(f"[UNPATCHED] Component {comp} - High Risk Vulnerability detected. Premium service required.")

# Run the simulation
display_system_state(system_state, "Initial System State:")
scan_system(system_state)
patch_system(system_state)
display_system_state(system_state, "Final System State:")

