from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_groq import ChatGroq
# make sure your prompt template has *both* {context} and {input}
from src.prompt_template import get_anime_prompt

class AnimeRecommender:
    def __init__(self, retriever, api_key: str, model_name: str):
        self.llm = ChatGroq(api_key=api_key, model_name=model_name, temperature=0.1)
        self.prompt = get_anime_prompt()

        # 1) Chain that stuffs retrieved docs into the prompt and calls the LLM
        self.docs_chain = create_stuff_documents_chain(self.llm, self.prompt)

        # 2) Retrieval chain = retriever + docs_chain
        self.qa_chain = create_retrieval_chain(retriever, self.docs_chain)

    def get_recommendation(self, user_input: str) -> str:
        result = self.qa_chain.invoke({"input": user_input})
        # result["answer"] is the model output; result["context"] is a list[Document]
        return result["answer"]