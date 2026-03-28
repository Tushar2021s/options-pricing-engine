# benchmark.py
import csv
import time

def benchmark(model, n=10000):
    import time

    S, K, T, r, sigma = 100, 100, 1, 0.05, 0.2

    start = time.perf_counter()

    for _ in range(n):
        model.price(S, K, T, r, sigma)

    end = time.perf_counter()

    total_time = end - start
    ops_per_sec = n / total_time

    return model.__class__.__name__, ops_per_sec

def compare_models(models, n=10000):
    results = []

    for model in models:
        name, ops = benchmark(model, n)

        print(f"{name}: {ops:.2f} ops/sec")
        results.append((name, ops))

    return results
def latency_test(model, runs=1000):
    """
    Measure latency per call (microseconds)
    """
    S, K, T, r, sigma = 100, 100, 1, 0.05, 0.2

    times = []

    for _ in range(runs):
        start = time.perf_counter()
        model.price(S, K, T, r, sigma)
        end = time.perf_counter()

        times.append((end - start) * 1e6)  # microseconds

    avg_latency = sum(times) / len(times)

    print(f"{model.__class__.__name__} Latency:")
    print(f"Average: {avg_latency:.4f} µs")
    print(f"Min: {min(times):.4f} µs")
    print(f"Max: {max(times):.4f} µs")
    print("-" * 40)

def latency_percentiles(model, runs=5000):
    import numpy as np

    S, K, T, r, sigma = 100, 100, 1, 0.05, 0.2

    times = []

    for _ in range(runs):
        start = time.perf_counter()
        model.price(S, K, T, r, sigma)
        end = time.perf_counter()

        times.append((end - start) * 1e6)

    times = np.array(times)

    print(f"{model.__class__.__name__} Latency Percentiles:")
    print(f"P50: {np.percentile(times, 50):.4f} µs")
    print(f"P90: {np.percentile(times, 90):.4f} µs")
    print(f"P99: {np.percentile(times, 99):.4f} µs")
    print("-" * 40)


def save_results(filename, data):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)

        # Header
        writer.writerow(["Model", "Ops_per_sec"])

        # Data rows
        for name, ops in data:
            writer.writerow([name, ops])