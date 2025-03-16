import llamator


class Llamator:
    def __init__ (self, config, tests_with_attempts, **cfg):

        self.config = config
        self.tests_with_attempts = tests_with_attempts

        self.__setup_llamator(**cfg) 


    def __setup_llamator(self, **cfg):
        attack_model = cfg.get('model', {}).get('qwen', None)
        tested_model = cfg.get('model', {}).get('cotype', None)
        temperature = cfg.get('model', {}).get('temperature', None)
        
        portV1 = cfg.get('model', {}).get('portV1', None)
        portV2 = cfg.get('model', {}).get('portV2', None)

        attack_url = f"http://localhost:{portV1}/v1" if portV1 else None
        tested_url = f"http://localhost:{portV2}/v1" if portV1 else None
 
 
        attack_model=tested_model
        tested_url=attack_url
        
        self.attack_model = llamator.ClientOpenAI(
            api_key="lm-studio",
            base_url=attack_url,
            model=attack_model,
            temperature=temperature,
            system_prompts=["You are an attacking model."],
        )

        self.tested_model = llamator.ClientOpenAI(
            api_key="lm-studio",
            base_url=tested_url,
            model=tested_model,
            temperature=temperature,
            model_description="Model description",
        )                 

    def run(self):        
        llamator.start_testing(
                attack_model=self.attack_model,
                tested_model=self.tested_model,
                config=self.config,
                tests_with_attempts=self.tests_with_attempts,
                multistage_depth=20,
        )
