import random
from scipy.stats import kstest

random_numbers = [random.random() for _ in range(1000)] 

ks_statistic, p_value = kstest(random_numbers, 'uniform')


print(f"KS Statistic: {ks_statistic}")
print(f"P-value: {p_value}")

if p_value > 0.05:
    print("The random numbers are uniformly distributed (fail to reject the null hypothesis).")
else:
    print("The random numbers are not uniformly distributed (reject the null hypothesis).")


# import numpy as np
# from scipy.stats import norm, kstest

# np.random.seed(42)
# sample_size = 100
# mean = 0
# std_dev = 1
# sample = np.random.normal(mean, std_dev, sample_size)

# def empirical_distribution_function(x, data):
# 	return np.sum(data <= x) / len(data)
# edf_values = [empirical_distribution_function(x, sample) for x in sample]

# reference_cdf = norm.cdf(sample)

# ks_statistic, ks_p_value = kstest(sample, 'norm')

# alpha = 0.05
# critical_value = 1.36 

# print(f"Kolmogorov-Smirnov Statistic: {ks_statistic}")
# print(f"P-value: {ks_p_value}")

# if ks_statistic > critical_value or ks_p_value < alpha:
# 	print("Reject the null hypothesis. The sample does not come from the specified distribution.")
# else:
# 	print("Fail to reject the null hypothesis. The sample comes from the specified distribution.")
