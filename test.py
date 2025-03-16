import hydra
from omegaconf import DictConfig

from agent.vllm.openai_client import OpenAIClient
from agent.prompts import system_prompt, injection_prompt, simple_prompt


from agent.utils import CustomDataset

# @hydra.main(version_base=None, config_path=".", config_name="config")
# def test(cfg: DictConfig):
#     model = cfg.model.qwen
#     openai_key = cfg.api.openai_key
#     port = cfg.model.portV1

#     client = OpenAIClient(model=model, openai_key=openai_key, port=port)
#     text = client.ChatCompletion(prompt=system_prompt, content=injection_prompt)
#     print(text)
    
#     return text

# test()



# Пример использования
dataset = CustomDataset("./dataset", chunk_size=300)
dataset.read_files()
dataset.create_chunks()
df = dataset.convert2df()
print(df.head())










# from vllm import LLM, SamplingParams
# import torch
# import os
# os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"   # see issue #152
# os.environ["CUDA_VISIBLE_DEVICES"]="3,4"

# def is_chinese_token(token_id, tokenizer):
#     token = tokenizer.decode([token_id])
#     return any('\u4e00' <= char <= '\u9fff' for char in token)

# class ChineseTokenFilter:
#     def __init__(self, tokenizer):
#         self.tokenizer = tokenizer
#         self.chinese_token_ids = [
#             token_id for token_id in range(tokenizer.vocab_size)
#             if is_chinese_token(token_id, tokenizer)
#         ]

#     def __call__(self, input_ids, scores):
#         scores[self.chinese_token_ids] = float('-inf')
#         return scores

# max_seq_length=1024*8
# llm = LLM(
#     model=safename, 
#     trust_remote_code=True, 
#     max_seq_len_to_capture=max_seq_length,
#     max_model_len=max_seq_length,
#     dtype=torch.float16,
#     gpu_memory_utilization=0.99,
#     tensor_parallel_size=2,
# )

# sampling_params_logits = SamplingParams(
#     temperature=0.7,
#     top_k=50,
#     top_p=0.95,
#     max_tokens=100,#max_seq_length,
#     seed=42,
#     stop=['<|im_end|>', '<|eot_id|>'],

#     logits_processors=[ChineseTokenFilter(llm.get_tokenizer())]
# )

# def get_answer(messages):
#     answer =  llm.generate(
#         messages,
#         sampling_params_logits,
#     )[0].outputs[0].text
#     return answer

# message = "Все преграды одолев, бьёт преграды верный"
# prompts = ["<|im_start|>user\n"+
#            message+
#            "<|im_end|>\n<|im_start|>assistant\n"]
# get_answer(prompts)