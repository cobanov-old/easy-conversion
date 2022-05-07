import numpy as np
import os

files = [i for i in os.listdir(".") if i.endswith(".npz")]

dimension = np.load(files[0])["embeddings"].shape[1]

data = np.zeros((1, dimension))

for file in files:
    temp = np.load(file)["embeddings"]
    data = np.concatenate((data, temp), axis=0)
    print("Done", file, data.shape[0])

np.savez('merged_embeddings.npz', data)
