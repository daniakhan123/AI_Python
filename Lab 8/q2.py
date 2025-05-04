from pgmpy.models import DiscreteBayesianNetwork as BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
# Step 1: Define the structure of the Bayesian Network
# G edges: (I, G), (S, G), (D, G), (G, P)
model = DiscreteBayesianNetwork([
    ('Intelligence', 'Grade'),
    ('StudyHours', 'Grade'),
    ('Difficulty', 'Grade'),
    ('Grade', 'Pass')
])

# Step 2: Define the CPDs (Conditional Probability Distributions)

# Prior probabilities
cpd_intelligence = TabularCPD(
    variable='Intelligence', variable_card=2,
    values=[[0.7], [0.3]],
    state_names={'Intelligence': ['High', 'Low']}
)

cpd_studyhours = TabularCPD(
    variable='StudyHours', variable_card=2,
    values=[[0.6], [0.4]],
    state_names={'StudyHours': ['Sufficient', 'Insufficient']}
)

cpd_difficulty = TabularCPD(
    variable='Difficulty', variable_card=2,
    values=[[0.4], [0.6]],
    state_names={'Difficulty': ['Hard', 'Easy']}
)

# Grade depends on Intelligence, StudyHours, Difficulty
cpd_grade = TabularCPD(
    variable='Grade', variable_card=3,
    # Order of evidence: I, S, D => 2x2x2 = 8 rows of conditions
    values=[
        # P(G=A)
        [0.9, 0.7, 0.7, 0.6, 0.6, 0.5, 0.4, 0.3],
        # P(G=B)
        [0.08, 0.2, 0.2, 0.3, 0.3, 0.3, 0.4, 0.4],
        # P(G=C)
        [0.02, 0.1, 0.1, 0.1, 0.1, 0.2, 0.2, 0.3],
    ],
    evidence=['Intelligence', 'StudyHours', 'Difficulty'],
    evidence_card=[2, 2, 2],
    state_names={
        'Grade': ['A', 'B', 'C'],
        'Intelligence': ['High', 'Low'],
        'StudyHours': ['Sufficient', 'Insufficient'],
        'Difficulty': ['Hard', 'Easy']
    }
)

# Pass depends on Grade
cpd_pass = TabularCPD(
    variable='Pass', variable_card=2,
    values=[
        [0.95, 0.80, 0.50],  # P(Pass=Yes | Grade)
        [0.05, 0.20, 0.50],  # P(Pass=No  | Grade)
    ],
    evidence=['Grade'],
    evidence_card=[3],
    state_names={
        'Pass': ['Yes', 'No'],
        'Grade': ['A', 'B', 'C']
    }
)

# Step 3: Add CPDs to the model
model.add_cpds(cpd_intelligence, cpd_studyhours, cpd_difficulty, cpd_grade, cpd_pass)

# Validate the model
assert model.check_model()

# Step 4: Inference
inference = VariableElimination(model)

# Query 1: P(Pass | StudyHours=Sufficient, Difficulty=Hard)
q1 = inference.query(variables=['Pass'], evidence={'StudyHours': 'Sufficient', 'Difficulty': 'Hard'})
print("P(Pass | StudyHours=Sufficient, Difficulty=Hard):")
print(q1)

# Query 2: P(Intelligence=High | Pass=Yes)
q2 = inference.query(variables=['Intelligence'], evidence={'Pass': 'Yes'})
print("\nP(Intelligence=High | Pass=Yes):")
print(q2)
