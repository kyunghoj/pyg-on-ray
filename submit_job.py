import ray

# Option 2: Using Ray Jobs API (Python SDK)
from ray.job_submission import JobSubmissionClient

HEAD_NODE_IP="127.0.0.1"

# Ref: https://docs.ray.io/en/latest/ray-core/handling-dependencies.html
# This will set up (install) required dependencies for the task
runtime_env = {"pip": ["torch", "torch_geometric"]}

client = JobSubmissionClient(f"http://{HEAD_NODE_IP}:8265")
job_id = client.submit_job(
    entrypoint="python /Users/kjeon/git/pyg-on-ray/pyg_on_ray_example.py",
    runtime_env=runtime_env,
)
