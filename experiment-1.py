import TrieArray, TrieBST, TrieList
from pympler import asizeof
import re
import time
import numpy as np


def process_text(source):
    """Process the input text file to filter and prepare word list."""
    with open(source, 'r', encoding='utf-8') as file:
        text = file.read().lower()
        text = re.sub('[^a-z ]+', ' ', text)
        words = text.split()
        filtered_words = {w for w in words if len(w) >= 3}

    with open('dictionary.txt', 'w', encoding='utf-8') as file:
        for w in sorted(filtered_words):
            file.write(w + '\n')

    return filtered_words


def run_experiment(trie_class, words):
    """Run experiment for a specific trie class and return stats."""
    times = []
    memory_usages = []

    for _ in range(10):
        trie = trie_class()
        start_time = time.time()
        for word in words:
            trie.insert(word)
        end_time = time.time()

        times.append((end_time - start_time) * 1000)
        memory_usages.append(asizeof.asizeof(trie) / (1024 ** 2))

    return {
        'Mean Time (ms)': np.mean(times),
        'Time Std Dev (ms)': np.std(times),
        'Mean Memory (MB)': np.mean(memory_usages),
        'Memory Std Dev (MB)': np.std(memory_usages)
    }


def main():
    source = 'shakespeare.txt'
    words = process_text(source)
    trie_types = [TrieArray.TrieArray, TrieList.TrieList, TrieBST.TrieBST]
    results = {}

    for t in trie_types:
        results[t.__name__] = run_experiment(t, words)

    # Print results
    for trie_name, metrics in results.items():
        print(f"{trie_name}:")
        print(
            f"  Mean Time: {metrics['Mean Time (ms)']:.2f} ms, Time Std Dev: {metrics['Time Std Dev (ms)']:.2f} ms")
        print(
            f"  Mean Memory Usage: {metrics['Mean Memory (MB)']:.2f} MB, Memory Std Dev: {metrics['Memory Std Dev (MB)']:.2f} MB")


if __name__ == "__main__":
    main()
