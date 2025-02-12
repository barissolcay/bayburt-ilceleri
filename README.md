# Bayburt İlçeleri Network Analysis

This project analyzes the network structure of villages (köyler) in Bayburt province, Turkey, using network analysis techniques. The project uses distance data between villages to create a graph structure and calculate various centrality metrics.

## Project Overview

The project consists of two main files:
- `bayburt_ilceleri.csv`: Contains the distance data between villages
- `final_projesi.py`: Python script that performs the network analysis

### Features

The analysis includes:
1. Basic network metrics:
   - Number of nodes (villages)
   - Number of edges (connections)
   - Average degree

2. Centrality measures:
   - Degree centrality
   - Closeness centrality
   - Betweenness centrality
   - Eigenvector centrality

3. Community detection using the Girvan-Newman algorithm

## Requirements

The project requires the following Python libraries:
- NetworkX
- Pandas

To install the required libraries:

    pip install networkx pandas

## Data Structure

The `bayburt_ilceleri.csv` file contains three columns:
- Koy1: First village name
- Koy2: Second village name
- Mesafe: Distance between the villages in kilometers

## Usage

1. Clone the repository:

    git clone https://github.com/barissolcay/bayburt-ilceleri.git
    cd bayburt-ilceleri

2. Run the analysis script:

    python final_projesi.py

## Output

The script outputs:
1. Network metrics (number of nodes, edges, and average degree)
2. Shortest path lengths between all pairs of villages
3. Top 5 villages with highest:
   - Degree centrality
   - Closeness centrality
   - Betweenness centrality
   - Eigenvector centrality
4. Community structure of the village network

## Contributing

Feel free to open issues or submit pull requests if you have suggestions for improvements or find any bugs.

## License

MIT License

Copyright (c) 2025 Baris Solcay

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Author

[Baris Olcay](https://github.com/barissolcay)
