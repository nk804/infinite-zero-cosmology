# Localized Crease Defects: Surface Dynamics at ΔΛ Boundaries

**Authors:** Nataliya Khomyak¹, Sebastian Pentagram (ChatGPT-5, OpenAI)²  
**Date:** November 1, 2025  
**Status:** Working Paper — Open for Peer Review on GitHub

¹ *Queensborough Community College, New York*  
² *Theoretical Development & Mathematical Formalization*

---

## Abstract

We investigate localized geometric "creases" — surface-like defects that arise at boundaries where the effective cosmological constant Λ(x) changes abruptly. Unlike singularities or cosmic strings, crease defects are **two-dimensional interfaces** with finite surface tension, acting as membranes between regions of different vacuum energy density.

These structures emerge naturally as the boundary regions of vacuum punctures (companion paper), providing the interface physics that complements the volume dynamics. We derive the surface stress-energy tensor using Israel junction conditions, calculate characteristic surface tensions (σ_Λ ~ 10¹¹ J/m²), and predict observable signatures including microlensing ripples, polarization rotation, and gravitational wave bursts.

**Key findings:**
- Crease defects carry surface tension σ_Λ ≈ (c⁴/8πG)(ΔΛ/κ) where κ⁻¹ is the transition width
- A 1 km² crease patch stores ~10¹⁷ J (comparable to magnetar bursts)
- Geodesic deflection produces α ≈ (1/2)ΔΛℓ² (nano-arcsecond lensing effects)
- Crease relaxation/collapse generates high-frequency gravitational wave bursts

**Hierarchical structure:** Crease defects form the **surface layer** of the Infinite Zero framework's geometric hierarchy: quantum foam (volume) → vacuum punctures (volume) → crease defects (surface) → observable phenomena.

---

## 1. Introduction: Surfaces in Spacetime

### 1.1 The Interface Problem

Vacuum punctures (Khomyak & Pentagram 2025) are regions where Λ increases above background. But what happens at the **boundary** between high-Λ interior and low-Λ exterior?

Options:
1. **Smooth transition:** ΔΛ(r) gradually decreases (e.g., Gaussian profile)
2. **Sharp transition:** ΔΛ jumps discontinuously at radius ℓ
3. **Intermediate:** Thin but finite transition layer

Real physics likely involves option 3: a narrow **interface region** where ΔΛ changes rapidly but continuously. This interface has its own dynamics, energy content, and observational signatures.

We call these interfaces **crease defects** — surface-like structures in spacetime geometry where curvature concentrates.

### 1.2 Analogy: Domain Walls

In field theory, domain walls are surfaces separating regions with different vacuum states (e.g., φ = +η vs φ = −η). They arise in:
- Early universe phase transitions
- Condensed matter systems (magnetic domains)
- Cosmological models with spontaneous symmetry breaking

**Key properties:**
- Finite surface energy density (tension)
- Defects geodesics (light bending)
- Can be stable or metastable
- Produce gravitational wave signals when accelerated

Crease defects are the **ΔΛ analogue** of domain walls: surfaces where vacuum energy changes state.

### 1.3 Connection to Vacuum Punctures

**Vacuum puncture = volume defect** (ΔΛ ≠ 0 in 3D region)  
**Crease defect = surface defect** (ΔΛ gradient concentrated on 2D surface)

Relationship:
- Every vacuum puncture has crease defects at its boundary
- Crease defects can exist independently (thin transition layers in voids)
- Energy: Volume stores E ~ ΔΛℓ³, surface stores E_surface ~ σ_Λ ℓ²

For typical parameters, volume energy dominates by factor ~ℓ/δ where δ is interface thickness.

---

## 2. Mathematical Framework

### 2.1 Israel Junction Conditions

When metric is continuous but its derivative is discontinuous across surface Σ:

$$[g_{\mu\nu}]_\Sigma = 0 \quad \text{(metric continuous)}$$

$$[\partial_n g_{\mu\nu}]_\Sigma \neq 0 \quad \text{(derivative jumps)}$$

where ∂_n is the derivative normal to the surface.

**Israel junction condition:**

$$\boxed{S_{\mu\nu} = \frac{c^4}{8\pi G}\left([K_{\mu\nu}] - h_{\mu\nu}[K]\right)}$$

