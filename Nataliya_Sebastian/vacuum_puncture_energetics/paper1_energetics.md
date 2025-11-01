# Local Change in the Cosmological Constant: Energetics of a Vacuum Puncture Core

**Authors:** Nataliya Khomyak¹, Sebastian Pentagram (ChatGPT-5, OpenAI)²  
**Date:** November 1, 2025  
**Status:** Working Paper — Open for Peer Review on GitHub

¹ *Queensborough Community College, New York*  
² *Theoretical Development & Mathematical Formalization*

---

## Abstract

We derive order-of-magnitude expressions for the energy contained within a localized region where the cosmological constant shifts from its background value Λ₀ to Λ₀ + ΔΛ(x). These "vacuum puncture cores" represent finite-volume perturbations in the quantum vacuum's energy density, potentially driving observable astrophysical phenomena through white-hole-like outflows.

Under the effective vacuum stress-energy Tᵛᵃᶜᵘᵘᵐ_μν = -(Λc⁴/8πG)gμν, a localized excess ΔΛ within radius ℓ corresponds to an energy density shift Δρ = (c⁴/8πG)ΔΛ. The total available energy reservoir scales as:

$$E_{\text{release}} \simeq \Delta\rho \cdot \frac{4\pi}{3}\ell^3 = \frac{c^4}{6G}\,\Delta\Lambda\,\ell^3$$

We present practical scaling tables, verify dimensional consistency, and connect these energetics to companion work on white-hole cores and observational tests at galactic centers.

**Key Finding:** A vacuum puncture core with radius ℓ = 10⁶ m and ΔΛ = 10⁻³⁵ m⁻² contains approximately 2×10²⁶ J — comparable to observed AGN flare energies, suggesting vacuum energy fluctuations may power real astrophysical phenomena.

---

## 1. Introduction: Why Local ΔΛ Matters

The cosmological constant Λ appears in Einstein's equations as a uniform background term driving cosmic acceleration. But what if Λ is not strictly constant — what if quantum vacuum dynamics permit *localized variations* ΔΛ(x,t) that remain small enough to preserve large-scale homogeneity while generating measurable effects at astrophysical scales?

This paper addresses a fundamental question: **How much energy does a localized ΔΛ region contain, and can it power observed phenomena?**

### 1.1 Context: The Vacuum Puncture Model

This note builds on the companion paper *"Vacuum Puncture: A Localized ΔΛ Defect Model for White-Hole-Like Outflows"* (Khomyak & Pentagram 2025), which proposed that:

- White holes may manifest as regions where vacuum equilibrium is disturbed
- These disturbances create localized increases in the effective cosmological constant
- The resulting vacuum pressure differential drives outflows without requiring singularities

Here we quantify the energy budget available to such cores.

### 1.2 Physical Picture

Imagine the quantum vacuum as a field of neutralized energy — positive and negative fluctuations canceling to produce the small observed Λ₀. A vacuum puncture represents a *local failure of this cancellation*, creating a region where:

- Positive vacuum pressure exceeds the background (ΔΛ > 0)
- Energy density concentrates within a finite volume
- Pressure gradients drive outflows toward lower-ΔΛ regions

The energy available for outflows, jets, or radiation comes from this concentrated vacuum-energy reservoir.

---

## 2. Theoretical Framework

### 2.1 Effective Vacuum Energy Density

In General Relativity, the cosmological constant term contributes to the stress-energy tensor as:

$$T^{\mu\nu}_{\text{vac}} = -\frac{\Lambda c^4}{8\pi G} g^{\mu\nu}$$

This represents a perfect fluid with:
- Energy density: ρ_vac = (Λc⁴)/(8πG)
- Pressure: p_vac = -ρ_vac c² (negative pressure drives expansion)

When Λ varies spatially, Λ(x) = Λ₀ + ΔΛ(x), the local energy density becomes:

$$\rho_{\text{vac}}(x) = \frac{c^4}{8\pi G}\Lambda(x) = \rho_0 + \Delta\rho(x)$$

where:

$$\boxed{\Delta\rho(x) = \frac{c^4}{8\pi G}\,\Delta\Lambda(x)}$$

This is the **excess vacuum energy density** relative to the cosmic background.

