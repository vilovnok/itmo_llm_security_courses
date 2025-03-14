import hydra
from omegaconf import DictConfig

import subprocess

from huggingface_hub import login


@hydra.main(version_base=None, config_path="../../", config_name="config")
def main(cfg: DictConfig):        
    
    login(token=cfg.model.hf_token)
    
    command = [
        "python", "-m", "vllm.entrypoints.openai.api_server",
        "--model", cfg.model.deepseek,
        "--gpu-memory-utilization", "0.25",
        "--port", str(cfg.model.portV2)
    ]
    subprocess.run(command)

if __name__ == "__main__":
    main()