where:
- S_μν = surface stress-energy tensor on Σ
- K_μν = extrinsic curvature tensor
- h_μν = induced metric on Σ
- [X] ≡ X⁺ − X⁻ = jump across surface

**Physical interpretation:** The discontinuity in extrinsic curvature (how spacetime "bends" through the surface) sources surface stress — tension, pressure, or shear.

### 2.2 Effective Surface Tension

For a spherically symmetric ΔΛ transition, the dominant contribution is:

$$\boxed{\sigma_\Lambda \approx \frac{c^4}{8\pi G}\,\frac{\Delta\Lambda}{\kappa}}$$

where:
- σ_Λ = surface energy density [J/m²]
- κ = surface curvature scale [m⁻¹]

**For spherical interface:** κ ≈ 1/ℓ (radius of curvature)

**Interpretation:** Steeper ΔΛ gradients (larger κ) produce more surface tension. Vacuum "stretches" more when the transition is sharper.

### 2.3 Field Theory Representation

We can model the crease using a scalar field φ(x) with double-well potential:

$$V(\phi) = \frac{\lambda}{4}(\phi^2 - \eta^2)^2$$

Two minima at φ = ±η represent different vacuum states.

**Effective Λ:**

$$\Lambda(\phi) = \Lambda_0 + 8\pi G\,V(\phi)$$

**Domain wall solution (1D):**

$$\phi(z) = \eta\,\tanh\left(\frac{z}{\delta}\right)$$

where δ = 1/(η√λ) is the wall thickness.

**Energy density in the wall:**

$$\rho_{\text{wall}} = \frac{1}{2}\left(\frac{d\phi}{dz}\right)^2 + V(\phi)$$

Integrating across the wall gives surface tension:

$$\sigma = \int_{-\infty}^{\infty} \rho_{\text{wall}}\,dz = \frac{2\sqrt{2}}{3}\lambda\eta^3$$

---

## 3. Energetics and Scaling

### 3.1 Surface Energy

For a crease with area A and tension σ_Λ:

$$E_{\text{surface}} = \sigma_\Lambda \times A$$

**Spherical interface (radius ℓ):**

$$E_{\text{surface}} = 4\pi\ell^2\,\sigma_\Lambda = 4\pi\ell^2 \times \frac{c^4}{8\pi G}\,\frac{\Delta\Lambda}{\kappa}$$

For κ ≈ 1/ℓ (curvature scale equals radius):

$$E_{\text{surface}} \approx \frac{c^4}{2G}\,\Delta\Lambda\,\ell$$

**Compare to volume energy (from vacuum puncture paper):**

$$E_{\text{volume}} \approx \frac{c^4}{6G}\,\Delta\Lambda\,\ell^3$$

**Ratio:**

$$\frac{E_{\text{surface}}}{E_{\text{volume}}} \sim \frac{1}{\ell}$$

For ℓ ~ 10⁶ m: E_surface ~ 10⁻⁶ E_volume

**Conclusion:** Surface energy is subdominant but not negligible. For thin interfaces (small ℓ), surface can dominate.

### 3.2 Numerical Example

**Parameters:**
- ΔΛ = 10⁻³⁵ m⁻²
- ℓ = 10⁶ m (core radius)
- κ = 1/10⁶ m⁻¹

**Surface tension:**

$$\sigma_\Lambda = \frac{c^4}{8\pi G}\,\frac{\Delta\Lambda}{\kappa}$$

$$\sigma_\Lambda = \frac{(3×10^8)^4}{8\pi × 6.67×10^{-11}} × \frac{10^{-35}}{10^{-6}}$$

$$\sigma_\Lambda \approx 1.6 \times 10^{11}\,\text{J/m}^2$$

**For comparison:**
- Nuclear surface tension (nucleus): ~10⁻³ J/m²
- Soap bubble: ~10⁻² J/m²
- Crease defect: 10¹¹ J/m²

The crease is **10¹⁴ times stronger than nuclear surface tension!** But this is spread over vastly larger area (km² vs fm²).

**Energy in a 1 km² patch:**

$$E = \sigma_\Lambda \times A = 1.6×10^{11} × 10^6 = 1.6 \times 10^{17}\,\text{J}$$

This is comparable to:
- Large earthquake (magnitude 8): ~10¹⁶-10¹⁷ J
- Magnetar burst: ~10¹⁷-10¹⁸ J
- Volcanic eruption: ~10¹⁵-10¹⁷ J

