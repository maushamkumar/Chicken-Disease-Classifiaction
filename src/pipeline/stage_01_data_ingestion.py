from src import logger
from config.configuration import ConfigurationManager
from components.data_ingestion import DataIngestion

STAGE_NAME = "Data Ingestion stage"



class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
       
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
        
        
if __name__ == '__main__':
    try:
        logger.info(f" Stage {STAGE_NAME} started ≤≤≤≤≤≤≤≤≤≤≤")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> Stage {STAGE_NAME} completed >>>>>>>>>>>>>>>")
    except Exception as e:
        logger.exception(f" Stage {STAGE_NAME} failed >>>>>>>>>>>")
        raise e