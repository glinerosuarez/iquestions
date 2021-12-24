"""
The following dataset has information on red wine characteristics (acidity, pH, etc) as well as a quality rating. More
information about the schema can be found here. Can you create a Random Forest model to predict wine quality? Using a
tool or method of your choice, can you optimize the parameters of the model?
"""
import pandas as pd
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.model_selection import cross_val_score, train_test_split

if __name__ == '__main__':
    # Read dataset
    df = pd.read_csv(
        "https://raw.githubusercontent.com/erood/interviewqs.com_code_snippets/master/Datasets/winequality-red.csv",
        sep=";"
    )

    model = RandomForestClassifier(n_jobs=-1)

    X_train, X_test, y_train, y_test = train_test_split(df[df.columns[:-1]], df.quality, test_size=0.2)

    scores = cross_val_score(model, X_train, y_train, cv=5, n_jobs=-1)

    print(scores)