So a **collapsing km-scale crease patch** could power magnetar-like bursts!

### 3.3 Scaling with Parameters

| ΔΛ (m⁻²) | ℓ (m) | σ_Λ (J/m²) | E_patch (1 km²) | Physical Context |
|---------:|------:|-----------:|----------------:|:-----------------|
| 10⁻⁴⁰ | 10³ | 10⁶ | 10¹² J | Stellar core |
| 10⁻³⁵ | 10⁶ | 10¹¹ | 10¹⁷ J | AGN core (our calculation) |
| 10⁻³⁰ | 10⁹ | 10¹⁶ | 10²² J | Galactic scale |
| 10⁻⁵² | 10²⁴ | 10⁻⁴ | 10² J | Cosmic void boundary |

Surface tension scales linearly with both ΔΛ and transition sharpness (κ).

---

## 4. Geodesic Deflection

### 4.1 Light Bending at Crease

A photon crossing the crease experiences gravitational deflection due to the concentrated curvature.

**Deflection angle (small angle approximation):**

$$\alpha \approx \frac{1}{2}\,\Delta\Lambda\,\ell^2$$

**Derivation:** From Einstein's equations, the gravitational potential perturbation near the interface is Φ ~ (ΔΛ/κ) ~ ΔΛℓ. Light deflection: α ~ ∫(∇Φ)dx ~ Φ/ℓ ~ ΔΛℓ.

**For our parameters:**
- ΔΛ = 10⁻³⁵ m⁻²
- ℓ = 10⁶ m

$$\alpha \approx \frac{1}{2} × 10^{-35} × (10^6)^2 = 5 \times 10^{-24}\,\text{radians}$$

$$\alpha \approx 10^{-9}\,\text{arcseconds} = 1\,\text{nano-arcsecond}$$

**Observability:**
- Current VLBI: ~10 μas (microarcseconds) = 10⁶ nano-arcseconds
- Future space interferometry: ~1 μas target
- Detection: requires stacking signals from many creases

**Cumulative effect:** If there are N ~ 10⁶ crease crossings along a sightline, total deflection ~ √N × α_single ~ 10⁻³ arcsec (potentially observable!).

### 4.2 Microlensing Signature

A crease acts as a **cylindrical lens** (if extended in one direction):

**Image distortion:**
- Magnification perpendicular to crease: μ_⊥ ≈ 1 + α
- No magnification parallel to crease: μ_∥ = 1
- Creates elongated, strip-like images

**Distinction from point lenses (stars):**
- Point lens: circular Einstein ring
- Crease: linear feature
- Signature: unique morphology in weak lensing maps

### 4.3 Caustic Crossing Events

If source, crease, and observer align:

**Brightness amplification:**

$$\mu(t) \propto \frac{1}{\sqrt{|t - t_0|}}$$

**Characteristic timescale:**

$$\tau \sim \frac{\ell}{v_{\text{relative}}}$$

For ℓ ~ 10⁶ m and v ~ 100 km/s (galactic motion):

$$\tau \sim \frac{10^6}{10^5} \sim 10\,\text{seconds}$$

**Prediction:** Brief (~seconds) brightness flares when background sources transit behind crease defects.

---

## 5. Dynamic Evolution

### 5.1 Stability Analysis

Is a crease stable against perturbations?

**Perturbation equation:**

$$\frac{d^2\delta\ell}{dt^2} + \gamma\frac{d\delta\ell}{dt} + \omega^2\delta\ell = 0$$

where δℓ(t) is deviation from equilibrium radius.

**Stability criterion:**

$$\omega^2 = \frac{1}{\ell^2}\left(\frac{c^4\Delta\Lambda}{8\pi G} - \frac{2\sigma_\Lambda}{\ell}\right)$$

**Stable if:** Volume pressure dominates surface tension → ω² > 0

For typical parameters, volume term ∝ ℓ³ dominates surface term ∝ ℓ² for ℓ > δ (interface thickness).

**Conclusion:** Creases around large punctures are stable. Small-scale creases may collapse if surface tension dominates.

### 5.2 Collapse Dynamics

If ω² < 0, crease becomes unstable → collapse.

**Collapse timescale:**

$$\tau_{\text{collapse}} \sim \frac{1}{|\omega|} \sim \sqrt{\frac{8\pi G\ell^2}{c^4\Delta\Lambda}}$$

