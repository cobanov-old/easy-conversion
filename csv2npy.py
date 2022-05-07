import numpy as np
import pandas as pd
import sys
import os

file_path = sys.argv[1]
file_name, ext = os.path.splitext(file_path)

if ext == ".csv":
    data = pd.read_csv(file_path).values
    np.save(file_name + ".csv", data)

    print(data.shape)

else:
    print("Please provide a csv file")
    sys.exit(1)
