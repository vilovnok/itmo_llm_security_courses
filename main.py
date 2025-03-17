import hydra
from omegaconf import DictConfig

# from agent.garak.adaptor import Garak
from agent.llamator.adaptor import Llamator
from agent.vllm.openai_client import OpenAIClient
from agent.database.retriever import Retriever

from agent.prompts import system_prompt, injection_prompt, simple_prompt

import logging



##################### Setup Llamator ############################
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

    client = Llamator(config=config, tests_with_attempts=tests_with_attempts, **cfg)    
    client.run()


##################### Setup Garak ############################
@hydra.main(version_base=None, config_path=".", config_name="config")
def adapterGarak(cfg: DictConfig):
    client = Garak(**cfg)    
    client.run()


##################### Setup Custom ############################
@hydra.main(version_base=None, config_path=".", config_name="config")
def adaptorCustom(cfg: DictConfig):
    model = cfg.model.qwen
    openai_key = cfg.api.openai_key
    port = cfg.model.portV1

    client = OpenAIClient(model=model, openai_key=openai_key, port=port)
    text = client.ChatCompletion(prompt=system_prompt, content=injection_prompt)
    
    print(text)
    return text


##################### Setup RAG ############################
@hydra.main(version_base=None, config_path=".", config_name="config")
def RAG(cfg: DictConfig):
    
    model_name = cfg.embeddings.model_name
    model_tag = cfg.embeddings.model_tag
    collection_name = cfg.embeddings.collection_name

    retriever = Retriever(device=0)

    ## создание базы
    # dense_embeddings = {}
    # dense_embeddings[model_name] = retriever.encode(text='Hello, world', model_name=model_name)        

    # retriever.create_database(       
    #     model_name=model_name,  
    #     dense_embeddings=dense_embeddings,
    #     collection_name=database_name
    # )

    # retriever.upload_db(collection_name=database_name, model_name=model_name)
    
    ## поиск в базе
    items = retriever.search(collection_name=collection_name, 
                    model_tag=model_tag, 
                    model_name=model_name, 
                    score_threshold=0.6,
                    query='С какой планеты исходил сигнал бедствия ?')

    print(items)
    ## удаление базы
    # retriever.delete_database(collection_name=database_name)




if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    
    # adapterLlamator()
    # adapterGarak()
    # adaptorCustom()

    RAG()