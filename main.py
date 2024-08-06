from src import logger

from src.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from src.pipeline.stage_03_training import ModelTrainingPipeline
from src.pipeline.stage_04_evaluation import ModelEvaluationPipeline


STAGE_NAME = "Data Ingestion stage"
if __name__ == '__main__':
    try:
        logger.info(f" Stage {STAGE_NAME} started ≤≤≤≤≤≤≤≤≤≤≤")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> Stage {STAGE_NAME} completed >>>>>>>>>>>>>>>")
    except Exception as e:
        logger.exception(f" Stage {STAGE_NAME} failed >>>>>>>>>>>")
        raise e
    

STAGE_NAME = "Prepare base model"
if __name__ == '__main__':
    try:
        logger.info(f" Stage {STAGE_NAME} started")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f" Stage {STAGE_NAME} completed")
    except Exception as e:
        logger.exception(f" Stage {STAGE_NAME} failed as {e}")
        raise e
    
    
STAGE_NAME = "Training stage"
if __name__ == '__main__':
    try:
        logger.info(f" ••••••••••••••••••••••• ")
        logger.info(f">>>>>> stage {STAGE_NAME} started >>>>>>>>>>>>>>>")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed >>>>>>>>>>>>>>>")
    except Exception as e:
        logger.exception(f" stage {STAGE_NAME} failed and Error {e}>>>>>>>>>>>")
        raise e
    
STAGE_NAME = "Evaluation stage"
if __name__ == '__main__':
    try:
        logger.info(f" ••••••••••••••••••••••• ")
        logger.info(f">>>>>> stage {STAGE_NAME} started >>>>>>>>>>>>>>>")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed >>>>>>>>>>>>>>>")
    except Exception as e:
        logger.exception(f" stage {STAGE_NAME} failed and Error {e}>>>>>>>>>>>")
        raise e