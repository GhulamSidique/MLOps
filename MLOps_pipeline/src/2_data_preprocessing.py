# import libraries
import nltk, os, string, sys
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
        df.to_csv("E:\complete ML\MLOps\MLOps\MLOps\MLOps_pipeline\data\dataset.csv", index = False)
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
        df['target'] = df['target'].astype(str).str.strip()
        df['target'] = le.fit_transform(df['target'])
        df.to_csv(dset, index=False)
        logger.debug("encode the target column, %s", df)
        return df
    except FileNotFoundError:
        logger.error("file not found %s", dset)
        raise
    except Exception as e:
        logger.error("Exceptional error %s", e)
        raise
# ==============================================================================================================

# function to tokenize the value column
def preprocess_text(text):
    try:

        # lower the characters
        text = text.lower()

        # tokenize the text
        text = nltk.word_tokenize(text)

        # remove non_alphanumeric charaters
        text = [word for word in text if word.isalnum()]

        # remove stopwords
        text = [word for word in text if word not in stopwords.words("english") and word not in string.punctuation]

        # apply porter stemmer
        ps = PorterStemmer()
        text = [ps.stem(word) for word in text]

        # join the tokens back into a single string
        return " ".join(text)
    except Exception as e:
        logger.error("Exceptional error %s", e)
def tokenize_text(dset):
    try:
        df = pd.read_csv(dset)
        df['value'] = df['value'].astype(str).apply([preprocess_text])

        df.to_csv(dset, index=False)
        logger.debug("preprocessed the value column completely")
        return df

    except FileNotFoundError:
        logger.error("File not found %s", dset)
        raise
    except Exception as e:
        logger.error("Execption error %s", e)
        raise
# ==============================================================================================================

def remove_nans(dset: str)-> pd.DataFrame:
    try:
        df = pd.read_csv(dset)
        df.dropna(inplace=True)
        df.to_csv(dset, index=False)
        logger.debug("Removed nan values")
        return df
    except FileNotFoundError:
        logger.error("File not found %s", dset)
        raise
    except Exception as e:
        logger.error("Execption error %s", e)
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
    
        dset3 = params['2_data_preprocessing']['dset_path2']
        df = tokenize_text(dset3)
        logger.debug("encoded dset %s", df)

        dset4 = params['2_data_preprocessing']['dset_path2']
        df = remove_nans(dset4)
        logger.debug("encoded dset %s", df)


    except FileNotFoundError:
        logger.error("File not found %s", dset)
        raise
    except Exception as e:
        logger.error("Exceptional error %s", e)
        raise
if __name__=="__main__":
    main()
