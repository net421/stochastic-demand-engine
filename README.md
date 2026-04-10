## 🔬 Repository Purpose

This repository is the **official computational companion** to the research manuscript:

> *“Decreasing Failure Rate in Near-Critical Systems: Inverse Gaussian First-Passage Dynamics and Hazard-Structure Characterization”*

The purpose of this repository is to ensure **complete transparency, reproducibility, and validation** of all results presented in the manuscript.

Specifically, it contains:

* All simulation code used to generate the results
* All statistical analyses and model fitting procedures
* All figure and table generation scripts
* Full pipeline to reproduce the manuscript outputs from scratch

👉 Every figure, table, and numerical result in the paper can be regenerated directly from this repository

---

## 🚀 Research Contributions (Summary)

Beyond reproducibility, this work introduces **original theoretical and practical contributions** to the analysis of near-critical systems:

* **New diagnostic metric (Jump Ratio ( R_J ))**
  A dimensionless parameter that governs collapse dynamics and determines when diffusion-based models are valid

* **Two-regime collapse framework**
  Identification of *drift-dominated* vs. *jump-dominated* regimes, explaining when classical approximations succeed or fail

* **Discovery of Decreasing Failure Rate (DFR) behavior**
  Demonstration that failure risk decreases over time due to endogenous survivorship effects—contradicting standard reliability assumptions

* **Quantification of model bias in diffusion approximations**
  Systematic underestimation of shape parameters with an invariant correction structure

* **Operational insight: failure of mean-based risk metrics**
  Evidence that up to **72% of systems fail before the mean**, motivating quantile-based decision frameworks

👉 Collectively, these contributions bridge **stochastic process theory and real-world operational risk**, with direct implications for supply chains, infrastructure systems, and reliability engineering.

---

## 🧠 Scientific Context

We study **first-passage collapse dynamics** in capacity-constrained systems operating near their stability boundary.

System dynamics:

* Demand: ( D(t) \sim \text{Poisson}(\lambda) )
* Disruptions: ( B(t) \sim \text{Bernoulli}(1 - p) )
* State evolution:

[
I(t+1) = I(t) + B(t)\cdot C - D(t)
]

Collapse is defined as the first-passage time:

[
\tau = \min { t : I(t) < -X_0 }
]

---

## 🚀 Core Contributions of the Research

This work makes four primary contributions:

### 1. Distributional Characterization of Collapse Times

* Demonstrates that the **Inverse Gaussian distribution** provides the best fit in 14/15 configurations
* Quantifies when the diffusion approximation is valid vs. when it breaks down

---

### 2. Introduction of the Jump Ratio (New Diagnostic)

[
R_J = \frac{X_0}{\lambda}
]

* A **dimensionless parameter** governing collapse dynamics
* Provides a principled way to classify system behavior

---

### 3. Two-Regime Structure of Collapse Dynamics

* **Drift-dominated regime** (diffusion-valid, IG dominant)
* **Jump-dominated regime** (single-event collapse, diffusion breakdown)

👉 Establishes that regime classification is **inherently two-dimensional**
(dependent on both ( R_J ) and utilization ( \lambda/C ))

---

### 4. Discovery and Mechanistic Explanation of DFR Behavior

* Confirms **Decreasing Failure Rate (DFR)** across all configurations
* Identifies **endogenous survivorship selection** as the mechanism

Key implication:

> Systems that survive longer become *less likely to fail*, contradicting standard reliability assumptions.

---

### 5. Operational Implication (Critical)

* Mean collapse time is **systematically misleading**
* Up to **72% of systems fail before the mean**

👉 Supports transition to:

* Quantile-based risk metrics
* Condition-based monitoring strategies

---

## 📊 Simulation Framework

* 15 configurations:

  * ( \lambda/C \in {0.40, 0.55, 0.70, 0.80, 0.95} )
  * ( \delta \in {0.005, 0.01, 0.02} )

* Per configuration:

  * **50,000 simulated paths**
  * Monte Carlo estimation of collapse times

---

## ⚙️ Reproducibility

### Install dependencies

```bash
pip install -r requirements.txt
```

---

### Run full pipeline

```bash
python src/run_all.py
```

This will:

1. Run all simulations
2. Perform statistical fitting (IG vs Lognormal, etc.)
3. Execute diagnostic analyses
4. Generate all manuscript figures and tables

⏱️ Runtime: ~55–75 minutes

---

## 📁 Repository Structure

```
src/        → Simulation and analysis code  
results/    → Generated figures, tables, raw data  
paper/      → Manuscript and supplementary materials  
docs/       → Model and methodology explanations  
```

---

## 📈 Outputs

The pipeline reproduces:

* Distributional comparisons (IG vs Lognormal)
* Hazard functions and DFR diagnostics
* TTT-transform analysis
* Regime classification maps
* Tail risk and quantile statistics

---

## 🧪 Validation & Robustness

* Independent cross-validation (pure Python implementation)
* Vuong likelihood ratio test
* Mechanism decomposition (overshoot, disruption structure)
* Sensitivity analyses:

  * Buffer size
  * Correlated disruptions
  * Scale invariance

---

## 📄 Paper & Supplementary Material

Available in `/paper`:

* `manuscript.pdf`
* `supplementary.pdf`
* `highlights.txt`

---

## 👤 Author

**Emmanuel Beristain Guzmán**
Logistics Engineer — Supply Chain Optimization & Data Analysis

---

## 📜 License

MIT License

---

## 📌 Citation

```bibtex
@article{beristain2026nearcritical,
  title={Decreasing Failure Rate in Near-Critical Systems},
  author={Beristain Guzmán, Emmanuel},
  year={2026}
}
```