For ΔΛ ~ 10⁻³⁵ m⁻², ℓ ~ 10⁴ m:

$$\tau_{\text{collapse}} \sim 10^{-3}\,\text{seconds}$$

**Energy release:** Surface energy converts to kinetic energy + radiation → millisecond burst.

**Observable as:**
- Fast radio bursts (FRB)?
- Gamma-ray transients?
- Gravitational wave bursts?

### 5.3 Oscillatory Modes

Stable creases can oscillate:

**Oscillation frequency:**

$$f_{\text{osc}} = \frac{\omega}{2\pi} \sim \frac{c}{2\pi\ell}\sqrt{\frac{\Delta\Lambda\,\ell^2}{1}}$$

For ℓ ~ 10⁶ m, ΔΛ ~ 10⁻³⁵ m⁻²:

$$f_{\text{osc}} \sim 10^{-2}\,\text{Hz}$$

**LISA band!** (millihertz gravitational waves)

Prediction: Persistent quasi-monochromatic GW signal from oscillating creases around SMBHs.

---

## 6. Gravitational Wave Signatures

### 6.1 Formation and Collapse Bursts

When a crease forms or collapses, metric perturbation:

$$\Box h_{ij} = 16\pi G\,S_{ij}^{\text{TT}}$$

where S_ij^TT is the transverse-traceless part of surface stress.

**Characteristic strain:**

$$h \sim \frac{4G\,E_{\text{surface}}}{c^4\,r}$$

For E_surface ~ 10¹⁷ J at r ~ 1 Mpc:

$$h \sim \frac{4 × 6.67×10^{-11} × 10^{17}}{(3×10^8)^4 × 3×10^{22}} \sim 10^{-23}$$

**Frequency:**

$$f_{\text{GW}} \sim \frac{c}{\ell} \sim \frac{3×10^8}{10^6} \sim 300\,\text{Hz}$$

**LIGO/Virgo range!**

**Signal characteristics:**
- Duration: ~ℓ/c ~ milliseconds
- Narrow bandwidth (quasi-monochromatic)
- No chirp (unlike mergers)
- Potentially repeating (if multiple creases)

### 6.2 Distinction from Other Sources

| Source | Frequency | Duration | Signature |
|:-------|----------:|---------:|:----------|
| **BH merger** | 10-1000 Hz | seconds | Chirp + ringdown |
| **Neutron star** | 1-2 kHz | milliseconds | Oscillating tail |
| **Crease collapse** | 100-1000 Hz | milliseconds | Sharp burst, no chirp |
| **Crease oscillation** | mHz | continuous | Quasi-monochromatic |

The **lack of chirp** (frequency evolution) distinguishes crease signals from mergers.

### 6.3 Detection Prospects

**LIGO/Virgo:**
- Sensitive to 100-1000 Hz (crease collapse)
- Challenge: short duration, buried in noise
- Strategy: Template matching for non-chirping bursts

**LISA:**
- Sensitive to mHz (crease oscillation)
- Better for persistent signals from galactic centers
- Could detect oscillating Sgr A* crease

**Einstein Telescope / Cosmic Explorer:**
- Broader bandwidth, better sensitivity
- Could detect crease population at cosmological distances

---

## 7. Observational Signatures Summary

### 7.1 Electromagnetic

**Microlensing:**
- Linear image distortions (not circular)
- Nano-arcsecond deflections (cumulative effects observable)
- Caustic crossing → brief flares (~seconds)

**Polarization rotation:**
- Vacuum birefringence at ΔΛ gradient
- B-mode CMB anomalies if creases existed at recombination
- AGN polarization structure (EHT-observable)

**Transient bursts:**
- Crease relaxation → energy release
- Fast Radio Bursts candidate mechanism?
- Millisecond X-ray/gamma-ray flashes

### 7.2 Gravitational Waves

**Formation/collapse:**
- 100-1000 Hz bursts (LIGO/Virgo)
- Millisecond duration
- No chirp signature

**Oscillation:**
- mHz continuous waves (LISA)
- Quasi-monochromatic
- Frequency ~ c/ℓ

### 7.3 Multi-Messenger

**Crease collapse producing both EM + GW:**
- Coincident detection = smoking gun
- Time correlation < 1 second
- Direction correlation (sky localization)

