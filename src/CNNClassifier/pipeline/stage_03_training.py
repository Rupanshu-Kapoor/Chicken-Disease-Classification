from CNNClassifier.config.configuration import ConfigurationManager
from CNNClassifier.components.training import Training
from CNNClassifier.components.prepare_callback import PrepareCallBacks
from CNNClassifier import logger


STAGE_NAME = "Training stage"


class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_callbacks_config = config.get_prepare_callbacks_config()
        prepare_callbacks = PrepareCallBacks(config=prepare_callbacks_config)
        callback_list = prepare_callbacks.get_tb_ckpt_callbacks()
        
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train(
            callback_list=callback_list
        )



if __name__ == '__main__':
    try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completeed <<<<<<<\n\nx==========x")
    
    except Exception as e:
        logger.exception(e)
        raise e