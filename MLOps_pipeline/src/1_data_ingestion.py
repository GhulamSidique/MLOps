# import libraries
import pandas as pd 
import os, sys
# to set an absolute parth for loading the logger and params functions from extra 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from extra.logger_func import create_logger
from extra.params_func import load_params

# logger object
logger = create_logger("1_data_ingestion") # name according to the file 

# load the dataset
def load_dataset(d_set_path:str)->pd.DataFrame:
    try:
        df = pd.read_csv(d_set_path, encoding='ISO-8859-1')
        logger.debug("Loaded dataset from %s", d_set_path)
        return df
    except pd.errors.ParserError as e:
        logger.error("Error loading dataset %s", e)
        raise
    except Exception as e:
        logger.error("Exception error %s", e)
        raise
# ===============================================================================================================

# save the dataset in data folder
def save_dset(dset_dir, df:pd.DataFrame):
    try:
        # dset_dir = "E:\complete ML\MLOps\MLOps\MLOps_pipeline\data"
        os.makedirs(dset_dir, exist_ok=True)
        path= os.path.join(dset_dir, "raw_dataset.csv")
        df.to_csv(path, index=False)
        logger.debug("Dataset save successfully %s", path)
    except FileNotFoundError:
        logger.error("File not found %s", path)
        raise
    except Exception as e:
        logger.error("Exception errpr %s", e)
        raise
# ===============================================================================================================

def main():
    try:
        logger.debug("Starting main ingestion function.")
        params = load_params()
        logger.debug("loaded parameters %s", params)

        # for load_dataset
        d_set_path = params['1_data_ingestion']['dset_path']
        df = load_dataset(d_set_path)
        logger.debug("loaded dset %s", df)

        # for save_dset
        dset_save_dir = params['1_data_ingestion']['dset_save_dir']
        save_dset(dset_save_dir, df = df)
        logger.debug("save dataset %s", df)

    except FileNotFoundError:
        logger.error("File not found %s", df)
        raise
# ===============================================================================================================

if __name__=="__main__":
    main()