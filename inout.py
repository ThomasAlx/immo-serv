import numpy as np
import os

class InOut:

    def __init__(self):
        pass

    @staticmethod
    def save_data(folder, data, name):
        np.save(os.path.join(folder, name), data, allow_pickle=True)

    @staticmethod
    def load_data(folder, name):
        return np.load(os.path.join(folder, name), allow_pickle=True)



