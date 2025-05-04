from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Step 1: Define the structure of the Bayesian Network
# Disease -> {Fever, Cough, Fatigue, Chills}
model = DiscreteBayesianNetwork([
    ('Disease', 'Fever'),
    ('Disease', 'Cough'),
    ('Disease', 'Fatigue'),
    ('Disease', 'Chills')
])

# Step 2: Define the CPDs (Conditional Probability Distributions)

# Prior probability for Disease
cpd_disease = TabularCPD(
    variable='Disease', variable_card=2,
    values=[[0.3], [0.7]],
    state_names={'Disease': ['Flu', 'Cold']}
)

# Fever depends on Disease
cpd_fever = TabularCPD(
    variable='Fever', variable_card=2,
    values=[
        [0.9, 0.5],  # P(Fever=Yes | Flu), P(Fever=Yes | Cold)
        [0.1, 0.5]   # P(Fever=No | Flu),  P(Fever=No | Cold)
    ],
    evidence=['Disease'],
    evidence_card=[2],
    state_names={
        'Fever': ['Yes', 'No'],
        'Disease': ['Flu', 'Cold']
    }
)

# Cough depends on Disease
cpd_cough = TabularCPD(
    variable='Cough', variable_card=2,
    values=[
        [0.8, 0.6],  # P(Cough=Yes | Flu), P(Cough=Yes | Cold)
        [0.2, 0.4]
    ],
    evidence=['Disease'],
    evidence_card=[2],
    state_names={
        'Cough': ['Yes', 'No'],
        'Disease': ['Flu', 'Cold']
    }
)

# Fatigue depends on Disease
cpd_fatigue = TabularCPD(
    variable='Fatigue', variable_card=2,
    values=[
        [0.7, 0.3],
        [0.3, 0.7]
    ],
    evidence=['Disease'],
    evidence_card=[2],
    state_names={
        'Fatigue': ['Yes', 'No'],
        'Disease': ['Flu', 'Cold']
    }
)

# Chills depends on Disease
cpd_chills = TabularCPD(
    variable='Chills', variable_card=2,
    values=[
        [0.6, 0.4],
        [0.4, 0.6]
    ],
    evidence=['Disease'],
    evidence_card=[2],
    state_names={
        'Chills': ['Yes', 'No'],
        'Disease': ['Flu', 'Cold']
    }
)

# Step 3: Add CPDs to the model
model.add_cpds(cpd_disease, cpd_fever, cpd_cough, cpd_fatigue, cpd_chills)

# Validate the model
assert model.check_model()

# Step 4: Inference
inference = VariableElimination(model)

# Task 1: P(Disease | Fever=Yes, Cough=Yes)
print("Task 1: P(Disease | Fever=Yes, Cough=Yes)")
result1 = inference.query(variables=['Disease'], evidence={'Fever': 'Yes', 'Cough': 'Yes'})
print(result1)

# Task 2: P(Disease | Fever=Yes, Cough=Yes, Chills=Yes)
print("\nTask 2: P(Disease | Fever=Yes, Cough=Yes, Chills=Yes)")
result2 = inference.query(variables=['Disease'], evidence={'Fever': 'Yes', 'Cough': 'Yes', 'Chills': 'Yes'})
print(result2)

# Task 3: P(Fatigue=Yes | Disease=Flu)
print("\nTask 3: P(Fatigue=Yes | Disease=Flu)")
result3 = inference.query(variables=['Fatigue'], evidence={'Disease': 'Flu'})
print(result3)
