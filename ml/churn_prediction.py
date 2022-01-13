"""
Given the following
[dataset](https://raw.githubusercontent.com/erood/interviewqs.com_code_snippets/master/Datasets/teleco_user_data.csv),
can you create a decision tree to predict customer churn? For simplicity, you can set the maximum depth of the decision
tree to 4. For the purpose of this exercise, you do not need to optimize the model.
"""
import pandas as pd
from implementations import DecisionTree
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


if __name__ == '__main__':
    # Read dataset
    df = pd.read_csv(
        "https://raw.githubusercontent.com/erood/interviewqs.com_code_snippets/master/Datasets/teleco_user_data.csv"
    )
    df['Churn'] = df.Churn.apply(lambda x: 1 if x == 'Yes' else 0)  # Cast labels to int

    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(
        df.iloc[:, :-1],
        df.iloc[:, -1:],
        test_size=0.20,
        random_state=42
    )
    model = DecisionTree(criterion=DecisionTree.Criterion.ENTROPY, max_depth=3, min_node_size=0)
    model.train(pd.concat([X_train, y_train], axis=1), "Churn")

    # Compute accuracy
    y_pred = model.predict(X_test)
    print(f"Train accuracy: {accuracy_score(y_train, model.predict(X_train)):0.2%}")
    print(f"Test accuracy: {accuracy_score(y_test, y_pred):0.2%}")
