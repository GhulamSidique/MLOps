import logging, os

def create_logger(logger_name):
        # create logging information both file and console handler
        # create the main folder logs
        logs_dir= r"E:\complete ML\MLOps\MLOps\MLOps\MLOps_pipeline\logs" # we can change it any time when needed
        os.makedirs(logs_dir, exist_ok=True)

        # create the file and console handler
        # create a logger object
        logger = logging.getLogger(logger_name)
        logger.setLevel("DEBUG")

        # create a console
        console = logging.StreamHandler()
        console.setLevel("DEBUG")

        # create a file handler and save information in it
        file_name= logger_name + ".log"
        log_file_path = os.path.join(logs_dir, file_name)
        file_handler = logging.FileHandler(log_file_path)
        file_handler.setLevel("DEBUG")

        # create the formater to display the informtaion on the terminal and save it in the logs folder
        console_formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        console.setFormatter(console_formater)
        file_handler.setFormatter(console_formater)

        # add the logging information to both file and the console
        logger.addHandler(console)
        logger.addHandler(file_handler)

        return logger

