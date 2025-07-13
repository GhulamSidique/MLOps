import mlflow
import matplotlib.pyplot as plt
import mlflow.sklearn
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_wine
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# set a tracking ui for mlflow
mlflow.set_tracking_uri("http://127.0.0.1:5000") # local host is 5000

# load the dataset
wine = load_wine()
# separate the x and y 
x= wine.data
y = wine.target

# split the train and test data
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=42)

max_depth = 10
n_estimators = 12

# set experiment
mlflow.set_experiment("My_exp_log")
mlflow.autolog()
# write the mlflow code 
with mlflow.start_run():
    # fit the model
    rf = RandomForestClassifier(max_depth=max_depth, n_estimators=n_estimators, random_state=42)

    # fit the data
    rf.fit(xtrain, ytrain)

    # accuracy score
    y_pred = rf.predict(xtest)
    acc = accuracy_score(ytest, y_pred)

    # log the parameters and metrix
    # mlflow.log_metric("accuracy", acc)
    # mlflow.log_param("max_depth", max_depth)
    # mlflow.log_param("n_estimators", n_estimators)

    # create the artifacts by ploting a confusion metrics
    cm = confusion_matrix(ytest, y_pred)
    plt.figure(figsize=(6,6))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=wine.target_names, yticklabels=wine.target_names)
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title("CM")
    plt.savefig("CM.png")

    #W log the artificats
    # mlflow.log_artifact("CM.png")
    mlflow.log_artifact(__file__) # must to write to read a local file

    # adding tags
    mlflow.set_tags({"Author":"Haji", "Project":"Wine Classification"})
    # mlflow.sklearn.log_model(rf, "Random Forest Classifier")
    print(acc)  