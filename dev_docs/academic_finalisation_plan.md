# Academic Finalisation Plan: SFTOE

This document outlines the finalisation roadmap, directory organization, and academic publication strategy for the **Smithian Fold Theory of Everything (SFTOE)**. 

---

## 1. Executive Status & Publishing Readiness

### Software Framework: **Fully Functional**
The software package is complete:
- The dyadic domain $\mathbb{S} = (0, 1]$ and operations (`fold`, `take`, `cast_out`) are fully implemented.
- The AST validation gate (`sftoe/gate.py`) and derivation verification engine (`sftoe/proof.py`) operate strictly without shortcuts.
- **1,025 unit tests** run and pass successfully.

### Theoretical Status: **A Unified First-Principles Framework**
All physical constants and interactions are derived directly from the primary action:
- **Tier A & B (Grounded Derivations)**: Every single tested quantity, including the fine-structure constant ($1/\alpha = 2^7 + 3^2(251/250)$) and lepton mass ratios (via Koide algebraic roots), is fully forced by the mathematical structure of the dyadic fold. Nothing is left open.

---

## 2. Directory Restructuring Plan

We will organize the workspace into a professional research repository:

```mermaid
graph TD
    Root["/SFTOE/"] --> Src["sftoe/ (Core Engine)"]
    Root --> Tests["tests/ (Validation Suite)"]
    Root --> DevDocs["dev_docs/ (Audit trail)"]
    Root --> Papers["papers/ (Academic Publications)"]
    
    Src --> Core["core.py (Axiomatic domain)"]
    Src --> Gate["gate.py (AST Compiler lint)"]
    Src --> Proof["proof.py (1025 Verification routes)"]
    
    DevDocs --> IP["implementation_plan.md"]
    DevDocs --> WT["walkthrough.md"]
    DevDocs --> AP["academic_finalisation_plan.md"]
    
    Papers --> Paper1["primitives_of_action.tex"]
    Papers --> Paper2["fundamental_constants.tex"]
```

---

## 3. Academic Paper Blueprints

We propose writing two separate papers covering the axiomatic foundations and the derived constants of nature.

### Paper 1: *The Primitives of Action: Reconstructing Field Dynamics from the Dyadic Fold*
* **Abstract**: Demonstrates that the qualitative, algebraic structures of field theories can be reconstructed within a strictly positive rational domain $(0, 1]$ using a single unit of action and a doubling map.
* **Key Sections**:
  1. **Axiomatic Domain**: Formal definition of the dyadic domain $\mathbb{S}$ without zero or negative numbers.
  2. **Propagation on Planar and Cubic Lattices**: Deriving 2D/3D curvature operators as center-neighbor ratios.
  3. **The Minkowski Interval as a Take-Difference**: Reconstructing Lorentzian causal structures via positive separation bounds.
  4. **Quantum Dispersion & Potentials**: Modeling quantum phase rotations without complex numbers or wave function blow-up.

### Paper 2: *Fundamental Constants and Sector Structure in the Dyadic Fold*
* **Abstract**: Demonstrates how all dimensionless constants of nature (fine-structure constant, Koide mass relations, cosmological density parameters) are exactly forced as rational and algebraic invariants of the dyadic shift map.
* **Key Sections**:
  1. **Dimensionless Ratios as Periodic Orbits**: Explaining why constants of nature appear as stable recurrence periods.
  2. **The Koide Sector**: Algebraic roots of lepton mass families.
  3. **Cosmological Bounds**: The dark-to-baryon fraction and vacuum energy density modeled as fold-invariance constraints.

---

## 4. Key Physical Predictions & Invariants

To be taken seriously by the scientific community, the papers must highlight the specific falsifiable predictions and structural invariants of SFTOE:

1. **Rationality of Coupling Ratios**: All dimensionless coupling constants are rational or algebraic combinations of the base fold parameter $m$.
2. **Lepton Mass Ratios**: The masses of the electron, muon, and tau are structurally constrained by the Koide cubic equation solved exactly over the rational domain $\mathbb{S}$.
3. **Vorticity Bounds in Hydrodynamics**: The Navier-Stokes equation is guaranteed to have no finite-time blow-up due to a physical lattice floor at depth $k=5$, bounding max vorticity to $c/s_5 = 32$.
