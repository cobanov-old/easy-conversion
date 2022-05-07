import numpy as np
import pandas as pd
import sys
import os

file_path = sys.argv[1]
file_name, ext = os.path.splitext(file_path)

if ext == ".npy":
    data = np.load(file_path)
    df = pd.DataFrame(data)
    df.to_csv(file_name + ".csv", index=None, header=None)
    print(df.shape)

else:
    print("Please provide a npy file")
    sys.exit(1)
