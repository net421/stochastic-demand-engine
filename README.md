# Near-Critical Systems: Inverse Gaussian First-Passage Dynamics

📄 **Paper:** *(manuscript currently under review; PDF available in `/paper`)*
📊 **Field:** Operations Research · Reliability Engineering · Stochastic Processes
⚙️ **Reproducibility:** Full simulation pipeline included

---

## 🔬 Overview

This repository contains a fully reproducible computational framework for analyzing **first-passage collapse dynamics** in capacity-constrained systems operating near their stability boundary.

We study systems governed by:

* Demand: ( D(t) \sim \text{Poisson}(\lambda) )
* Disruptions: ( B(t) \sim \text{Bernoulli}(1 - p) )
* State evolution:

[
I(t+1) = I(t) + B(t)\cdot C - D(t)
]

Collapse occurs at the first-passage time:
[
\tau = \min { t : I(t) < -X_0 }
]

---

## 🧠 Key Contributions

* **Inverse Gaussian (IG)** emerges as the dominant distribution in drift-dominated regimes
* Introduction of the **jump ratio**:

[
R_J = \frac{X_0}{\lambda}
]

* Identification of **two collapse regimes**:

  * Drift-dominated (diffusion-valid)
  * Jump-dominated (diffusion breakdown)

* Demonstration of **Decreasing Failure Rate (DFR)** across all configurations

* Proof that **mean collapse time is misleading** for risk assessment

---

## 📊 Main Results

* IG provides best fit in **14/15 configurations**
* Hazard function strictly decreasing (Spearman ( \rho < -0.93 ))
* Mean residual life increases up to **6.5× conditional survival**
* **72% of systems fail before the mean collapse time**

---

## ⚙️ Reproducibility

### Requirements

```bash
pip install -r requirements.txt
```

Dependencies are strictly pinned for reproducibility.

---

### Full Pipeline Execution

```bash
python src/run_all.py
```

**Pipeline includes:**

1. Primary simulation (50,000 paths × 15 configurations)
2. Vuong likelihood ratio tests
3. Diagnostic decomposition (CDF, hazard, mechanisms)
4. Supplementary analyses
5. Cross-validation (independent implementation)
6. Figure generation (publication-quality)

⏱️ **Total runtime:** ~55–75 minutes

---

## 📁 Repository Structure

```
near-critical-systems/
├── src/        # Simulation and analysis code
├── results/    # Figures, tables, raw data
├── paper/      # Manuscript and supplementary materials
├── docs/       # Model and methodology documentation
```

---

## 🔁 Simulation Design

* Capacity: ( C = 100 )
* Buffer: ( X_0 = 50 )

Parameter space:

* Utilization: ( \lambda/C \in {0.40, 0.55, 0.70, 0.80, 0.95} )
* Supercritical margin: ( \delta \in {0.005, 0.01, 0.02} )

Total configurations: **15**
Total simulations per configuration: **50,000 paths**

---

## 📈 Generated Outputs

The pipeline produces:

* Distributional fits (IG vs Lognormal)
* Hazard function estimates
* TTT-transform diagnostics
* Regime classification map
* Tail risk and quantile tables

All outputs are stored in `/results`.

---

## 🧪 Validation & Robustness

* Independent **pure-Python cross-validation**
* **Vuong likelihood decomposition**
* Mechanism-level analysis (overshoot, disruption structure)
* Sensitivity analyses:

  * Buffer size
  * Correlated disruptions (Gilbert–Elliott)
  * Scale invariance

---

## 🧠 Practical Implications

* Age-based maintenance is **suboptimal under DFR dynamics**
* Systems exhibit **endogenous survivorship selection**
* **Condition-based monitoring is theoretically justified**
* Quantile-based metrics outperform mean-based decision rules

---

## 📄 Paper & Supplementary Material

Located in `/paper`:

* `manuscript.pdf` — Main article
* `supplementary.pdf` — Extended results and validation
* `highlights.txt` — Key findings

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
  title={Decreasing Failure Rate in Near-Critical Systems: Inverse Gaussian First-Passage Dynamics},
  author={Beristain Guzmán, Emmanuel},
  year={2026}
}
```

