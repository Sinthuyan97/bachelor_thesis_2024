import numpy as np
import matplotlib.pyplot as plt

def calculate_gini_coefficient(balances):
    """Calculate the Gini coefficient from a list of balances."""
    # Sort balances in ascending order
    sorted_balances = np.sort(balances)
    n = len(sorted_balances)
    cumulative_total = np.cumsum(sorted_balances)
    lorenz_curve = cumulative_total / cumulative_total[-1]
    
    # Compute area under the Lorenz Curve using the trapezoidal rule
    area_under_lorenz = np.trapz(lorenz_curve, dx=1/n)
    gini_coefficient = 1 - 2 * area_under_lorenz
    return gini_coefficient

def plot_lorenz_curve(balances):
    """Plot the Lorenz curve from a list of balances."""
    sorted_balances = np.sort(balances)
    n = len(sorted_balances)
    cumulative_total = np.cumsum(sorted_balances)
    lorenz_curve = cumulative_total / cumulative_total[-1]
    
    # Set up the figure and axis
    plt.figure(figsize=(10, 6))
    ax = plt.gca()
    
    # Plot the Lorenz curve
    x = np.linspace(0, 100, n)  # Convert fraction to percentage
    plt.plot(x, lorenz_curve * 100, label='Lorenz Curve', color='blue', linewidth=2.5)
    
    # Plot the line of equality
    plt.plot([0, 100], [0, 100], linestyle='--', color='darkred', label='Line of Equality')
    
    # Fill the area under the Lorenz curve
    plt.fill_between(x, lorenz_curve * 100, x, color='skyblue', alpha=0.5)
    
    # Add labels and title
    plt.title('Lorenz Curve for Wealth Distribution', fontsize=16)
    plt.xlabel('Cumulative Share of Addresses (%)', fontsize=14)
    plt.ylabel('Cumulative Share of Wealth (%)', fontsize=14)
    
    # Add a grid for better readability
    plt.grid(True, linestyle='--', alpha=0.5)
    
    # Add a legend
    plt.legend(fontsize=12)

    # Show the plot
    plt.show()

# Example balances from a hypothetical blockchain dataset
balances = np.array([1000, 3000, 6000, 9000, 21000])

# Plot the Lorenz Curve
plot_lorenz_curve(balances)