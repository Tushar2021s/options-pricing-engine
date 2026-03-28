# Options Pricing Engine

A modular and performance-focused **options pricing engine** implementing core quantitative finance models, numerical methods, and benchmarking tools.

Built to simulate real-world derivatives pricing systems with emphasis on **clean architecture, numerical stability, and performance analysis**.

---

## Key Features

### Pricing Models
- Black-Scholes (Analytical)
- Monte Carlo Simulation
- Binomial Tree (CRR Model)

### Greeks Engine
- Delta, Gamma, Vega, Theta, Rho
- Supports both analytical and numerical computation

### Implied Volatility Solver
- Newton-Raphson method for fast convergence  
- Bisection fallback for robustness  
- Handles convergence edge cases gracefully  

### Volatility Smile
- Strike vs Implied Volatility analysis  
- Visualizes market skew and smile patterns  

---

## System Design

- Abstract base class: `PricingModel`
- Centralized engine: `PricingEngine`
- Plug-and-play model architecture  
- Clean modular structure (`src/` based)

---

## Performance Benchmarking

- Throughput (operations/sec)  
- Latency (µs per call)  
- Percentile metrics (P50, P90, P99)  
- CSV export for further analysis  

---

## Project Structure

```
options-pricing-engine/
│
├── src/
│   ├── black_scholes.py
│   ├── monte_carlo.py
│   ├── binomial_tree.py
│   ├── pricing_model.py
│   ├── pricing_engine.py
│   ├── implied_volatility.py
│   ├── greeks.py
│   ├── volatility_smile.py
│   ├── benchmark.py
│   ├── run_benchmarks.py
│   ├── main.py
│   └── benchmark_results.csv
│
├── tests/
├── requirements.txt
└── README.md
```

---

## Example Usage

```python
from pricing_engine import PricingEngine
from black_scholes import BlackScholes

engine = PricingEngine(BlackScholes())

price = engine.price(100, 100, 1, 0.05, 0.2)

print("Option Price:", price)
```

---

## Benchmarking

Run:

```bash
python src/run_benchmarks.py
```

### Outputs include:
- Operations per second  
- Latency (microseconds)  
- Percentiles (P50, P90, P99)  
- CSV results for deeper analysis  

---

## Highlights

- Implements industry-standard derivatives pricing models  
- Includes Greeks and implied volatility computation  
- Demonstrates numerical methods (root finding, simulation)  
- Designed with modular and extensible architecture  
- Includes performance and latency benchmarking  
- Supports volatility smile analysis  

---

## Future Improvements

- Monte Carlo optimization (vectorization, variance reduction)  
- Volatility surface (3D visualization)  
- Real market data integration  
- Parallel / multi-threading support  
- Portfolio-level risk engine  

---

## Tech Stack

- Python  
- NumPy  
- SciPy  

---

## Motivation

This project bridges **quantitative finance theory** and **real-world system design**, focusing on:

- Performance  
- Extensibility  
- Numerical robustness  