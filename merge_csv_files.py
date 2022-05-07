import os
import pandas as pd
from tqdm import tqdm


input_path = "./example"
csv_files = [i for i in os.listdir(input_path) if i.endswith(".csv")]
print(f"Found {len(csv_files)} files.")


df = pd.DataFrame()


for file in tqdm(csv_files):
    data = pd.read_csv(os.path.join(input_path, file), header=None)
    df = pd.concat([df, data], ignore_index=True)


print("Done!", df.shape)
df.to_csv("merged_csv_files.csv", index=False, header=None)

