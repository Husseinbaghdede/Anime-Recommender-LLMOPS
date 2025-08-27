from src.data_loader import AnimeDataLoader
from src.vector_store import VectorStoreBuilder
from dotenv import load_dotenv
load_dotenv()
from utils.logger import get_logger
from utils.custom_exception import CustomException

logger = get_logger(__name__)

def main():
    try:
        logger.info("Starting the build of pipeline") 
        
        data_loader  = AnimeDataLoader('data/anime_with_synopsis.csv',"data/anime_updated.csv")
        
        processed_csv = data_loader.load_and_process()
        
        vector_builder = VectorStoreBuilder("data/anime_updated.csv")
        vector_builder.build_and_save_vectorstore()
        
        logger.info("Vector store built successfully...")
        
        logger.info("Pipeline build completed")
    except Exception as e:
            raise CustomException("failed to execute pipeline",e)

if __name__ == "__main__":
	main()