# PyTorch Geometric (PyG) on Ray Cluster

## Installation

### Installing Ray on Local Machine

하나의 서버 노드에서 여러 개의 CPU를 활용하려는 경우, 

```
pip install -U "ray[default]"

# If you don't want Ray Dashboard or Cluster Launcher, install Ray with minimal dependencies instead.
# pip install -U "ray"
```

On Mac with Apple Silicon, you should use miniforge:
Please see [M1 Mac (Apple Silicon) Support](https://docs.ray.io/en/latest/ray-overview/installation.html#m1-mac-apple-silicon-support).

1. Install miniforge, a minimal `conda` environment:

```
wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-MacOSX-arm64.sh
bash Miniforge3-MacOSX-arm64.sh
rm Miniforge3-MacOSX-arm64.sh # Cleanup.
```

2. Ensure you're using the miniforge environment and create a new conda environment 

```
source ~/.bash_profile
conda create -n rayenv python=3.12
conda activate rayenv
```

3. Install Ray

```
pip install -U "ray[default]"
```

(Note that you don't need to install PyTorch Geometric. Dependencies will be handled by Ray's Runtime environment. Please see `submit_job.py`.)

### Setting up a Ray Cluster

여러 개의 서버 노드를 사용하려는 경우, [Ray Cluster](https://docs.ray.io/en/latest/cluster/key-concepts.html)를
셋업해야 합니다. (하나의 노드를 사용할 때에도 Single-node Ray Cluster를 셋업하는 게 좋습니다.)

자세한 방법은 [Launching an On-Premise
Cluster](https://docs.ray.io/en/latest/cluster/vms/user-guides/launching-clusters/on-premises.html)를
참고합니다.

#### Manually Set up a Ray Cluster

Start the Head Node:

```
ray start --head --port 26379
```

Start Worker Nodes:

On each of the other nodes, run the following command to connect to the head node you just created:

On macOS:

```
RAY_ENABLE_WINDOWS_OR_OSX_CLUSTER=1 ray start --address=<head-node-address:26379>
```

On Linux:

```
ray start --address=<head-node-address:26379>
```

You can see Ray Web Console at http://<head-node-address:8265>.

## Run

```
conda activate rayenv
python submit_job.py
```

To see the job status, go to http://127.0.0.1:8265 on you web browser.