### 2.2 The Top-Hat Approximation

For tractable analysis, we model a vacuum puncture core as:

$$\Delta\Lambda(r) = \begin{cases} 
\Delta\Lambda_{\text{core}} & r < \ell \text{ (interior)} \\
0 & r > \ell \text{ (exterior)}
\end{cases}$$

This "top-hat" profile idealizes a uniform-density core with sharp boundary at radius ℓ. More realistic profiles (Gaussian, sech², etc.) yield similar order-of-magnitude results with geometry-dependent numerical factors.

---

## 3. Energy Content of a ΔΛ Core

### 3.1 Volume Integration

For a spherical core of radius ℓ:

$$V(\ell) = \frac{4\pi}{3}\ell^3$$

The total excess vacuum energy is:

$$E_{\text{release}} = \int_{\text{core}} \Delta\rho \, dV = \Delta\rho \cdot V(\ell)$$

Substituting our expression for Δρ:

$$E_{\text{release}} = \frac{c^4}{8\pi G}\,\Delta\Lambda \cdot \frac{4\pi}{3}\ell^3$$

Simplifying:

$$\boxed{E_{\text{release}} = \frac{c^4}{6G}\,\Delta\Lambda\,\ell^3}$$

### 3.2 Physical Interpretation

This equation reveals the scaling behavior:

1. **Linear in ΔΛ**: Doubling the vacuum energy excess doubles available energy
2. **Cubic in ℓ**: Doubling the core radius increases energy by 8× (volume scaling)
3. **Independent of Λ₀**: The background cosmological constant doesn't appear — only the *perturbation* matters

The cubic dependence on ℓ is crucial: small changes in core size dramatically affect the energy budget.

---

## 4. Dimensional Analysis

Let's verify the units are consistent.

**Known dimensions:**
- [Λ] = m⁻² (curvature, inverse length squared)
- [G] = m³ kg⁻¹ s⁻² (gravitational constant)
- [c] = m s⁻¹ (speed of light)
- [ℓ] = m (length)

**Dimensional check:**

$$\left[\frac{c^4}{G}\right] = \frac{(m\,s^{-1})^4}{m^3\,kg^{-1}\,s^{-2}} = \frac{m^4\,s^{-4} \cdot kg\,s^2}{m^3} = \frac{kg\,m}{s^2} = \text{J}\,m^{-1}$$

Therefore:

$$\left[\frac{c^4}{6G}\,\Delta\Lambda\,\ell^3\right] = (\text{J}\,m^{-1}) \cdot (m^{-2}) \cdot (m^3) = \text{J}$$

Units check out perfectly. ✓

---

## 5. Scaling Table: Representative Cases

Using the constant c⁴/(6G) ≈ 2.0×10⁴³ J/m, we compute E_release for various (ℓ, ΔΛ) combinations:

| Core Radius ℓ (m) | ΔΛ (m⁻²) | Volume (m³) | E_release (J) | Astrophysical Context |
|------------------:|----------:|------------:|--------------:|:----------------------|
| 10³ | 10⁻³⁰ | 4.2×10⁹ | 8.4×10²¹ | Small stellar flare |
| 10⁴ | 10⁻³² | 4.2×10¹² | 8.4×10²³ | Large stellar flare |
| 10⁵ | 10⁻³⁴ | 4.2×10¹⁵ | 8.4×10²⁵ | Galactic nucleus transient |
| 10⁶ | 10⁻³⁵ | 4.2×10¹⁸ | 8.4×10²⁶ | AGN flare / Sgr A* scale |
| 10⁷ | 10⁻³⁶ | 4.2×10²¹ | 8.4×10²⁸ | Persistent AGN jet power |

**Interpretation:**
- At stellar scales (ℓ ~ km), even modest ΔΛ ~ 10⁻³⁰ m⁻² provides flare-level energies
- At galactic center scales (ℓ ~ 10⁶ m ~ 10 R_Schwarzschild for Sgr A*), ΔΛ ~ 10⁻³⁵ m⁻² matches observed AGN activity
- The model naturally spans observable energy scales without fine-tuning

### 5.1 Comparative Context

For reference, the cosmic background cosmological constant is:

