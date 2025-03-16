## Analytical Solution in Python for Moving Heat Source

The temperature at time **t** is given by:

T(t) - T₀ = (2 η Q) / (ρ c (π / 3)^(3/2)) * ∫[0 to t] (1 / sqrt(φₓ φᵧ φ_z)) * exp(-3 * (x² / φₓ + y² / φᵧ + z² / φ_z)) dt'

where, 

φᵢ = 12 α (t - t') + σᵢ², for i = x, y, z


with:

- **T(t)** = temperature at time **t**
- **T₀** = initial preheat temperature
- **Q** = beam power
- **η** = absorption efficiency
- **ρ** = material density
- **c** = specific heat capacity
- **α** = thermal diffusivity (k / (ρ c))
- **σₓ, σᵧ, σ_z** = beam width parameters
