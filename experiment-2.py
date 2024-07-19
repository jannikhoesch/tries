import TrieArray, TrieBST, TrieList
import random
import string
import numpy as np
import matplotlib.pyplot as plt
from pympler import asizeof
import time


def generate_unique_word(trie, length=3, word=None):
    """Generate a unique word not already in the trie."""
    if word is None:
        word = ''.join(random.choices(string.ascii_lowercase, k=length))

    while True:
        found, cost = trie.search(word)
        if not found:
            return word, cost
        word += random.choice(string.ascii_lowercase)


def run_experiment(trie_class, n_words):
    """Run a single experiment for a given trie type and number of words."""
    trie = trie_class()
    total_successful_search_cost = 0
    words = []
    start_time = time.time()

    for _ in range(n_words):
        word, cost = generate_unique_word(trie)
        trie.insert(word)
        words.append(word)
        total_successful_search_cost += cost

    total_unsuccessful_search_cost = 0
    for w in words:
        false_word = generate_unique_word(trie, None, w)
        _, cost = trie.search(false_word[0])
        total_unsuccessful_search_cost += cost

    time_taken = time.time() - start_time
    num_nodes = trie.node_count
    memory_usage = asizeof.asizeof(trie)

    return total_successful_search_cost, total_unsuccessful_search_cost, num_nodes, time_taken, memory_usage


def collect_data(n_range, trie_types, repetitions=5):
    """Collect experiment data across a range of input sizes and trie types."""
    results = {trie.__name__: {'successful search cost': [], 'unsuccessful search cost': [], 'number of nodes': [], 'time': [], 'memory usage': []} for trie in trie_types}

    for n in n_range:
        print(f"Running experiments for {n} words...")
        for trie_class in trie_types:
            succ_costs, unsucc_costs, nodes, times, memories = [], [], [], [], []
            for _ in range(repetitions):
                succ_cost, unsucc_cost,  node_count, time_taken, memory = run_experiment(trie_class, n)
                succ_costs.append(succ_cost)
                unsucc_costs.append(unsucc_cost)
                nodes.append(node_count)
                times.append(time_taken)
                memories.append(memory)

            trie_name = trie_class.__name__
            results[trie_name]['successful search cost'].append((np.mean(succ_costs), np.std(succ_costs)))
            results[trie_name]['unsuccessful search cost'].append((np.mean(unsucc_costs), np.std(unsucc_costs)))
            results[trie_name]['number of nodes'].append((np.mean(nodes), np.std(nodes)))
            results[trie_name]['time'].append((np.mean(times), np.std(times)))
            results[trie_name]['memory usage'].append((np.mean(memories), np.std(memories)))

    return results


def plot_results(n_range, results, metrics):
    """Plot results for each metric."""
    plt.figure(figsize=(12, 8))
    for metric in metrics:
        plt.clf()
        for trie_name, data in results.items():
            means, stds = zip(*data[metric])
            plt.plot(n_range, means, label=f'{trie_name} - {metric}')
            plt.fill_between(n_range, np.array(means) - np.array(stds), np.array(means) + np.array(stds), alpha=0.2)
        plt.xlabel('Number of Words (n)')
        plt.ylabel(metric)
        plt.title(f'Performance Analysis: {metric}')
        plt.legend()
        plt.grid(True)
        plt.show()


def main():
    trie_types = [TrieArray.TrieArray, TrieList.TrieList, TrieBST.TrieBST]
    n_range = range(10, 10000, 100)
    results = collect_data(n_range, trie_types, 5)
    plot_results(n_range, results, ['successful search cost', 'unsuccessful search cost', 'number of nodes', 'time', 'memory usage'])


if __name__ == "__main__":
    main()
