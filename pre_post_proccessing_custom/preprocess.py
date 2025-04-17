import pandas as pd
import numpy as np

df_train = pd.read_json("../data/transfermarkt_real/real_data_train.json")
df_test = pd.read_json("../data/transfermarkt_real/real_data_test.json")

df_train["target"] = "0"
df_test["target"] = "0"

###TRAIN
# make dates numerical as days since 01.0
df_train['validity_start'] = pd.to_datetime(df_train['validity_start'])
df_train['validity_end'] = pd.to_datetime(df_train['validity_end'])
df_train['date_of_birth'] = pd.to_datetime(df_train['date_of_birth'])

reference_date = pd.Timestamp('1970-01-01')

# days since ref date
df_train['validity_start'] = (df_train['validity_start'] - reference_date).dt.days
df_train['validity_end'] = (df_train['validity_end'] - reference_date).dt.days
df_train['date_of_birth'] = (df_train['date_of_birth'] - reference_date).dt.days


### TEST
# make dates numerical as days since 01.0
df_test['validity_start'] = pd.to_datetime(df_test['validity_start'])
df_test['validity_end'] = pd.to_datetime(df_test['validity_end'])
df_test['date_of_birth'] = pd.to_datetime(df_test['date_of_birth'])

reference_date = pd.Timestamp('1970-01-01')

# days since ref date
df_test['validity_start'] = (df_test['validity_start'] - reference_date).dt.days
df_test['validity_end'] = (df_test['validity_end'] - reference_date).dt.days
df_test['date_of_birth'] = (df_test['date_of_birth'] - reference_date).dt.days

desired_order = [
    "player_id", "reason", "validity_start", "validity_end", "first_name", "last_name", "pseudonym", "height",
    "date_of_birth", "age", "foot", "position", "citizenship", "injury", "injury_category", "market_value",
    "market_value_category", "last_transfer_fee", "club", "club_id", "season_id", "league", "league_id",
    "international_competition", "coach", "coach_id", "league_played_matches", "league_minutes_played",
    "league_goals", "international_played_matches", "international_minutes_played", "international_goals",
    "missed_matches", "target"
]

df_train = df_train[desired_order]
df_test = df_test[desired_order]


##

# df_train.to_json("../data/transfermarkt_real/real_data_train_processed.json", orient="records")
# df_test.to_json("../data/transfermarkt_real/real_data_test_processed.json", orient="records")

#
# df_train.drop("player_id", axis=1, inplace=True)
# df_test.drop("player_id", axis=1, inplace=True)
# df_train.fillna("default_value", inplace=True)
# df_test.fillna("default_value", inplace=True)

unique_ids = df_train["player_id"].unique()
np.random.shuffle(unique_ids)

split_idx = int(len(unique_ids) * 0.8)
train_ids = unique_ids[:split_idx]
test_ids = unique_ids[split_idx:]

df_train_80 = df_train[df_train["player_id"].isin(train_ids)]
df_test = df_train[df_train["player_id"].isin(test_ids)]
df_train_80.to_json("../data/tm_own_split/train.json", orient="records")
b

