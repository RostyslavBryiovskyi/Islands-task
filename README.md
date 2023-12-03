# Island Counting Algorithm

## Overview

This Python algorithm calculates the number of islands in a map represented by a matrix. In this context, '1' denotes land (island), and '0' denotes the ocean. The algorithm uses Depth-First Search (DFS) to traverse the matrix and count the distinct islands.

*Note*: All presented code was performed with Python 3.8.10.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)

## Installation

1. **Clone the repository:**

```bash
git clone hhttps://github.com/RostyslavBryiovskyi/Islands-task.git
cd Islands-task
```

2. **Install the requirements:**
```bash
pip install -r requirements.txt
```

## Usage
In order to run the code, specify matrix values over "," and row with columns:
```bash
python islands_task.py --matrix 0,1,0,0,0,0,0,1,1 --rows 3 --columns 3
```

This will generate matrix in next format:
```code
[[0 1 0]
 [0 0 0]
 [0 1 1]]
 ```
and return number of islands