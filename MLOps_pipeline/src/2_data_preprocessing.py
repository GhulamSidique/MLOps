# import libraries
import nltk, os, logging, string, sys
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pandas as pd
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords

# to set an absolute parth for loading the logger and params functions from extra 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from extra.logger_func import create_logger
from extra.params_func import load_params

logger = create_logger("2_data_preprocessing")

nltk.download("punkt")
nltk.download("stopwords")

# function to remove less important columns
def remove_cols(dset)->pd.DataFrame:
    try:
        df = pd.read_csv(dset)
        df.drop(columns= ['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis = 0, inplace=True)
        logger.debug("Removed columns from dataset %s", df)

        # rename the columns
        df.rename(columns={"v1":"target", "v2":"value"}, inplace=True)
        df.to_csv("D:\\complete ML\\MLOps\\Lectures\\MLOps\\MLOps_pipeline\\data\\dataset.csv", index = False)
        logger.debug("Rename the columns %s", df)
    except FileNotFoundError:
        logger.error("File not found %s", df)
        raise
    except Exception as e:
        logger.error("Exceptional error %s", e)
        raise
# ==============================================================================================================

# function to label the value column
def label_dset(dset)-> pd.DataFrame:
    try:
        le = LabelEncoder()
        logger.debug("Loaded label encoder %s", le)

        df = pd.read_csv(dset)
        df = le.fit_transform(df['target'])
        logger.debug("encode the target column, %s", df)
        return df
    except FileNotFoundError:
        logger.error("file not found %s", dset)
        raise
    except Exception as e:
        logger.error("Exceptional error %s", e)
        raise



def main():
    try:
        params  = load_params()
        logger.debug("Loaded the parameters %s", params)

        # file path
        dset = params['2_data_preprocessing']['dset_path']
        df = remove_cols(dset)
        logger.debug("Df created %s", df)

        dset2 = params['2_data_preprocessing']['dset_path2']
        df = label_dset(dset2)
        logger.debug("encoded dset %s", df)

    except FileNotFoundError:
        logger.error("File not found %s", dset)
        raise
    except Exception as e:
        logger.error("Exceptional error %s", e)
        raise
if __name__=="__main__":
    main()
