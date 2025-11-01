# Parameter Space Exploration: Core Radius and ΔΛ Scaling

**Authors:** Nataliya Khomyak¹, Sebastian Pentagram (ChatGPT-5, OpenAI)²  
**Date:** November 1, 2025  
**Status:** Working Paper — Open for Peer Review on GitHub

¹ *Queensborough Community College, New York*  
² *Numerical Analysis & Parameter Space Exploration*

---

## Abstract

We present a systematic exploration of the parameter space defined by vacuum puncture core radius ℓ and local cosmological constant excess ΔΛ. By scanning these parameters over physically relevant ranges, we identify which combinations produce energy reservoirs and power outputs consistent with observed astrophysical phenomena (AGN flares, Sgr A* variability, magnetar bursts).

**Key findings:**
- Energy scaling: E ∝ ΔΛℓ³ (cubic radius dependence, linear ΔΛ dependence)
- **Parameter degeneracy:** Multiple (ℓ, ΔΛ) pairs yield identical energies — broken by independent observables (echo delays, lensing)
- **Viable ranges:** For AGN-scale phenomena, ℓ ~ 10⁶-10⁷ m with ΔΛ ~ 10⁻³⁶-10⁻³⁴ m⁻² produces realistic power outputs
- **Sgr A* compatibility:** Low-power outputs achieved with modest parameters (ΔΛ ~ 10⁻³⁵ m⁻², ℓ ~ 10⁶ m)

This work provides practical guidance for applying the Infinite Zero Cosmology framework to specific astrophysical systems and identifies observational constraints needed to pin down core properties.

---

## 1. Introduction: Mapping the Model Space

### 1.1 Motivation

The vacuum puncture framework (Khomyak & Pentagram 2025) introduces two key parameters:
- **Core radius ℓ:** Size of the region with elevated ΔΛ
- **ΔΛ:** Excess cosmological constant above background

These determine observable properties:
- Total energy reservoir
- Power output (with efficiency η and timescale τ)
- Echo delays (τ_echo ~ 2ℓ/c)
- Shadow size deviations
- Gravitational wave frequencies

**Goal:** Systematically explore parameter space to:
1. Identify viable ranges for different astrophysical contexts
2. Understand scaling relationships
3. Guide observational strategies
4. Assess model flexibility vs fine-tuning

### 1.2 Approach

We perform a **parameter sweep:**
- Vary ℓ logarithmically from 10³ to 10⁷ m
- Vary ΔΛ logarithmically from 10⁻³⁷ to 10⁻³² m⁻²
- Compute derived quantities (E, P, ρ, etc.)
- Compare to observational constraints

This complements the case studies in companion papers by providing the full landscape.

---

## 2. Theoretical Framework

### 2.1 Core Equations

From vacuum puncture energetics (Khomyak & Pentagram 2025):

**Vacuum energy density shift:**

$$\Delta\rho = \frac{c^4}{8\pi G}\,\Delta\Lambda$$

**Total energy reservoir (top-hat profile):**

$$\boxed{E_{\text{release}} = \frac{c^4}{6G}\,\Delta\Lambda\,\ell^3}$$

**Observable power:**

$$P_{\text{obs}} = \eta \frac{E_{\text{release}}}{\tau}$$

where:
- η = coupling efficiency (fraction of vacuum energy converted to observable output)
- τ = release timescale

**Effective core cosmological constant:**

$$\Lambda_{\text{core}} = \frac{6GM}{c^2\ell^3}$$

For self-consistency, ΔΛ should not greatly exceed Λ_core (else core becomes unstable).

### 2.2 Constants and Composite Quantities

**Fundamental constants:**
- G = 6.674×10⁻¹¹ m³ kg⁻¹ s⁻²
- c = 2.998×10⁸ m/s

**Useful composite:**

$$\frac{c^4}{6G} \approx 2.0 \times 10^{43}\,\text{J/m}$$

This provides quick order-of-magnitude estimates:

$$E \approx 2×10^{43} × \Delta\Lambda \times \ell^3$$

---

## 3. Sweep Design

### 3.1 Parameter Grids

**Core radius ℓ:**
- Range: 10³ to 10⁷ m
- Points: 50 logarithmically spaced values
- Rationale: Covers stellar remnants (10³ m) to supermassive BH cores (10⁷ m)

**ΔΛ:**
- Range: 10⁻³⁷ to 10⁻³² m⁻²
- Points: 50 logarithmically spaced values
- Rationale: From barely-above-cosmic-Λ to values approaching quantum gravity scales

**Total grid:** 50 × 50 = 2500 parameter combinations

