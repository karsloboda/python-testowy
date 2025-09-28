import pandas as pd
import os

def read(path):
    try:
        return pd.read_excel(path)
    except:
        print("Błąd")

def create(data, path):
    df = pd.DataFrame(data, index=[0])
    try:
        if not os.path.exists(path):
           df.to_excel(path, index=False)
        else:
           current_df = read(path)
           new_df = pd.concat([current_df, df])
           new_df.to_excel(path, index=False)
    except Exception as e:
        print(e)