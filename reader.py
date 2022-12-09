import numpy as np
import os

class Reader:

    def __init__(self):
        pass

    @staticmethod
    def save_data(folder, data):
        np.save(os.path.join(folder, "immo-cleaned-data.npy"), data, allow_pickle=True)

    @staticmethod
    def load_data(folder):
        return np.load(os.path.join(folder, "immo-cleaned-data.npy"), allow_pickle=True)