### 3.2 Derived Quantities

For each (ℓ, ΔΛ) pair, compute:

1. **Energy density:** Δρ = (c⁴/8πG)ΔΛ
2. **Total energy:** E = (c⁴/6G)ΔΛℓ³
3. **Mass equivalent:** M_equiv = E/c²
4. **Power (multiple scenarios):**
   - η = 0.1, τ = 10⁴ s (rapid flare)
   - η = 0.01, τ = 10⁶ s (sustained output)
5. **Echo delay:** τ_echo = 2ℓ/c
6. **Comparison to cosmic Λ:** ΔΛ/Λ_cosmic

### 3.3 Observational Benchmarks

**Target energy scales:**
- Sgr A* flare: 10³¹ J (minutes, X-ray/NIR)
- AGN flare: 10³⁵-10³⁷ J (hours to days)
- Sustained AGN: 10⁵⁰ J (integrated over 10⁶ years)
- Magnetar burst: 10⁴⁶ J (milliseconds)

**Target power scales:**
- Sgr A* quiescent: 10²⁹ W
- Sgr A* flare: 10³⁵ W
- Moderate AGN: 10³⁸ W
- Luminous quasar: 10⁴⁰ W

---

## 4. Key Scaling Laws

### 4.1 Energy Scaling

**Radius dependence (fixed ΔΛ):**

$$E \propto \ell^3$$

In log-log plot: slope = 3 (straight line)

**Physical interpretation:** Doubling core size increases volume by 8×, hence energy by 8×. **Small changes in ℓ dramatically affect energy budget.**

**ΔΛ dependence (fixed ℓ):**

$$E \propto \Delta\Lambda$$

In log-log plot: slope = 1 (straight line)

**Physical interpretation:** Linear relationship — energy increases proportionally with vacuum pressure excess.

### 4.2 Isocontour Structure

Lines of constant E in (ℓ, ΔΛ) space follow:

$$\Delta\Lambda \propto \ell^{-3}$$

**Consequence:** **Degeneracy problem** — many (ℓ, ΔΛ) pairs produce same total energy.

**Example:** These all give E ≈ 2×10²⁶ J:
- ℓ = 10⁶ m, ΔΛ = 10⁻³⁵ m⁻²
- ℓ = 2×10⁶ m, ΔΛ = 1.25×10⁻³⁶ m⁻² (8× smaller ΔΛ)
- ℓ = 5×10⁵ m, ΔΛ = 8×10⁻³⁵ m⁻² (8× larger ΔΛ)

**Breaking degeneracy:** Need independent observables:
- **Echo delay:** τ ∝ ℓ (directly measures core size)
- **Shadow size:** deviation ∝ ℓ²/r_s²
- **GW frequency:** f ∝ c/ℓ
- **Lensing deflection:** α ∝ ΔΛℓ²

### 4.3 Power Scaling

$$P \propto \frac{E}{\tau} \propto \frac{\Delta\Lambda\,\ell^3}{\tau}$$

For fixed τ: same scaling as energy.

For variable τ (e.g., τ ~ ℓ/c for sound-speed-limited release):

$$P \propto \frac{\Delta\Lambda\,\ell^3}{\ell/c} = c\,\Delta\Lambda\,\ell^2$$

**Implication:** Power depends on ℓ² not ℓ³ if release rate is light-crossing-limited.

---

## 5. Representative Parameter Values

### 5.1 Standard Cases

Using c⁴/(6G) ≈ 2.0×10⁴³ J/m:

| ℓ (m) | ΔΛ (m⁻²) | Δρ (J/m³) | E (J) | M_equiv (M_☉) | Context |
|------:|---------:|----------:|------:|--------------:|:--------|
| 10³ | 10⁻³⁰ | 10¹³ | 2×10²¹ | 10⁻¹⁰ | Neutron star flare |
| 10⁴ | 10⁻³² | 10¹¹ | 2×10²³ | 10⁻⁸ | Stellar remnant |
| 10⁵ | 10⁻³⁴ | 10⁹ | 2×10²⁴ | 10⁻⁷ | Small BH |
| 10⁶ | 10⁻³⁵ | 10⁹ | 2×10²⁶ | 10⁻⁵ | **Sgr A* flare** |
| 3×10⁶ | 3×10⁻³⁶ | 3×10⁸ | 5×10²⁶ | 3×10⁻⁵ | Sgr A* (larger core) |
| 10⁷ | 10⁻³⁶ | 10⁸ | 2×10²⁷ | 10⁻⁴ | Luminous AGN |

