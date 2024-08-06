from src.components.model_evaluation import Evaluation
from src.config.configuration import ConfigurationManager
from src import logger

STAGE_NAME = "Evaluation stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config) 
        evaluation.evaluation()
        evaluation.save_score()

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
        