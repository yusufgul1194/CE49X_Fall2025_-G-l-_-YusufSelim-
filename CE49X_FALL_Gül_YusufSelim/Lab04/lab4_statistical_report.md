# Lab 4: Statistical Analysis Report

## Part 1: Descriptive Statistics (Concrete Strength)

### Five-Number Summary
- **Min:** 21.80 MPa
- **Q1 (25th):** 31.10 MPa
- **Median (50th):** 34.20 MPa
- **Q3 (75th):** 39.12 MPa
- **Max:** 47.10 MPa

### Measures of Central Tendency
- **Mean:** 35.06 MPa
- **Median:** 34.20 MPa
- **Mode:** 31.80 MPa

### Measures of Spread
- **Standard Deviation:** 6.16 MPa
- **Variance:** 37.98 MPa²
- **Range:** 25.30 MPa
- **IQR:** 8.02 MPa

### Measures of Shape
- **Skewness:** 0.047
- **Kurtosis:** -0.675

**Interpretation:**
The mean (35.06) and median (34.20) are very close, and the skewness (0.047) is near zero, suggesting the data is **largely symmetric**. 
The kurtosis (-0.675) is also near zero, indicating a **mesokurtic** shape, similar to a normal distribution.

## Part 2: Probability Modeling Scenarios

### 1. Binomial (Quality Control)
- P(Exactly 3 defects in 100): 13.9576%
- P(5 or fewer defects in 100): 61.5999%

### 2. Poisson (Bridge Load Events)
- P(Exactly 8 trucks in 1 hr): 11.2599%
- P(More than 15 trucks in 1 hr): 4.8740%

### 3. Normal (Steel Yield Strength)
- P(Strength > 280 MPa): 2.2750%
- 95th Percentile Strength: 274.67 MPa

### 4. Exponential (Component Lifetime)
- P(Failure < 500 hours): 39.3469%
- P(Survives > 1500 hours): 22.3130%

## Part 3: Bayes' Theorem Application (Damage Detection)

- **Prior Probability** (P(Damage)): 5.0%
- **Sensitivity** (P(Test+ | Damage)): 95.0%
- **Specificity** (P(Test- | No Damage)): 90.0%
- **Posterior Probability (P(Damage | Test+)): 33.3333%**

**Interpretation:**
Even with a positive test, the probability of the structure actually having damage is only **33.33%**. 
This is because the base rate (prior) of damage is very low (5%). The false positive rate (10%) on the large population of non-damaged structures generates many false alarms.
