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
- check if test data is used somewhere
- train with real train data and create as many samples as are in there