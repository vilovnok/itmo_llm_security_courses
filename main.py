import hydra
from omegaconf import DictConfig

import logging
import argparse

import subprocess


from garak.generators.rest import RestGenerator

from agent.vllm.openai_client import OpenAIClient

from agent.llamator.adaptor import Llamator
# from agent.garak.adaptor import Garak

@hydra.main(version_base=None, config_path=".", config_name="config")
def adapterLlamator(cfg: DictConfig):
    
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

    client = Llamator(config=config,
                      tests_with_attempts=tests_with_attempts, **cfg)    
    client.run()





##################### Setup Garak ############################
@hydra.main(version_base=None, config_path=".", config_name="config")
def garak_run(cfg: DictConfig):
        clinet = OpenAIClient(cfg.model.cotype, cfg.api.openai_key, cfg.model.portV2)                
        text = clinet.invoke(prompt='Отвечай высокомерно.', content='ЧТо самое главное в человеке?')



        def run_garak(config_file="config.yml"):
            try:
                result = subprocess.run(["garak", "--config", config_file],
                                        capture_output=True, text=True)
                
                print("[INFO] Garak Output:")
                print(result.stdout)
                print("[ERROR] Garak Errors:")
                print(result.stderr)

            except Exception as e:
                print(f"[ERROR] Failed to run Garak: {e}")



        # generator = RestGenerator(
        #     uri=f"http://localhost:{cfg.model.portV1}/v1"
        # )
        
        # generator.config = {
        #     "request_json": {
        #         "text": "$INPUT"
        #     },
        #     "method": "POST",
        #     "response_field": "text"
        # }

        # response = generator.generate("Привет, как дела?")
        # print(response)



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    
    # parser = argparse.ArgumentParser()
    # parser.add_argument("--type", type=str, required=True)    
    
    # llamator_run()
    # garak_run()
    adapterLlamator()