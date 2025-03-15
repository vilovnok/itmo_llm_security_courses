import garak
import subprocess


class Garak:
    def __init__ (self, **cfg):

        self.__setup_garak(**cfg)

    def __setup_garak(self, **cfg):
        qwen_model = cfg.get('model', {}).get('qwen', None)
        cotype_model = cfg.get('model', {}).get('cotype', None)
        
        self.commands = [
            [
                "python3", "-m", "garak",
                "--model_type", "huggingface",
                "--model_name", f"{qwen_model}",
                "--probes", "promptinject.HijackHateHumans,realtoxicityprompts.RTPInsult,xss.MarkdownImageExfil"
            ],
            [
                "python3", "-m", "garak",
                "--model_type", "huggingface",
                "--model_name", f"{cotype_model}",
                "--probes", "promptinject.HijackHateHumans,realtoxicityprompts.RTPInsult,xss.MarkdownImageExfil"
            ]
        ]

    def run(self):        
        for cmd in self.commands:
            try:
                cmdod = ' '.join(cmd)
                result = subprocess.run(cmd, capture_output=True, text=True, check=True)
                print("✅ STDOUT:", result.stdout)
                print("🛑 STDERR:", result.stderr)
                print(cmdod)
                print("🔚 Код завершения:", result.returncode)
            except subprocess.CalledProcessError as e:
                print(f"❌ Ошибка при выполнении команды: {e}")
            except Exception as e:
                print(f"❌ Неизвестная ошибка: {e}")
            finally:
                print("-" * 40)