import llamator



class Llamator:
    def __init__ (self, config, tests_with_attempts, **cfg):

        self.config = config
        self.tests_with_attempts = tests_with_attempts

        self.__setup_llamator(**cfg)


    def __setup_llamator(self, **cfg):
        attack_model = cfg.model.qwen
        tested_model = cfg.model.cotype
        temperature = cfg.model.temperature
        
        portV1 = cfg.model.portV1
        portV2 = cfg.model.portV2

        attack_url = f"http://localhost:{portV1}/v1"
        tested_url = f"http://localhost:{portV2}/v1"   

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
