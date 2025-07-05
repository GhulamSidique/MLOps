# import libraries
import pandas as pd 
import logging, os, yaml

# ===============================================================================================================
class data_ingestion:
    def __init__(self):
        self.logger = None
    # ===============================================================================================================

    # function to create a logger
    def create_logger(self):
        # create logging information both file and console handler
        # create the main folder logs
        logs_dir= r"E:\complete ML\MLOps\MLOps\MLOps_pipeline\logs" # we can change it any time when needed
        os.makedirs(logs_dir, exist_ok=True)

        # create the file and console handler
        # create a logger object
        self.logger = logging.getLogger("1_data_ingestion")
        self.logger.setLevel("DEBUG")

        # create a console
        console = logging.StreamHandler()
        console.setLevel("DEBUG")

        # create a file handler and save information in it
        file_name= "1_data_ingestion.log"
        log_file_path = os.path.join(logs_dir, file_name)
        file_handler = logging.FileHandler(log_file_path)
        file_handler.setLevel("DEBUG")

        # create the formater to display the informtaion on the terminal and save it in the logs folder
        console_formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        console.setFormatter(console_formater)
        file_handler.setFormatter(console_formater)

        # add the logging information to both file and the console
        self.logger.addHandler(console)
        self.logger.addHandler(file_handler)
    # ===============================================================================================================

    # function to create a load the params used for this code file 
    def load_params(self, params_path: str):
        # read the parameters
        try:
            with open(params_path, "r") as file:
                params = yaml.safe_load(file)
            self.logger.debug("Loaded the parameters safely %s", params_path)
            return params
        except FileNotFoundError:
            self.logger.error("parameters file not found %s", params_path)
            raise
        except Exception as e:
            self.logger.error("Exception error %s", e)
            raise


    # load the dataset
    def load_dataset(self, d_set_path:str)->pd.DataFrame:
        try:
            df = pd.read_csv(d_set_path, encoding='ISO-8859-1')
            self.logger.debug("Loaded dataset from %s", d_set_path)
            return df
        except pd.errors.ParserError as e:
            self.logger.error("Error loading dataset %s", e)
            raise
        except Exception as e:
            self.logger.error("Exception error %s", e)
            raise
    # ===============================================================================================================

    # save the dataset in data folder
    def save_dset(self, dset_dir, df:pd.DataFrame):
        try:
            # dset_dir = "E:\complete ML\MLOps\MLOps\MLOps_pipeline\data"
            os.makedirs(dset_dir, exist_ok=True)
            path= os.path.join(dset_dir, "raw_dataset.csv")
            df.to_csv(path, index=False)
            self.logger.debug("Dataset save successfully %s", path)
        except FileNotFoundError:
            self.logger.error("File not found %s", path)
            raise
        except Exception as e:
            self.logger.error("Exception errpr %s", e)
            raise
    # ===============================================================================================================

    def main(self):
        # Setup temporary logger in case params.yaml is broken
        # self.create_logger("logs", "temp.log")
        try:
            # data_path = "E:\complete ML\MLOps\MLOps\MLOps_pipeline\spam.csv"
            # load the parameter
            load_create_logger=self.create_logger()
            self.logger.debug("loaded create_logger %s", load_create_logger)


            params = self.load_params("E:\complete ML\MLOps\MLOps\MLOps_pipeline\params.yaml")
            self.logger.debug("loaded parameters %s", params)

            # for create_logger
            # logs_dir, file_name = params['1_data_ingetsion']['logs_dir'], params['1_data_ingetsion']['file_name']
            # self.create_logger(logs_dir, file_name)
            # self.logger.debug("created dset %s", file_name)

            # for load_dataset
            d_set_path = params['1_data_ingestion']['dset_path']
            df = self.load_dataset(d_set_path)
            self.logger.debug("loaded dset %s", df)

            # for save_dset
            dset_save_dir = params['1_data_ingestion']['dset_save_dir']
            self.save_dset(dset_save_dir, df = df)
            self.logger.debug("save dataset %s", df)
        except FileNotFoundError:
            self.logger.error("File not found %s", df)
            raise
# ===============================================================================================================

if __name__=="__main__":
    ingestion = data_ingestion()
    ingestion.main()
