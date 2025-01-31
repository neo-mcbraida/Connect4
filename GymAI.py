import os

import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from keras import losses 
from keras import optimizers 

class AIOp:
    def __init__(self):
        self.SinceUpdate = 0
        self.model = tf.keras.models.load_model("Model.h5")

    def GetColumn(self, state):
        
        action = self.GetAction(state)

        self.SinceUpdate += 1

        if self.SinceUpdate == 2_000:
            self.UpdateModel()
            self.SinceUpdate = 0

        return action

    def GetAction(self, state):
        state_tensor = tf.convert_to_tensor(state)
        state_tensor = tf.expand_dims(state_tensor, 0)
        action_probs = self.model(state_tensor, training=False)
        #print("predicted!")
        # Take best action
        action = tf.argmax(action_probs[0]).numpy()
        action = np.argmax(action)
        return action
         
    def UpdateModel(self):
        self.model = tf.keras.models.load_model("Model.h5")
        print("updated Opponent")

AI = AIOp()