# Butler-Volmer Equation Demonstration

This application visualizes the Butler-Volmer equation, showing the relationship between the reaction rate (or current density) and electrode potential. It now includes the functionality to consider the effects of a limiting current density, which can be indicative of concentration overpotential due to mass transport limitations.

## Overview

The Butler-Volmer equation is central to the description of the kinetics of electrode reactions. This application allows users to explore the impact of various electrochemical parameters on the reaction rate. Users can adjust parameters such as the exchange current density (i0), temperature (T), number of electrons transferred in the reaction (n), charge transfer coefficients (alpha_a and alpha_c), and the limiting current density (i_lim) when mass transport limitations are significant.

The plots provide a visual representation of the relationship between the anodic and cathodic currents and the electrode potential, allowing users to gain insight into the electrochemical behavior under different conditions.

## Features

- Interactive sliders to adjust electrochemical parameters, including the option to consider a limiting current density (i_lim).
- Visualization of the Butler-Volmer equation results on two scales:
  - Linear Scale
  - Logarithmic Scale
- Display of anodic (i_a) and cathodic (i_c) currents as separate dotted lines.
- Calculation and display of Tafel slopes for both anodic and cathodic reactions.
- Option to toggle the inclusion of the limiting current density, reflecting concentration overpotentials.

## Usage

The application interface is intuitive, with sliders and checkboxes that allow for the dynamic adjustment of parameters. By toggling the checkbox for the limiting current density, users can observe the transition from activation-controlled to mass transport-controlled kinetics.

## Contributing

Contributions to the project are welcome. For substantial changes or enhancements, please open an issue first to discuss your ideas. This ensures a collaborative and inclusive approach to improving the application.

## License

This project is covered under the MIT License.
