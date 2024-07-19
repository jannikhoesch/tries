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

## Tries
Tries are a specialized type of search tree used primarily for managing strings over an alphabet. Characterized by their unique ability to quickly retrieve, insert, or delete keys based on their common prefixes, tries are particularly useful for tasks that involve large sets of strings and require efficient prefix-based querying. I will briefly describe each of the trie types used in the experiments in terms of their characteristic data structure, the resulting advantages and disadvantages, and provide an implementation of a node to demonstrate the architecture. In my implementation I added to each word that was added to a trie ’#’ as a special character to indicate the end of a word in the trie. This ensures that no added word is the prefix of another word.

![image](https://github.com/user-attachments/assets/f8797cc0-b190-4881-9061-6a77f7d8b1ec)

### Array-Trie
Array Tries use a fixed-size array to represent the children of each node. Each slot in the array corresponds to a possible character from the trie’s alphabet, allowing direct access to children based on character values. In the experiment, I used an array of length 27 to capture every lowercase letter of the English alphabet and additionally the special character ’#’. This structure provides fast lookup for each character of the key being searched, inserted, or deleted. The primary advantage is fast access speeds, but this can come at the cost of higher memory consumption, especially if the trie is sparsely populated.

### List-Trie
List Tries utilize a linked list like structure to store children at each node. Each node has a pointer to their first child and their next sibling, if they exist. The siblings are kept in alphabetical order. Therefore, List Tries only allocate space for characters that actually appear in the words, which can significantly reduce memory usage when dealing with a large but sparsely used alphabet. This approach is more space-efficient with unpredictable data sets.

### BST-Trie
Binary Search Tree Tries, or Ternary Search Tries (TSTs), enhance the basic trie structure by organizing characters at each node into a binary search tree format. Each node in a TST contains three pointers: left, center, and right, corresponding to characters less and greater than the node’s character. The center pointer leads to the next character of the key, enabling shared prefix management. TSTs often need less memory than the other trie types, which comes with less time efficiency.

## Experiments
The experiments were performed on an Apple MacBook Air equipped with the Apple M2 chip and 8 GB of RAM. As programming environment I chose PyCharm with Python version 3.10.

### Structured Data
The first experiment measures the time and space required to insert a set of words into each of the different trie variants. I used the text ”Shakespeare’s Complete Works” from Project Gutenberg as source to extract the words 1. I converted all letters to lowercase, removed all non-alphabetic characters, splitted the text into words and removed all words of less than three letters, which resulted in a dictionary of 24.324 distinct word. For each trie type, these words were inserted measuring the time to construct the trie and the space of the resulting trie. The generation of each trie was done 30 times to reliably calculate means and deviations.

### Randomized Data
The second experiment aims to assess the performance of the trie variants when managing randomly generated data. It focuses on analyzing the trie’s behavior under conditions of synthetic, unique string insertions and calculates the associated search costs. Words were generated by starting with a three-letter base, which is expanded randomly until the word does not match any existing entry in the trie, ensuring all words are unique. After each word is inserted, it is immediately searched in the trie to measure the successful search cost - the number of steps taken to confirm the word’s presence. To measure the unsuccessful search cost - the number of steps taken to confirm that the word is not present - I added more characters to the previously generated and inserted word until they became unique. Then I searched these non-existent words in the trie to measure the cost of the unsuccesful search. During insertion of words a counter keeps track of the number of nodes in the trie. After all words are added this counter can be accessed to get the final number of nodes. The experiment is repeated for varying sizes of the dataset, from 10 to 10000 words in increments of 100. For each size, the experiment is conducted 5 times to calculate average values and standard deviations for successful search costs, unsuccessful search costs, and the number of nodes. Additionally I measured the time and space of the tries to test the results of the first experiment.

## Results
The results from Experiment 1 show the trade-offs between time efficiency and memory usage among the trie types: 
- TrieArraywhile quite fast, consumes the most memory
- TrieList: very fast and least memory consuming
- TrieBST: quite slow, but uses reasonable amount of memory
