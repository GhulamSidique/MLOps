import yaml
from extra.logger_func import create_logger

# logger = create_logger()

def load_params():
        # read the parameters
        try:
            with open("E:\complete ML\MLOps\MLOps\MLOps\MLOps_pipeline\params.yaml", "r") as file:
                params = yaml.safe_load(file)
            # logger.debug("Loaded the parameters safely %s",params)
            return params
        except FileNotFoundError:
            # logger.error("parameters file not found %s", params)
            raise
        except Exception as e:
            # logger.error("Exception error %s", e)
            raise