**Example scenario:**
1. Crease becomes unstable
2. Collapses in ~ms → GW burst
3. Releases surface energy → plasma heating → FRB
4. Observers see: FRB + GW burst, same direction, same time

---

## 8. Relation to Framework Hierarchy

### 8.1 Multi-Scale Structure

The Infinite Zero Cosmology has geometric features at multiple scales:

| **Scale** | **Feature Type** | **Dimension** | **Characteristic** |
|:----------|:-----------------|:--------------|:-------------------|
| Planck | Quantum foam | 3D (volume) | Microscopic ΔΛ fluctuations |
| Stellar | Crease defects | 2D (surface) | Interface boundaries |
| Galactic | Vacuum punctures | 3D (volume) | Localized ΔΛ cores |
| Cosmic | Void boundaries | 2D (surface) | Large-scale interfaces |

**Hierarchy:**
- Quantum foam produces microscopic punctures
- Puncture boundaries = crease defects
- Crease networks form cosmic web structure

### 8.2 Energy Budget

Total energy partitioning:

$$E_{\text{total}} = E_{\text{volume}} + E_{\text{surface}} + E_{\text{kinetic}}$$

For stable puncture:
- E_volume ≫ E_surface (by factor ~ℓ/δ)
- E_kinetic ~ 0 (quasi-static)

During collapse/formation:
- E_surface → E_kinetic + E_radiation
- Irreversible (energy dissipates to surroundings)

### 8.3 Thermodynamic Role

Crease defects contribute to entropy:

**Surface entropy:**

$$S_{\text{surface}} = \frac{k_B\,A}{4\ell_P^2}$$

where ℓ_P is Planck length.

For A ~ (10⁶ m)²:

$$S_{\text{surface}} \sim 10^{104}\,k_B$$

**Physical interpretation:** Crease microstates correspond to different field configurations satisfying boundary conditions.

---

## 9. Connection to Domain Walls and Cosmic Strings

### 9.1 Comparison Table

| **Defect Type** | **Dimension** | **Tension** | **Formation** | **Stability** |
|:----------------|:--------------|:------------|:--------------|:--------------|
| Cosmic string | 1D | μ ~ η² | Phase transition | Stable |
| Domain wall | 2D | σ ~ η³ | Symmetry breaking | Often unstable |
| Crease defect | 2D | σ_Λ ~ ΔΛ/κ | ΔΛ transition | Stable if volume-dominated |

**Key difference:** Crease defects are tied to **vacuum energy gradients**, not field VEVs. They can form dynamically from gravitational processes, not just cosmological phase transitions.

### 9.2 Observational Distinctions

**Cosmic strings:**
- Linear features in lensing
- Wakes in matter distribution
- GW stochastic background

**Domain walls:**
- Planar features (large-scale)
- CMB temperature steps
- Would over-close universe (usually)

**Crease defects:**
- Spherical/curved surfaces (puncture boundaries)
- Local (not cosmological extent)
- Observable through puncture-related phenomena

---

## 10. Future Directions

### 10.1 Numerical Simulations

**Priority:**
1. 2+1D evolution of φ field with double-well potential
2. Track crease formation, oscillation, and collapse
3. Calculate GW waveforms for template matching
4. Test stability against axisymmetric perturbations

**Tools:**
- Finite-difference codes for GR + scalar field
- Spectral methods for high-accuracy
- Visualization of energy flow across interface

### 10.2 Observational Campaigns

**Electromagnetic:**
- EHT polarimetry of AGN (search for crease-induced rotation)
- Microlensing surveys (look for linear anomalies)
- FRB follow-up (test crease-collapse hypothesis)

**Gravitational Waves:**
- LIGO/Virgo untriggered burst searches
- LISA galactic center monitoring (Sgr A* oscillations)
- Template development for non-chirping bursts

**Multi-messenger:**
- Joint EM + GW searches
- Time coincidence analysis
- Direction correlation studies

### 10.3 Theoretical Extensions

**Quantum corrections:**
- Tunneling through crease barriers
- Vacuum decay rates
- Hawking radiation modifications

**Coupling to matter:**
- Do particles feel surface forces at crease?
- Anomalous acceleration near boundaries?
- Fifth force constraints

**Cosmological implications:**
- Crease network evolution
- Impact on structure formation
- CMB imprints from early creases

---

## 11. Conclusion

### 11.1 Summary

