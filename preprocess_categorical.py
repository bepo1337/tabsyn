import pandas as pd
import argparse
from sklearn.model_selection import train_test_split
import random


parser = argparse.ArgumentParser(description="Process missing cateogrical values from test set",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-d", "--dataname", required=True, type=str, help="Input file (train)")
args = parser.parse_args()

dataname = args.dataname

df = pd.read_json(f"data/{dataname}/train_raw.json")
df["target"] = "0"

unique_ids = df["player_id"].unique()
train_ids, test_ids = train_test_split(unique_ids, test_size=0.15, random_state=1)
train_df = df[df["player_id"].isin(train_ids)].copy()
test_df = df[df["player_id"].isin(test_ids)].copy()


player_ids = train_df.player_id.tolist()
first_names = train_df.first_name.tolist()
last_names = train_df.last_name.tolist()
pseudonyms = train_df.pseudonym.tolist()
citzenships = train_df.citizenship.tolist()
# go thru real and full player_id_to_names, also pseudonym

injury_mapping = train_df.groupby('injury_category')['injury'].apply(lambda x: list(set(x))).to_dict()

random.seed(42)

# Create sets for fast lookup
train_static_values = {
    "first_name": set(first_names),
    "last_name": set(last_names),
    "player_id": set(player_ids),
    "pseudonym": set(pseudonyms),
    "citizenship": set(citzenships),
    "injury": set(train_df.injury.tolist()),
}

# Value pools for replacements
replacement_pool = {
    "first_name": first_names,
    "last_name": last_names,
    "player_id": player_ids,
    "pseudonym": pseudonyms,
    "citizenship": citzenships,
}

# Cache to store replacements per test player
player_static_replacements = {}

# iterate over test playerrs
for pid in test_df.player_id.unique():
    player_rows = test_df[test_df.player_id == pid]
    sample_row = player_rows.iloc[0]
    replacement = {}

    # check for each value if it is in the training set
    for field in ["player_id", "first_name", "last_name", "pseudonym", "citizenship"]:
        val = sample_row[field]
        if val not in train_static_values[field]:
            replacement[field] = random.choice(replacement_pool[field])
        else: # is in the trainnig set: can keep old value
            replacement[field] = val

    player_static_replacements[pid] = replacement


# change values in test set with possibly replaced field values
def apply_replacements(row):
    repl = player_static_replacements[row.player_id]
    for field in ["player_id", "first_name", "last_name", "pseudonym", "citizenship"]:
        row[field] = repl[field]
    return row

test_df = test_df.apply(apply_replacements, axis=1)



def replace_injury(row):
    if row["injury"] not in train_static_values["injury"]:
        options = injury_mapping.get(row["injury_category"], [])
        if options:
            return random.choice(options)
    return row["injury"]

test_df["injury"] = test_df.apply(replace_injury, axis=1)

train_df.to_json(f"data/{dataname}/train.json", orient="records")
test_df.to_json(f"data/{dataname}/test.json", orient="records")