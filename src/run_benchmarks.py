from black_scholes import BlackScholes
from monte_carlo import MonteCarlo
from binomial_tree import BinomialTree

from benchmark import compare_models, save_results

models = [
    BlackScholes(),
    MonteCarlo(simulations=10000),
    BinomialTree(steps=100)
]

# Run benchmark
results = compare_models(models, n=20000)

# Save to CSV
save_results("benchmark_results.csv", results)