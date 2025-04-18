# categories that are in train but not in test are fine. But vice versa is not
Affected columns are the following
- player_id
- injury
- first name
- last name
- pseudonym
- citizenship


# How to fix
Build script that does the following
- Get player_ids from real data set and make a 1:1 replacement in test dataset
  - same for first_name and last_name 
- get rows with injuries and just take a random injury from the same category



# how to argument
- injury: gsp uses injury_cateogry --> no change, only other metrics affected a bit, but its only 5 out of 300 injuries
- names: we dont track names, ids -->no change
- pseudonym: random col anyways
- citizenship: only 1 affected