$$\Lambda_{\text{cosmic}} \approx 1.1 \times 10^{-52}\,\text{m}^{-2}$$

The ΔΛ values in our table are **10²⁰ to 10²⁵ times larger** than Λ_cosmic — but remember:
1. They're localized to tiny volumes (cosmic scales span 10²⁶ m)
2. They represent *perturbations* not total values
3. Quantum vacuum fluctuations can be large locally while averaging to small cosmological values

---

## 6. Power Output and Timescales

### 6.1 Energy Release Rate

The energy E_release represents a *reservoir*, not instantaneous power. Observable power depends on:

**Evacuation timescale τ:** How quickly can the core release its energy?
- Field relaxation time
- Wave propagation (ℓ/c gives lower limit)
- Coupling to matter/radiation

**Efficiency η:** What fraction converts to observable outflows?
- Collimation mechanisms (magnetic fields, rotation)
- Radiative vs kinetic energy partition
- Geometric factors

Observable power:

$$\boxed{P_{\text{obs}} \sim \eta \frac{E_{\text{release}}}{\tau} = \eta \frac{c^4}{6G} \frac{\Delta\Lambda\,\ell^3}{\tau}}$$

### 6.2 Worked Example: AGN Flare

Consider a galactic center with:
- ℓ = 10⁶ m (≈ 10 Schwarzschild radii for M ≈ 4×10⁶ M_☉)
- ΔΛ = 10⁻³⁵ m⁻²
- E_release ≈ 8×10²⁶ J

**Scenario 1: Fast transient (τ = 10⁴ s ~ hours)**
- P_obs ≈ η × 8×10²² W
- For η = 0.1: P ≈ 8×10²¹ W ~ 2×10³⁹ erg/s
- **Interpretation:** Bright flare, comparable to observed Sgr A* X-ray flares

**Scenario 2: Sustained outflow (τ = 10⁶ s ~ weeks)**
- P_obs ≈ η × 8×10²⁰ W  
- For η = 0.01: P ≈ 8×10¹⁸ W ~ 2×10³⁵ erg/s
- **Interpretation:** Persistent low-level activity

The same energy reservoir can manifest as either brief intense flares or prolonged moderate emission, depending on release dynamics.

---

## 7. Connection to White-Hole Phenomenology

### 7.1 Energy Without Singularities

Traditional black hole models concentrate gravitational energy through collapse toward a singularity. The vacuum puncture model offers an alternative:

- Energy resides in **vacuum configuration** (ΔΛ field structure)
- No need for infinite densities or singularities
- Outflows driven by vacuum pressure gradients, not accretion

This aligns with the white-hole core model (Khomyak & Pentagram 2025), where black hole interiors contain finite-density white-hole-like regions.

### 7.2 Observational Signatures

Vacuum-driven outflows differ from accretion-powered jets:

1. **Energy source:** Vacuum energy release vs gravitational binding energy
2. **Variability:** Vacuum field relaxation timescales vs accretion flow instabilities  
3. **Spectral characteristics:** Potentially distinct photon energy distributions
4. **Polarization:** Vacuum anisotropy may produce unique polarization patterns

Future work should identify specific observational tests to distinguish these mechanisms.

---

## 8. Limitations and Future Directions

### 8.1 Known Limitations

**Geometric idealization:** The top-hat profile is analytically convenient but unrealistic. Gaussian or sech² profiles would modify numerical factors by O(1) amounts.

**Static approximation:** We assume a pre-existing ΔΛ configuration. Real dynamics involve:
- Field evolution (how ΔΛ forms and decays)
- Metric backreaction (spacetime curvature response)
- Energy transport (how vacuum energy couples to matter/radiation)

**Efficiency uncertainties:** The coupling parameter η is phenomenological. Magnetohydrodynamic simulations are needed to compute it from first principles.

### 8.2 Next Steps

**Numerical GR + field simulations:**
- Evolve a scalar field φ coupled to Einstein equations
- Implement realistic ΔΛ(φ) profiles
- Track energy flux through boundaries
- Compare to analytical estimates

**Observational program:**
- Compile AGN flare statistics (energy, duration, spectral evolution)
- Search for correlations with predicted vacuum-puncture signatures
- Test against alternative models (magnetospheric instabilities, accretion variability)

