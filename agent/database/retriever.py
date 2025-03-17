import tqdm

import pandas as pd
from datasets import Dataset

import requests
from typing import List, Union

from torch.cuda import is_available
from qdrant_client import QdrantClient, models
from sentence_transformers import SentenceTransformer

from agent.utils import CustomDataset


class Retriever(CustomDataset):
    def __init__(self,
        localhost: str='0.0.0.0',
        port: int=6333,
        dataset_dir: str='./dataset',
        device: int = None
        ) -> None:
        
        self.dataset_dir = dataset_dir
        
        self._device = 0 if (device is None and is_available()) else device
        self._client = self._setup_database(localhost=localhost, port=port)           


    def _setup_database(self, localhost: str, port: int):        
        if not requests.get(f'http://localhost:6333'):
            raise Exception(f'Qdrant server is not running at http://{localhost}:{port}')
            
        client = QdrantClient(location=localhost, port=6333)
        return client


    def _setup_model(self, model_name: str):                    
        model = SentenceTransformer(model_name, device=self._device)        
        return model
    
    def encode(self, text: Union[List[str], str], model_name: str):
        try:
            embeddings = SentenceTransformer(
                    model_name,
                    device=self._device
                ).encode(text, normalize_embeddings=True)
            
            return embeddings        
        except Exception as err:
            raise Exception(f'Ошибка при кодировании текста: {err}')
        

    def search(
            self,
            query: str,
            model_tag: str,
            model_name: str,
            collection_name: str,
            topk: int = 10,
            filter_options: dict = None,
            score_threshold: float = 0.0
        ):
        try:
            embedding = self.encode(query, model_name=model_name)
            results = self._client.search(
                collection_name=collection_name,
                query_vector=(model_tag, embedding),
                with_payload=True,
                limit=topk,
                query_filter=models.Filter(
                    must=[
                        models.FieldCondition(key=k, match=models.MatchValue(value=v))
                        for k, v in filter_options.items()
                    ]
                ) if filter_options else None,
                score_threshold=score_threshold
            )
            return results
        except Exception as error:
            raise Exception(f'Ошибка при поиске: {error}')

    def create_database(self, 
                        model_name: str,
                        dense_embeddings: list, 
                        collection_name: str='security_db'):
        """ Create the database """
        try:
            if self._client.collection_exists(collection_name=collection_name):
                return
            
            dense_embeddings = {}
            dense_embeddings[model_name] = self.encode(text='Hello, world', model_name=model_name)        

            self._client.create_collection(
                collection_name=collection_name,
                vectors_config={
                    "all-MiniLM-L6-v2":models.VectorParams(
                        size=len(dense_embeddings[model_name]),
                        distance=models.Distance.COSINE
                    )
                }
            )
        except Exception as error:
            raise Exception(f'Ошибка при создании базы: {error}')
        
    def delete_database(self, collection_name: str):
        """ Delete the database """
        try:
            self._client.delete_collection(collection_name=collection_name)
        except Exception as error:
            raise Exception(f'Ошибка при удалении базы: {error}')
        
    def read_files(self):
        pass
        

    def upload_db(self, collection_name: str, model_name: str, batch_size: int=4):
        """ Загружаем данные в базу """

        df = pd.read_csv('dataset.csv').reset_index()
        dataset = Dataset.from_pandas(df)
        dense_embedding_model_MiniLM = self._setup_model(model_name=model_name)

        for batch in tqdm.tqdm(dataset.iter(batch_size=batch_size), total=len(dataset) // batch_size):
            try:
                dense_embeddings_MiniLM = list(dense_embedding_model_MiniLM.encode(batch["text_chunk"]))

                self._client.upload_points(
                    collection_name=collection_name,
                    points=[
                        models.PointStruct(
                            id=int(batch["index"][i]),
                            vector={
                                "all-MiniLM-L6-v2": dense_embeddings_MiniLM[i].tolist()
                            },
                            payload={
                                "text_chunk": batch["text_chunk"][i],
                                "len_chunk": batch["len_chunk"][i]
                            }
                        )
                        for i, _ in enumerate(batch["index"])
                    ],
                    batch_size=batch_size,  
                )
            except Exception as error:
                raise Exception(f'Ошибка при загрузке в базу: {error}')