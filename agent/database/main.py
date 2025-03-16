from agent.database.retriever import Retriever

import logging



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    retriever = Retriever(device=0)
