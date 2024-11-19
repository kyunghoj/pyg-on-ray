"""
A simple test code for PyTorch Geometric (PyG) on Ray 
"""

import ray
import time

@ray.remote
def my_pyg_function(i) -> int:
    print(f"Worker {i} starts... ")
    import torch
    from torch_geometric.data import Data
    edge_index = torch.tensor([[0, 1, 1, 2],
                               [1, 0, 2, 1]], dtype=torch.long)
    x = torch.tensor([[-1], [0], [1]], dtype=torch.float)
    data = Data(x=x, edge_index=edge_index)
    time.sleep(10)
    print(f"Worker {i} ends...")
    return i

if __name__ == "__main__":
    futures = [my_pyg_function.remote(i) for i in range(16)]
    for f in futures:
        print(f"{ray.get(f)}")
