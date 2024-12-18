"""
A simple PyTorch Geometric test code
Dependency: pip install torch_geometric
"""

import torch
from torch_geometric.data import Data

edge_index = torch.tensor([[0, 1, 1, 2],
                           [1, 0, 2, 1]], dtype=torch.long)
x = torch.tensor([[-1], [0], [1]], dtype=torch.float)

data = Data(x=x, edge_index=edge_index)

print(data)

# This should print:
# Data(edge_index=[2, 4], x=[3, 1])
