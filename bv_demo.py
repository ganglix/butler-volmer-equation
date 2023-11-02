import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Constants
R = 8.314  # J/(mol K)
F = 96485.3329  # C/mol

def butler_volmer(eta, i0, alpha_a, alpha_c, n, T, ilim):
    """Compute the Butler-Volmer equation for a given overpotential including a limiting current density"""
    ia = i0 * np.exp(alpha_a * n * F * eta / (R * T))
    ic = i0 * np.exp(-alpha_c * n * F * eta / (R * T))
    if ilim != np.inf:  # Apply limiting current density only if it's not infinity
        ic = ic / (1 + ic/ilim)
    return ia - ic, ia, ic

def tafel_slope(alpha, n, T):
    """Compute the Tafel slope."""
    return (2.303 * R * T) / (alpha * n * F)

def main():
    st.title('Butler-Volmer Equation Demonstration')

    st.write("""
    This app demonstrates the Butler-Volmer equation, which describes the relationship between reaction rate (or current density) and electrode potential. 
    Use the sidebar to adjust the parameters including the limiting current density, and observe the changes in the graph.
    """)


    # Input parameters in the sidebar
    i0 = st.sidebar.slider('Exchange current density (i0) [A/m^2]', 0.01, 100.0, 1.0)
    T = st.sidebar.slider('Temperature (T) [K]', 200, 1000, 300)
    n = st.sidebar.slider('Number of electrons (n)', 1, 5, 1)
    alpha_a = st.sidebar.slider('Anodic charge transfer coefficient (alpha_a)', 0.1, 1.0, 0.5)
    st.sidebar.text(f'Tafel Slope (anodic): {tafel_slope(alpha_a, n, T):.2f} V/dec')
    alpha_c = st.sidebar.slider('Cathodic charge transfer coefficient (alpha_c)', 0.1, 1.0, 0.5)
    st.sidebar.text(f'Tafel Slope (cathodic): {tafel_slope(alpha_c, n, T):.2f} V/dec')
    eta_min, eta_max = st.sidebar.slider('Overpotential range (eta) [V]', -1.0, 1.0, (-0.25, 0.25), 0.01)

    use_ilim = st.sidebar.checkbox('Use limiting current density (i_lim)', value=False)

    if use_ilim:
        ilim = st.sidebar.slider('Limiting current density (i_lim) [A/m^2]', 0.01, 10.0, 1.0)
    else:
        ilim = np.inf  # Assign a very large number to ilim when the checkbox is not checked


    # Generate potential values
    eta = np.linspace(eta_min, eta_max, 1000)
    i, ia, ic = butler_volmer(eta, i0, alpha_a, alpha_c, n, T, ilim)

    # Plot figures
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    # Linear scale
    ax1.plot(i, eta, 'C2-', label='Butler-Volmer')
    ax1.plot(ia, eta, 'C1--', linewidth=2, label='$i_a$ (Anodic)')  # LaTeX-style label and thicker line
    ax1.plot(-ic, eta, 'C0--', linewidth=2, label='$i_c$ (Cathodic)')  # Thicker line
    ax1.set_xlim(-i0*100, i0*100)  # This line limits the x-axis range
    ax1.set_title('Linear Scale')
    ax1.set_xlabel('Current Density (A/m^2)')
    ax1.set_ylabel('Potential (V)')
    ax1.legend()

    # Logarithmic scale
    ax2.plot(np.abs(i), eta, 'C2-',label='Butler-Volmer')
    ax2.plot(np.abs(ia), eta, 'C1--', linewidth=2, label='$i_a$ (Anodic)')  # LaTeX-style label and thicker line
    ax2.plot(np.abs(ic), eta, 'C0--', linewidth=2, label='$i_c$ (Cathodic)')  # Thicker line
    ax2.set_xlim(i0/1000, max(np.abs(i)))  # This line limits the x-axis range
    ax2.set_xscale('log')
    ax2.set_title('Logarithmic Scale')
    ax2.set_xlabel('Current Density (A/m^2)')
    ax2.set_ylabel('Potential (V)')
    ax2.legend()

    plt.tight_layout()
    st.pyplot(fig)


    st.write("""
    The relationship between the currents in the Butler-Volmer equation can be described as:

    \[
    i = i_a + i_c
    \]

    where \( i \) is the total current, \( i_a \) is the anodic (positive) current, and \( i_c \) is the cathodic (negative) current.

    In the logarithmic scale plot, the cathodic current \( i_c \) is plotted as \( |i_c| \) to account for its negative value.
    """)

if __name__ == '__main__':
    main()
