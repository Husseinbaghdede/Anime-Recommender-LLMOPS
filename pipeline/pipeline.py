from src.vector_store import VectorStoreBuilder
from src.recommender import AnimeRecommender
from config.config import GROQ_API_KEY,MODEL_NAME
from utils.logger import get_logger
from utils.custom_exception import CustomException

logger = get_logger(__name__)

class AnimeRecommendationPipeline:
    def __init__(self,persist_directory:str="chroma_db"):
        try:
            logger.info("Initializing the pipeline")
            
            vector_builder = VectorStoreBuilder(csv_path="",persist=persist_directory)
            retriever = vector_builder.load_vector_store().as_retriever()
            
            self.anime_recommender = AnimeRecommender(retriever=retriever,
                                                      api_key=GROQ_API_KEY,model_name=MODEL_NAME)
            
            logger.info("Pipeline initialized successfully")
        except Exception as e:
            logger.error(f"Error occurred while initializing the pipeline:{e}")
            raise CustomException("Error occurred while initializing the pipeline",e)
            
    def recommend(self,query:str)->str:
        try:
            logger.info(f"Query received from user : {query}")
            recommendation = self.anime_recommender.get_recommendation(user_input=query)
            
            
            logger.info(f"Recommended animes are :{recommendation}")
            return recommendation
        except Exception as e:
            logger.error(f"Error occurred while recommending animes:{e}")
            raise CustomException("Error occurred while recommending animes",e)