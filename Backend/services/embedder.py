import tensorflow as tf
import tensorflow_hub as hub
from config import USE_PATH

class EmbedderService:
    def __init__(self):
        self.model = hub.load(USE_PATH)

    def get_vector(self, text):
        """Convert text into a vector representation"""
        return tf.make_ndarray(tf.make_tensor_proto(self.model([text]))).tolist()[0]
