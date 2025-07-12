import sys, os, pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from extra.logger_func import create_logger
from extra.params_func import load_params

logger = create_logger("3_model_building")

# function to convert the text into numerics
def model_building(dset: str, max_features: int, test_size:float, n_estimators:int, random_state: int) -> pd.DataFrame:
    try:
        df = pd.read_csv(dset)

        # separate the training and testing data 
        x = df['value'].astype(str).values
        y = df['target'].values

        xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=test_size)

        # apply the tfidf
        tfidf = TfidfVectorizer(max_features=max_features)

        xtrain_bow = tfidf.fit_transform(xtrain)
        xtest_bow = tfidf.transform(xtest)

        # build the classifier
        cls = RandomForestClassifier(n_estimators=n_estimators, random_state=random_state)

        # fit the training data
        cls.fit(xtrain_bow, ytrain)
        logger.debug("model fit with training data")
        ypred = cls.predict(xtest_bow)
        logger.info("Accuracy: %.2f%%", accuracy_score(ytest, ypred) * 100)
        logger.info("Classification Report:\n%s", classification_report(ytest, ypred))
        return cls
    except FileNotFoundError:
        logger.error("File not found %s", dset)
        raise
    except Exception as e:
        logger.error("exception error %e", e)
# ========================================================================================================   

# save model
def save_model(model, file_path:str):
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open (file_path, "w") as file:
            pickle.dump(model, file)
        logger.debug("saved model")
    except FileNotFoundError:
        logger.error("File not found %s", model)
        raise
    except Exception as e:
        logger.error("exception error %e", e)      

def main():
    try:
        params = load_params()

        dset =params['3_model_building']['dset_path']
        max_fets = params['3_model_building']['max_features']
        test_size = params['3_model_building']['test_size']
        n_estimators = params['3_model_building']['n_estimators']
        random_state = params['3_model_building']['random_state']
        model = model_building(dset,max_fets, test_size, n_estimators, random_state)
        logger.debug("applied tfidf on dataset %s", model)

        model_path = params['3_model_building']['model_path']
        save_model(model, model_path)
        logger.debug("saved model at %s", model_path)

    except Exception as e:
        logger.error("exception error %s", e) 
        raise

if __name__=="__main__":
    main()


