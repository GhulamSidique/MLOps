# import libraries
import pandas as pd 
import numpy as np
import logging, os

# ===============================================================================================================
# create logging information both file and console handler
# create the main folder logs
logs_dir = "logs"
os.makedirs(logs_dir, exist_ok=True)

# create the file and console handler
# create a logger object
logger = logging.getLogger("1_data_ingesztion")
logger.setLevel("DEBUG")

# create a console
console = logging.StreamHandler()
console.setLevel("DEBUG")

# create a file handler and ssave information in it
log_file_path = os.path.join(logs_dir, "1_data_ingestion.log")
file_handler = logging.FileHandler(log_file_path)
file_handler.setLevel("DEBUG")

# create the formater to display the informtaion on the terminal and save it in the logs folder
console_formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
console.setFormatter(console_formater)
file_handler.setFormatter(console_formater)

# add the logging information to both file and the console
logger.addHandler(console)
logger.addHandler(file_handler)
# ===============================================================================================================

# # create a params function that will load the data ingestion paramerters to make use of them here
# def load_params(param_path:str): # will contain param_path from the params yaml file for data ingestion
#     # read the parameters from the path
#     try:
#         with open(param_path, "r") as file:
#             params = yaml.safe_load(file)
#         # set the message
#         logger.debug("Successfully loaded the parameters for %s", param_path)
#         return params
#     except FileNotFoundError:
#         logger.error("fils not found %s", param_path)
#         raise 
#     except yaml.YAMLError as e:
#         logger.error("Yaml error %s", e)
#         raise
#     except Exception as e:
#         logger.error("Exception error %s", e)
#         raise
# ===============================================================================================================

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
def save_dset(df:pd.DataFrame):
    try:
        dset_dir = "data"
        os.makedirs(dset_dir, exist_ok=True)
        dset_path = df.to_csv(os.path.join(dset_dir, "data.csv"), index=False)
        logger.debug("Dataset save successfully %s", dset_path)
    except FileNotFoundError:
        logger.error("File not found %s", dset_path)
        raise
    except Exception as e:
        logger.error("Exception errpr %s", e)
        raise

def main():
    try:
        data_path = "E:\complete ML\MLOps\MLOps\MLOps_pipeline\spam.csv"
        df = load_dataset(d_set_path = data_path)
        save_dset(df = df)
        logger.debug("save dataset %s", df)
    except FileNotFoundError:
        logger.error("File not found %s", df)
        raise

if __name__=="__main__":
    main()



        