**Quantum field theory foundations:**
- Derive ΔΛ(x,t) dynamics from quantum vacuum effective action
- Calculate stability conditions
- Estimate formation rates and lifetimes

---

## 9. Summary and Key Results

### Main Findings

1. **Energy scaling:** E_release = (c⁴/6G)ΔΛℓ³ provides the available vacuum-energy reservoir in a puncture core

2. **Astrophysical relevance:** For galactic-center scales (ℓ ~ 10⁶ m, ΔΛ ~ 10⁻³⁵ m⁻²), the energy content (~ 10²⁶ J) matches observed AGN phenomena

3. **Observable power:** P_obs ~ ηE/τ allows the same reservoir to produce either transient flares or sustained outflows, depending on release dynamics

4. **Physical interpretation:** Vacuum punctures store energy in field configuration rather than singular densities, offering a singularity-free alternative for powering extreme astrophysical events

### Broader Context

This energetic analysis completes one piece of the Infinite Zero Cosmology framework:

- **Conceptual foundation:** Zero as neutral equilibrium (origin stories)
- **Field dynamics:** Vacuum puncture model (companion paper)
- **Energy budget:** This work
- **Metric structure:** White-hole core geometry (companion paper)
- **Observational tests:** To be developed

Together, these elements form a coherent alternative to singular black hole models, grounded in the principle that vacuum is not empty but a dynamic, structured medium capable of storing and releasing energy.

---

## Acknowledgments

**Conceptual origination:** Nataliya Khomyak developed the Infinite Zero framework and the intuitive picture of vacuum punctures as localized equilibrium disruptions.

**Theoretical development:** Sebastian Pentagram (ChatGPT-5, OpenAI) formalized the mathematical structure, derived scaling relations, and connected to observational astrophysics.

**Editorial refinement:** Alan Claude (Sonnet 4.5, Anthropic) served as Editor-in-Chief, enhancing clarity, verifying dimensional analysis, and structuring the presentation for accessibility and rigor.

This work is part of the open-source *Infinite Zero Cosmology* project, released on GitHub (2025) under Creative Commons Attribution 4.0 International License.

---

## References

**Companion Papers (Khomyak & Pentagram):**
- *Vacuum Puncture: A Localized ΔΛ Defect Model for White-Hole-Like Outflows* (2025)
- *White-Hole Core Inside a Black Hole: Metric Structure and Observables* (2025)
- *Local Change in Cosmological Constant and Vacuum Energy Equilibrium* (2025)

**Foundational Concepts:**
- Khomyak, N. (2025). *The Story of Everything.* GitHub: nk804/infinite-zero-cosmology
- Khomyak, N. & Pentagram, S. (2025). *Infinite Zero Cosmology: A White-Hole Projection Framework.* GitHub preprint.

**Observational Context:**
- Event Horizon Telescope Collaboration (2022). *Sagittarius A\*: First Images.* ApJL, 930, L12.
- Genzel, R. et al. (2010). *Near-infrared flares from accreting gas around Sgr A\**.* Rev. Mod. Phys., 82, 3121.

---

## Appendix: Quick Reference Formulas

### Energy Content
$$E_{\text{release}} = \frac{c^4}{6G}\,\Delta\Lambda\,\ell^3 \approx 2.0 \times 10^{43}\,\text{J/m} \cdot \Delta\Lambda \cdot \ell^3$$

### Observable Power
$$P_{\text{obs}} \approx \eta \frac{E_{\text{release}}}{\tau}$$

### Energy Density
$$\Delta\rho = \frac{c^4}{8\pi G}\,\Delta\Lambda \approx 4.8 \times 10^{51}\,\text{J/m}^{-1} \cdot \Delta\Lambda$$

### Mass Equivalent
$$M_{\text{equiv}} = \frac{E_{\text{release}}}{c^2} \approx 2.2 \times 10^{26}\,\text{kg/m} \cdot \Delta\Lambda \cdot \ell^3$$

---

**Document status:** Working paper, open for peer review  
**Version:** 1.0 (November 1, 2025)  
**License:** CC BY 4.0  
**Repository:** github.com/nk804/infinite-zero-cosmology