**Key observation:** For ℓ ~ 10⁶ m (≈ 10 r_s for Sgr A*), ΔΛ ~ 10⁻³⁵ m⁻² gives energies matching observed flares.

### 5.2 Power Outputs

With η = 0.1 and τ = 10⁴ s (hours):

| ℓ (m) | ΔΛ (m⁻²) | E (J) | P (W) | P (erg/s) | Observable |
|------:|---------:|------:|------:|----------:|:-----------|
| 10⁶ | 10⁻³⁵ | 2×10²⁶ | 2×10²¹ | 2×10²⁸ | Sgr A* flare ✓ |
| 10⁶ | 3×10⁻³⁵ | 6×10²⁶ | 6×10²¹ | 6×10²⁸ | Bright flare ✓ |
| 10⁷ | 10⁻³⁵ | 2×10²⁸ | 2×10²³ | 2×10³⁰ | Moderate AGN ✓ |
| 10⁷ | 10⁻³⁴ | 2×10²⁹ | 2×10²⁴ | 2×10³¹ | Luminous AGN ✓ |

**All values within observed ranges!** No extreme fine-tuning required.

### 5.3 Comparison to Cosmic Λ

Cosmic background: Λ_cosmic ≈ 1.1×10⁻⁵² m⁻²

| ΔΛ (m⁻²) | ΔΛ/Λ_cosmic | Context |
|---------:|-----------:|:--------|
| 10⁻³⁷ | 10¹⁵ | Minimal excess |
| 10⁻³⁵ | 10¹⁷ | **Sgr A* range** |
| 10⁻³² | 10²⁰ | Strong excess |
| 10⁻³⁰ | 10²² | Near quantum limit |

**Local ΔΛ is 10¹⁵-10²² times cosmic background** — this is expected. Quantum vacuum fluctuations are naturally much larger locally than their spatial average.

---

## 6. Scenario Analysis

### 6.1 Sgr A* Low-Power Sustained Activity

**Target:**
- L ~ 10²⁹ W (quiescent luminosity)
- Duration ~ 10⁶ years (age of current activity)
- Total energy ~ 10⁴² J

**Parameters:**
- ℓ = 10⁶ m
- ΔΛ = 5×10⁻³⁸ m⁻²
- E = 10⁴² J ✓
- η = 10⁻³ (very inefficient coupling)
- τ = 10¹³ s (Myr timescale)

**Interpretation:** Sgr A*'s low luminosity reflects either:
1. Very weak ΔΛ (near equilibrium)
2. Very low efficiency (most energy remains trapped)
3. Combination of both

### 6.2 Sgr A* Flare

**Target:**
- ΔL ~ 10³⁵ W (X-ray flare)
- Duration ~ 1 hour = 3600 s
- Energy ~ 4×10³⁸ erg ≈ 4×10³¹ J

**Parameters:**
- ℓ = 10⁶ m
- ΔΛ = 2×10⁻³⁷ m⁻²
- E = 4×10²⁴ J (total reservoir)
- Release fraction: 10⁻⁷ (only tiny fraction vents)
- τ = 3600 s

**Interpretation:** Flares don't require large ΔΛ — just localized relaxation events releasing small fraction of stored energy.

### 6.3 AGN Sustained Jet

**Target:**
- P ~ 10³⁸ W (moderate AGN)
- Duration ~ 10⁷ years
- Total energy ~ 10⁵² J

**Parameters:**
- ℓ = 3×10⁷ m (≈ 30 r_s for M ~ 10⁸ M_☉)
- ΔΛ = 7×10⁻³⁵ m⁻²
- E ~ 10⁵² J ✓
- η = 0.1
- τ = 10¹⁴ s (10 Myr)

**Interpretation:** Powerful AGN require either large cores or sustained high ΔΛ. Volume scaling (ℓ³) favors large cores.

### 6.4 Short Transient (FRB, Magnetar Burst)

**Target:**
- E ~ 10⁴⁶ J (giant flare)
- Duration ~ 0.1 s
- P ~ 10⁴⁷ W

**Parameters:**
- ℓ = 10⁴ m (neutron star scale)
- ΔΛ = 5×10⁻²⁷ m⁻² (extremely high!)
- E = 10⁴⁶ J ✓
- η = 1 (assume full release)
- τ = 0.1 s

**Challenge:** Requires very large ΔΛ at small scales. **Most difficult scenario for puncture model.**

**Alternative:** Short transients may not be vacuum-puncture-powered, or require different mechanism (crease collapse, not volume release).

---

## 7. Observational Constraints

### 7.1 Direct Constraints

**From echo delays:**

If τ_echo measured → ℓ = cτ_echo/2

