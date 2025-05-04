
from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Step 1: Define model structure (simplified)
model = DiscreteBayesianNetwork([('Color', 'Suit'), ('FaceCard', 'Suit')])  # Changed structure

# Step 2: Define CPDs (fixed)
cpd_color = TabularCPD(
    variable='Color',
    variable_card=2,
    values=[[0.5], [0.5]],
    state_names={'Color': ['Red', 'Black']}
)

cpd_face = TabularCPD(
    variable='FaceCard',
    variable_card=2,
    values=[[40/52], [12/52]],
    state_names={'FaceCard': ['No', 'Yes']}
)


cpd_suit = TabularCPD(
    variable='Suit',
    variable_card=4,
    values=[
                 
        [0.25, 0.25, 0.25, 0.25],  
        [0.25, 0.25, 0.25, 0.25],  
        [0.25, 0.25, 0.25, 0.25],  
        [0.25, 0.25, 0.25, 0.25]   
    ],
    evidence=['Color', 'FaceCard'],  
    evidence_card=[2, 2],
    state_names={
        'Suit': ['Hearts', 'Diamonds', 'Clubs', 'Spades'],
        'Color': ['Red', 'Black'],
        'FaceCard': ['No', 'Yes']
    }
)

model.add_cpds(cpd_color, cpd_face, cpd_suit)

# Step 3: Validate model
try:
    assert model.check_model()
    print("Model is valid!")
except AssertionError as e:
    print(f"Model invalid: {e}")


inference = VariableElimination(model)


result = inference.query(variables=['Suit'], evidence={'Color': 'Red'})
print("\nP(Suit | Color=Red):\n", result)

result = inference.query(variables=['Suit'], evidence={'FaceCard': 'Yes'})
print("\nP(Suit | FaceCard=Yes):\n", result)
