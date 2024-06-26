import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
import time
from CNNClassifier.entity.config_entity import PrepareCallbacksConfig


class PrepareCallBacks:
    def __init__(self, config: PrepareCallbacksConfig):
        self.config = config

    @property
    def create_tb_callback(self):
        timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")
        tb_running_log_dir = os.path.join(
            self.config.tensorboard_root_log_dir,
            f"tb_logs_at_{timestamp}"
        )
        return tf.keras.callbacks.TensorBoard(log_dir=tb_running_log_dir)
    
    @property
    def create_ckpt_callback(self):
        return tf.keras.callbacks.ModelCheckpoint(
            filepath=self.config.checkpoint_model_filepath,
            save_best_only=True
        )
    
    def get_tb_ckpt_callbacks(self):
        return [
            self.create_tb_callback,
            self.create_ckpt_callback
        ]