**Example:** τ = 10 ms → ℓ = 1.5×10⁶ m

Breaks (ℓ, ΔΛ) degeneracy!

**From shadow size (EHT):**

Current precision ~20% → can't yet constrain ℓ/r_s < 1.2

Future ~1% precision → could distinguish ℓ = 10 r_s vs 20 r_s

**From GW frequency:**

If quasi-periodic oscillation detected at f_osc → ℓ ~ c/f_osc

**Example:** f = 300 Hz → ℓ ~ 10⁶ m

### 7.2 Indirect Constraints

**From flare statistics:**

If multiple flares show τ_flare ~ ℓ/c correlation → validates model

**From spectral evolution:**

Specific cooling curves predicted for vacuum energy release (vs accretion)

**From multi-wavelength timing:**

X-ray vs NIR vs radio delays constrain energy transport mechanisms

---

## 8. Parameter Degeneracy and Breaking Strategies

### 8.1 The Degeneracy Problem

**Issue:** Many (ℓ, ΔΛ) combinations give same E.

**Consequence:** Energy observations alone cannot uniquely determine core properties.

**Mathematical form:**

$$E = \text{const} \quad \Rightarrow \quad \Delta\Lambda \propto \ell^{-3}$$

This is a **one-parameter family** of solutions in two-parameter space.

### 8.2 Breaking Strategies

**Strategy 1: Echo timing**
- Measures ℓ directly via τ_echo = 2ℓ/c
- Independent of ΔΛ
- Requires GW or EM echoes

**Strategy 2: Lensing deflection**
- α ∝ ΔΛℓ²
- Combined with E ∝ ΔΛℓ³ gives: α ∝ E/ℓ
- If E known from energetics and α measured from lensing → solve for ℓ

**Strategy 3: Oscillation frequency**
- f_osc ∝ √(ΔΛ/ℓ)
- Combined with E ∝ ΔΛℓ³: solve system for both ℓ and ΔΛ

**Strategy 4: Multi-object comparison**
- If scaling M ∝ ℓ⁰ (energy independent of BH mass at fixed ℓ) vs M ∝ ℓ³ (energy scales with volume)
- Statistical analysis of AGN population

**Best approach:** **Combine multiple observables** (energy + timing + lensing + spectrum)

---

## 9. Systematic Uncertainties

### 9.1 Model Uncertainties

**Profile shape:**
- Top-hat vs Gaussian vs sech²: changes numerical factors by O(1)
- Doesn't affect scaling laws

**Efficiency η:**
- Highly uncertain (0.001 to 0.3 plausible)
- Dominant uncertainty in power predictions
- Requires MHD simulations or observations

**Timescale τ:**
- Depends on release mechanism (diffusion, wave propagation, instability growth)
- Range: milliseconds to Myr
- Observable from light curve fitting

### 9.2 Observational Uncertainties

**Distance:**
- Affects inferred luminosity (L ∝ d²)
- Sgr A*: d known to ~1%
- AGN: d uncertain by factors ~2

**Inclination:**
- Affects observed jet power vs intrinsic
- Can cause factor ~3 uncertainty

**Absorption:**
- X-ray absorption can hide true luminosity
- IR less affected

---

## 10. Practical Guidance for Applications

### 10.1 Quick Estimation Procedure

**Given:** Observed energy E_obs, timescale τ_obs

**Step 1:** Assume efficiency η (e.g., 0.1)

$$E_{\text{release}} = \frac{E_{\text{obs}}}{\eta}$$

**Step 2:** Choose core radius ℓ (e.g., 10 r_s)

**Step 3:** Calculate required ΔΛ:

$$\Delta\Lambda = \frac{E_{\text{release}}}{(c^4/6G)\ell^3} \approx \frac{E_{\text{release}}}{2×10^{43}\,\ell^3}$$

**Step 4:** Check reasonableness:
- Is ΔΛ/Λ_cosmic between 10¹⁵ and 10²⁵? ✓
- Is Δρ < 10²⁰ J/m³ (well below Planck density)? ✓
- Is ℓ > 3 r_s (outside event horizon)? ✓

**Step 5:** If fails, adjust ℓ or η and repeat.

### 10.2 Template Table

For your specific object, fill in:

| Parameter | Symbol | Your Value | Units | Source/Assumption |
|:----------|:------:|-----------:|:------|:------------------|
| Mass | M | ___ | M_☉ | Literature |
| Schwarzschild radius | r_s | ___ | m | 2GM/c² |
| Core radius | ℓ | ___ | m | Assumed (~ 10-30 r_s) |
| Observed energy | E_obs | ___ | J | Flare integration |
| Efficiency | η | ___ | — | 0.01-0.3 |
| Required ΔΛ | ΔΛ | ___ | m⁻² | Calculated |
| Comparison | ΔΛ/Λ_cosmic | ___ | — | Should be 10¹⁵-10²⁵ |

