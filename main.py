import hydra
from omegaconf import DictConfig

import logging
import argparse

import subprocess

import llamator




@hydra.main(version_base=None, config_path=".", config_name="config")
def main(cfg: DictConfig):
        
##################### Setup LLamator ############################
    url = cfg.api.url
    model = cfg.model.qwen
    temperature = cfg.model.temperature

    attack_model = llamator.ClientOpenAI(
        api_key="lm-studio",
        base_url=url,
        model=model,
        temperature=temperature,
        system_prompts=["You are an attacking model."],
    )

    tested_model = llamator.ClientOpenAI(
        api_key="lm-studio",
        base_url=url,
        model=model,
        temperature=temperature,
        model_description="Model description",
    )

    tests_with_attempts = [
        ("aim_jailbreak", 2),
        ("base64_injection", 2),
        ("bon", 2),
        ("complimentary_transition", 2),
        ("crescendo", 2),
        ("do_anything_now_jailbreak", 2),
        ("RU_do_anything_now_jailbreak", 2),
        ("ethical_compliance", 2),
        ("harmful_behavior_multistage", 2),
        ("linguistic_evasion", 2),
        # ("logical_inconsistencies", 2),
        # ("past_tense", 2),
        # ("suffix", 2),
        # ("sycophancy", 2),
        # ("system_prompt_leakage", 2),
        # ("harmful_behavior", 2),
        # ("typoglycemia_attack", 2),
        # ("RU_typoglycemia_attack", 2),
        # ("ucar", 2),
        # ("RU_ucar", 2)
    ]

    config = {
        "enable_logging": True, "enable_reports": True, 
        "artifacts_path": "./artifacts", "debug_level": 1, 
        "report_language": "ru"
    }

    llamator.start_testing(
            attack_model=attack_model,
            tested_model=tested_model,
            config=config,
            tests_with_attempts=tests_with_attempts,
            multistage_depth=20,
    )

##################### Setup Garak ############################


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    main()