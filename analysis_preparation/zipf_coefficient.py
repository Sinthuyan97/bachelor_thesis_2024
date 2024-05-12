import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def zipf_law(r, C, s):
    """ Zipf's law function (f = C / r^s) for curve fitting. """
    return C / (r**s)

def fit_zipf_law(balances):
    """ Fit Zipf's law to the balances and plot the distribution. """
    sorted_balances = np.sort(balances)[::-1]  # Sort descending
    ranks = np.arange(1, len(sorted_balances) + 1)

    # Perform curve fitting
    params, params_covariance = curve_fit(zipf_law, ranks, sorted_balances, p0=[1, 1])

    # Plotting the balances on a log-log scale
    plt.figure(figsize=(10, 6))
    plt.loglog(ranks, sorted_balances, 'bo', label='Data (Balances)')
    plt.loglog(ranks, zipf_law(ranks, params[0], params[1]), 'r-', label=f'Fit: C={params[0]:.2f}, s={params[1]:.2f}')

    plt.title('Zipf\'s Law Fit to Blockchain Balances', fontsize=16)
    plt.xlabel('Rank (log scale)', fontsize=14)
    plt.ylabel('Balance (log scale)', fontsize=14)
    plt.legend()
    plt.grid(True, which="both", ls="--", alpha=0.5)
    plt.show()

    return params

# Example balances from a hypothetical blockchain dataset
balances = np.array([1000, 3000, 6000, 9000, 21000])

# Fit Zipf's law and plot the results
zipf_params = fit_zipf_law(balances)
print(f"Estimated Zipf Coefficient (s): {zipf_params[1]:.2f}")