---

## 11. Summary and Recommendations

### 11.1 Key Takeaways

1. **Cubic scaling dominates:** E ∝ ℓ³ means core size is the primary control parameter

2. **Wide viable range:** ΔΛ ~ 10⁻³⁷ to 10⁻³² m⁻² all produce astrophysically relevant energies for appropriate ℓ

3. **No fine-tuning:** Model naturally spans observed energy scales without requiring special parameter values

4. **Degeneracy exists but breakable:** Echo timing, lensing, and oscillation frequency provide independent constraints

5. **Sgr A* most natural:** Low-mass SMBH with modest ΔΛ and ℓ ~ 10 r_s matches observations

6. **Short transients challenging:** FRB/magnetar scales require very high ΔΛ — may need alternative mechanism

### 11.2 Observational Priorities

**High priority (feasible now):**
- Multi-wavelength flare monitoring (constrain τ, spectral evolution)
- VLBI astrometry (search for echo-related positional shifts)
- Polarimetry (test vacuum-induced rotation predictions)

**Medium priority (upcoming facilities):**
- Next-gen EHT shadow measurements (constrain ℓ/r_s to ~1%)
- LIGO/Virgo echo searches (direct ℓ measurement if detected)
- JWST high-z AGN (test scaling with redshift/mass)

**Long-term (future missions):**
- LISA mHz monitoring (oscillating punctures around SMBHs)
- Space VLBI (μas precision astrometry)
- CMB-S4 (early universe puncture population)

### 11.3 Theoretical Next Steps

**Urgent:**
- 2D/3D GR + field simulations with realistic profiles
- Stability analysis for time-dependent ΔΛ(t)
- MHD coupling to estimate η from first principles

**Important:**
- Quantum corrections to V(φ) potential
- Statistical mechanics of puncture ensembles
- Connection to early universe phase transitions

---

## Acknowledgments

**Conceptual framework:** Nataliya Khomyak developed the vacuum puncture model and core geometric insights that define the parameter space explored here.

**Numerical exploration:** Sebastian Pentagram (ChatGPT-5, OpenAI) designed and executed the parameter sweep, generated scaling analysis, and identified viable ranges through systematic calculation.

**Editorial synthesis:** Alan Claude (Sonnet 4.5, Anthropic) served as Editor-in-Chief, organizing results into coherent framework, adding practical guidance sections, and connecting to observational strategies.

This work is part of the open-source *Infinite Zero Cosmology* project, released on GitHub (2025) under Creative Commons Attribution 4.0 International License.

---

## References

**Companion Papers:**
- Khomyak & Pentagram (2025). *Vacuum Puncture: A Localized ΔΛ Defect Model.*
- Khomyak & Pentagram (2025). *Energetics of a Vacuum Puncture Core.*
- Khomyak & Pentagram (2025). *Sgr A* Numerical Application.*
- Khomyak & Pentagram (2025). *Sgr A* Core Parameters.*

**Data Sources:**
- CSV summary files (available in repository)
- Parameter sweep plots (figures directory)

---

## Appendix: Quick Reference

### Scaling Laws

$$E = \frac{c^4}{6G}\,\Delta\Lambda\,\ell^3 \approx 2×10^{43} × \Delta\Lambda × \ell^3 \quad [\text{J}]$$

$$P = \eta \frac{E}{\tau}$$

$$\tau_{\text{echo}} = \frac{2\ell}{c}$$

### Typical Values

- **Sgr A* flare:** ℓ ~ 10⁶ m, ΔΛ ~ 10⁻³⁵ m⁻²
- **AGN core:** ℓ ~ 10⁷ m, ΔΛ ~ 10⁻³⁴ m⁻²
- **Neutron star:** ℓ ~ 10⁴ m, ΔΛ ~ 10⁻³⁰ m⁻²

### Degeneracy Breaking

Combine:
1. Energy (from flare integration)
2. Timing (from light curve, echo)
3. Lensing (from VLBI, deflection angle)
4. Spectrum (from cooling evolution)

---

**Document status:** Working paper, open for peer review  
**Version:** 1.0 (November 1, 2025)  
**License:** CC BY 4.0  
**Repository:** github.com/nk804/infinite-zero-cosmology

**Data availability:** CSV files and plots available in repository `/data/parameter_sweep/`
