import random
import pandas as pd
import json
import numpy as np
# Create new features

def create_new_features(dataframe: pd.DataFrame, features_name: str, range_of_values: (int, int), n_values: int):
    print(range_of_values[0], range_of_values[1])
    mu = (int(range_of_values[1]+1)+int(range_of_values[0]))//2
    sigma = (int(range_of_values[1]+1) - int(range_of_values[0]))//5
    print(features_name, mu,sigma)
    list_of_values = np.abs(np.random.normal(mu, sigma, n_values))#.astype(int)
    dataframe[features_name] = list_of_values
    return dataframe


if __name__ == '__main__':
    n_sample = 5000
    features_dict = json.load(open('range_of_values.json',))
    print(features_dict)
    #features = ["numero di foto di buongiorno", "numero di like per foto", "numero di commenti per foto"]
    df_boomer = pd.DataFrame()
    df_non_boomer = pd.DataFrame()
    # Dataframe boomer
    for feature in features_dict["boomer"]:
        df_boomer = create_new_features(df_boomer, feature, features_dict["boomer"][feature],n_sample)
    df_boomer["boomer"] = [1]*n_sample

    for feature in features_dict["non_boomer"]:
        df_non_boomer = create_new_features(df_non_boomer, feature, features_dict["non_boomer"][feature], n_sample)
    df_non_boomer["boomer"] = [0]*n_sample

    final_df = df_boomer.append(df_non_boomer,ignore_index=True)
    final_df.to_csv("boomer_non_boomer.csv")
    #print(df_boomer,df_non_boomer)

