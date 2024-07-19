# Empirical Study of Tries

This repository contains a university project that I created for the course Advanced Data Structures at the Universitat Politècnica de Catalunya. The goal is to implement an conduct experiments with three different trie structures: Array-Trie, List-Trie, and BST-Trie (TST).

Tries are essential in many applications due to their efficiency in handling prefix- based searches and large text datasets. The goal is to measure and compare the performance across these trie types. In the first experiment, I will measure the time and space efficience of the tries using a word dictionary from a real text. In the second experiment, I will evaluate the total successful and unsuccessful search costs and node efficiency using synthetically generated strings. This report will offer insights into the practical applications and performance optimization of trie structures.


## Usage
### Repository Contents
- `TrieArray.py`, `TrieList.py`, `TrieBST.py`: Implementations of each Trie type.
- `shakespeare.txt`: Text file used as the source for word extraction in experiment 1.
- `experiment-1.py`: Script that includes functions to run experiment 1.
- `experiment-2.py`: Script that includes functions to run experiment 2.
- `requirements.txt`: Python dependencies required for running the experiments.
- `README.md`: This file.

### How to Run

Ensure you have Python 3.7+ installed on your system.

- Install dependencies:
   ```sh
   pip install -r requirements.txt

- To start experiment 1, run:
    ```sh
    python experiment-1.py
  
- To start experiment 2, run:
    ```sh
    python experiment-2.py

## Usage