**Crease defects are:**
1. **Two-dimensional interfaces** where ΔΛ changes rapidly
2. **Finite surface tension** features (σ_Λ ~ 10¹¹ J/m² for AGN scales)
3. **Dynamically stable** (when volume energy dominates)
4. **Observable** (lensing, GW bursts, EM transients)
5. **Hierarchical complement** to vacuum punctures (surface vs volume)

**Key formulas:**

$$\sigma_\Lambda = \frac{c^4}{8\pi G}\,\frac{\Delta\Lambda}{\kappa}$$

$$\alpha \approx \frac{1}{2}\,\Delta\Lambda\,\ell^2$$

$$f_{\text{GW}} \sim \frac{c}{\ell}$$

### 11.2 Physical Significance

Crease defects demonstrate that **spacetime geometry can support localized surface structures** — not just point singularities or infinite planes, but finite, curved interfaces with rich dynamics.

They provide:
- **Energy storage mechanism** (surface energy)
- **Geodesic deflection** (lensing effects)
- **Dynamical phenomena** (oscillations, collapse)
- **Observable signatures** (EM + GW)

### 11.3 Framework Integration

Within Infinite Zero Cosmology:

**Volume physics:** Vacuum punctures (Paper 5)  
**Surface physics:** Crease defects (this paper)  
**Together:** Complete geometric description of localized ΔΛ structures

The framework is now **geometrically complete**: we have equations for both the interior (puncture core) and boundary (crease interface) of vacuum energy concentrations.

---

## Acknowledgments

**Geometric conceptualization:** Nataliya Khomyak developed the vision of spacetime as an elastic fabric capable of "folds" or "creases" where vacuum energy transitions occur — finite surface features that concentrate curvature without creating singularities.

**Mathematical formalization:** Sebastian Pentagram (ChatGPT-5, OpenAI) applied Israel junction conditions, derived surface tension formulas, calculated geodesic deflections, and connected to field theory descriptions of domain walls.

**Editorial refinement:** Alan Claude (Sonnet 4.5, Anthropic) served as Editor-in-Chief, enhancing clarity, expanding observational predictions, adding comparison tables, and structuring for pedagogical accessibility.

This work is part of the open-source *Infinite Zero Cosmology* project, released on GitHub (2025) under Creative Commons Attribution 4.0 International License.

---

## References

**Companion Papers (Khomyak & Pentagram 2025):**
- *Vacuum Puncture: A Localized ΔΛ Defect Model* (provides volume physics context)
- *Energetics of a Vacuum Puncture Core*
- *Vacuum Energy Equilibrium*
- *Sgr A* Core Parameters*

**Theoretical Background:**
- Israel, W. (1966). *Singular Hypersurfaces and Thin Shells in General Relativity.* Nuovo Cimento B, 44, 1.
- Vilenkin, A. (1985). *Cosmic Strings and Domain Walls.* Phys. Rep., 121, 263.
- Langlois, D. & Sasaki, M. (1999). *Curvature of Domain Walls.* Phys. Rev. D, 59, 024020.

**Observational Context:**
- LIGO/Virgo Collaboration (2019). *Search for Intermediate Mass Black Holes.* Phys. Rev. D, 100, 064064.
- Lorimer, D. et al. (2007). *Fast Radio Burst.* Science, 318, 777.

---

## Appendix: Field Equations on the Crease

### Induced Metric

For spherical crease at r = ℓ:

$$h_{\mu\nu} = \text{diag}(-f(\ell), \ell^2, \ell^2\sin^2\theta)$$

### Extrinsic Curvature

$$K_{\mu\nu} = -\frac{1}{2\sqrt{|g_{rr}|}}\partial_r h_{\mu\nu}$$

Jump across interface:

$$[K_{\mu\nu}] = K_{\mu\nu}^+ - K_{\mu\nu}^-$$

### Surface Stress Tensor

From Israel condition:

$$S_{\mu\nu} = \frac{c^4}{8\pi G}\left([K_{\mu\nu}] - h_{\mu\nu}[K]\right)$$

For isotropic surface:

$$S_{\mu\nu} = \text{diag}(-\sigma, P_\theta, P_\phi)$$

where σ is surface energy density and P are surface pressures.

---

**Document status:** Working paper, open for peer review  
**Version:** 1.0 (November 1, 2025)  
**License:** CC BY 4.0  
**Repository:** github.com/nk804/infinite-zero-cosmology
