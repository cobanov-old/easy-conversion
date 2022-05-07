import numpy as np
import os
from tqdm import tqdm


input_path = "./example"
npy_files = [i for i in os.listdir(input_path) if i.endswith(".npy")]
print(f"Found {len(npy_files)} files.")


dimension = np.load(os.path.join(input_path, npy_files[0])).shape[1]
data = np.zeros((1, dimension))

for file in tqdm(npy_files):
    temp = np.load(os.path.join(input_path, file))
    data = np.concatenate((data, temp), axis=0)


print("Done!", data.shape)
np.save("merged_embeddings.npy", data)
