import pandas as pd
import numpy as np

### THIS WAS USED IN EXPERIMENTAL, NOT THE FINAL SYNTHESIS

df_train = pd.read_json("../data/transfermarkt_real/real_data_train.json")
df_test = pd.read_json("../data/transfermarkt_real/real_data_test.json")


df_train.drop('target', axis=1, inplace=True)
df_test.drop('target', axis=1, inplace=True)

date_cols = ['validity_start', 'validity_end', 'date_of_birth']
for col in date_cols:
        df_train[col] = pd.to_datetime(np.floor(df_train[col]), unit='D', origin='1970-01-01').dt.strftime('%Y-%m-%d')
        df_test[col] = pd.to_datetime(np.floor(df_test[col]), unit='D', origin='1970-01-01').dt.strftime('%Y-%m-%d')

float_to_int_cols = ["age", "season_id", "league_played_matches", "league_minutes_played", "league_goals", "international_played_matches", "international_minutes_played", "international_goals", "missed_matches"]

df_train[float_to_int_cols] = df_train[float_to_int_cols].apply(np.floor).astype('Int64')
df_test[float_to_int_cols] = df_test[float_to_int_cols].apply(np.floor).astype('Int64')

df_train.to_json("../real_data_train_processed.json", orient="records")
df_test.to_json("../real_data_test_processed.json", orient="records")