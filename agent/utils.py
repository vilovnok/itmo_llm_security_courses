import re
import os
import pandas as pd


class PromptSanitizer:
    def __init__(self):
        pass
    def __sanitize(self, input_text: str, delimiter: str):
        """Удаляет опасные конструкции из текста."""

        sanitized_user_input = input_text.replace(delimiter, "")
        return f"{delimiter}\n{sanitized_user_input}\n{delimiter}"
    
    def __remove_hashes(self, input_text: str):
        cleaned_text = re.sub(r"[^\w\s\n]", "", input_text)
        return cleaned_text
    
    def fix_response(self, content: str):
        """Проверяет текст на соответствие правилам."""
        return re.sub(r'Answer.*|###.*', '', content, flags=re.DOTALL)
    
    def get_completion_from_messages(self, input_text, delimiter):
        """Проводит полную обработку текста."""

        cleaned_text = self.__remove_hashes(input_text=input_text)
        return self.__sanitize(cleaned_text, delimiter)


class CustomDataset:
    def __init__(self, directory='./dataset', chunk_size=300, overlap=50):
        
        self.directory = directory
        self.chunk_size = chunk_size
        self.overlap = overlap
        self.data = []
    
    def read_files(self):
        """Читает все .txt файлы из указанной директории."""
        for file_name in os.listdir(self.directory):
            if file_name.endswith(".txt"):
                file_path = os.path.join(self.directory, file_name)
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read()
                    self.data.append((file_name, content))

    def create_chunks(self):
        """Разбивает содержимое файлов на чанки фиксированного размера с перекрытием."""
        chunked_data = []
        for file_name, content in self.data:
            for i in range(0, len(content) - self.overlap, self.chunk_size - self.overlap):
                chunk = content[i:i+self.chunk_size]
                chunked_data.append((file_name, chunk))
        self.data = chunked_data

    def convert2df(self):
        """Преобразует данные в pandas DataFrame."""
        df = pd.DataFrame(self.data, columns=["filename", "text_chunk"])
        df['len_chunk'] = df["text_chunk"].apply(lambda x: len(x))
        df.to_csv('dataset.csv', index=False)
        return df
