import pandas as pd
import numpy as np

# Load dataset
data = pd.read_csv('2.csv', header=None)
concept = np.array(data)
target = np.array(['yes', 'yes', 'no', 'yes'])

def learn(concept, target):
    specific_h = concept[0].copy()
    print("Initial Specific Hypothesis:", specific_h)

    general_h = [['?' for _ in specific_h] for _ in specific_h]
    print("Initial General Hypothesis:", general_h)

    for i, h in enumerate(concept):
        if target[i] == 'yes':
            for x in range(len(specific_h)):
                if h[x] != specific_h[x]:
                    specific_h[x] = '?'
                    general_h[x][x] = '?'
        elif target[i] == 'no':
            for x in range(len(specific_h)):
                if h[x] != specific_h[x]:
                    general_h[x][x] = specific_h[x]
                else:
                    general_h[x][x] = '?'

        print(f"\nIteration {i + 1}:")
        print("Specific Hypothesis:", specific_h)
        print("General Hypothesis:", general_h)

    # Remove overly general hypotheses
    indices = [i for i, val in enumerate(general_h) if val == ['?', '?', '?', '?', '?', '?']]
    for i in indices:
        general_h.remove(['?', '?', '?', '?', '?', '?'])


    return specific_h, general_h

# Run the Candidate Elimination Algorithm
specific_h, general_h = learn(concept, target)

print("\nFinal Specific Hypothesis:", specific_h)
print("Final General Hypothesis:", general_h)

Sunny,Warm,Normal,Strong,Warm,Same
Sunny,Warm,High,Strong,Warm,Same
Rainy,Cold,High,Strong,Warm,Change
Sunny,Warm,High,Strong,Cool,Change
