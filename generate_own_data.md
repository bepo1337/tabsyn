# How to generate own data
- Create directory in data `transfermarkt` and upload training data in json format with dummy varaible at the end
- and transfermarkt.json in /data/Info with dummy variable at the end
- Preprocess data: `python3 process_dataset.py --dataname transfermarkt`
- Train VAE `python3 main.py --dataname transfermarkt --method vae --mode train`
- Train TabSyn `python3 main.py --dataname transfermarkt --method tabsyn --mode train`
- Synthesize new samples: `python3 main.py --dataname transfermarkt --method tabsyn --mode sample --save_path=tm_samples.json`


# Next steps
- Use excerpt of real data ✅
- Create small preprocess script to fit it to the tabsyn dataset ✅
  - ie create dummy variable target ✅
- adapt the info file with the numerical and categorical values ✅
- check if test data is used somewhere ✅
- is test set used as val in training?
- set if validation set exists
- train with minimal dataset that only contains few columns that everybody has: league, international competition, performance data and check if that works with the trainig
- 
- training without player id, name, last name, pseudonym to ensure that 
- maybe just train 
- add test data and add this to the path after pre processing it
- train with real train data and create as many samples as are in there


# Check if Validation set exists