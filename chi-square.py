
#Chi-Square Test of Independence

import numpy as np
from scipy.stats import chi2_contingency

data = np.array([[10, 20, 30], 
                 [6,  9,  17]]) 


chi2_stat, p_value, dof, expected = chi2_contingency(data)

print(f"Chi-Square Statistic: {chi2_stat}")
print(f"P-value: {p_value}")
print(f"Degrees of Freedom: {dof}")
print("Expected Frequencies:")
print(expected)

