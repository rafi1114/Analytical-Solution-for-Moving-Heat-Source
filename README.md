## Heat Transfer Model

The temperature at time \( t \) is given by:

\[
T(t) - T_0 = \frac{2 \eta Q}{\rho c (\pi / 3)^{3/2}} \int_0^t \frac{1}{\sqrt{\phi_x \phi_y \phi_z}} \exp \left( -3 \left( \frac{x^2}{\phi_x} + \frac{y^2}{\phi_y} + \frac{z^2}{\phi_z} \right) \right) dt'
\]

where:

\[
\phi_i = 12 \alpha (t - t') + \sigma_i^2, \quad \text{for} \quad i = x, y, z
\]

and:

- \( T(t) \) is the temperature at time \( t \),
- \( T_0 \) is the initial preheat temperature,
- \( Q \) is the beam power,
- \( \eta \) is the absorption efficiency,
- \( \rho \) is the material density,
- \( c \) is the specific heat capacity,
- \( \alpha = k / (\rho c) \) is the thermal diffusivity,
- \( \sigma_x, \sigma_y, \sigma_z \) are the beam width parameters.

This equation represents the heat diffusion from a moving **Gaussian** heat source, integrated over time using Rieman Sum.
