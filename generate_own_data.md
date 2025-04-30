# How to generate own data
- Create directory in data `DATASET_NAME` and upload training data in json format as `train_raw.json`
- and DATASET_NAME.json in /data/Info
- Categorical preprocess data: `python3 preprocess_cateogrical -d=DATASET_NAME`
- TabSyn Preprocess data: `python3 process_dataset.py --dataname DATASET_NAME`
- Train VAE `python3 main.py --dataname DATASET_NAME --method vae --mode train`
- Train TabSyn `python3 main.py --dataname DATASET_NAME --method tabsyn --mode train`
- Synthesize new samples: `python3 main.py --dataname DATASET_NAME --method tabsyn --mode sample --save_path=tm_samples.json`

# Above also working with `tm_full` as example for the real data set with converted categorical values (USE ABOVE METHOD INSTEAD; DEPRECATED)
- For this the test data set had to be converted in parts
  - splitting the dataset in `debug/build_minimal_df.ipynb`
  - Converting the categoricla values afterwards in `pre_post_processing_custom/preprocess_categorical_cols.ipynb`
  - Then run the things from how to generate data and it should be fine to import in


