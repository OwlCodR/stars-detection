# Copyright (c) 2022 OwlCodR (Max)
# https://github.com/OwlCodR

from postgres_config import user, password, host, port

from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis

import psycopg2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def classify(classifiers, names, X_train, X_test, y_train, y_test):
    best_accuracy = 0
    best_classifier_name = ''

    for classifier, name in zip(classifiers, names):
        classifier.fit(X_train, y_train)

        prediction = classifier.predict(X_test)
        accuracy = accuracy_score(prediction, y_test)

        print(name)
        print(classification_report(prediction, y_test))

        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_classifier_name = name
        
    print('Best accuracy:', best_classifier_name, best_accuracy)


# Use it to balance stars count
def setRatio(df, column, ratio, isAscending = True):
    """
    Returns dataframe with stars ratio 
    that says how many times the number of 
    stars will exceed the number of other objects
    """

    notStarsCount = len(df[column].loc[df[column] == 0].index)
    starsCount = len(df[column].loc[df[column] == 1].index)

    minimum = min(notStarsCount, starsCount)

    print('notStarsCount:', notStarsCount)
    print('starsCount:', starsCount)

    df = df.sort_values(column, ascending=isAscending)

    print('Shape before setting ratio:', df.shape)
    df = df.drop(df.index[minimum + minimum * ratio:])
    print('Shape after setting ratio:', df.shape)

    return df

def main():
    table_name = 'stars3'

    print('Connecting to database...')
    con = psycopg2.connect(user=user, password=password, host=host, port=port)
    print('Done!')

    # sql = f'''SELECT "FUVmag", "e_FUVmag", "NUVmag", "e_NUVmag", "Vmag", "e_Vmag", "Bmag", "e_Bmag", "otype" FROM {table_name}'''

    sql = f'''SELECT "FUVmag", "e_FUVmag", "NUVmag", "e_NUVmag", "Vmag", "e_Vmag", "Bmag", "e_Bmag", "otype" FROM {table_name}'''

    df = pd.read_sql_query(sql, con)
    print('Table:\n', df)

    df['isStar'] = np.where(
        (df['otype'] == 'Star') | (df['otype'].str.contains('\*') == True), 1, 0)
    
    df = setRatio(df, 'isStar', 1)

    df_features = df[df.columns[:-2]]
    print('Features:\n', df_features)

    df_labels = df['isStar']
    print('Labels:\n', df_labels)

    plt.title("Stars")
    df_labels.hist()
    plt.show()

    X_train, X_test, y_train, y_test = train_test_split(df_features, df_labels, test_size=0.2)

    print('Train dataset: ', X_train.shape, y_train.shape)
    print('Test dataset: ', X_test.shape, y_test.shape)
    
    names = [
        "Nearest Neighbors",
        "Linear SVM",
        "RBF SVM",
        # "Gaussian Process",
        "Decision Tree",
        "Random Forest",
        "Neural Net",
        "AdaBoost",
        "Naive Bayes",
        "QDA",
    ]

    classifiers = [
        KNeighborsClassifier(3),
        SVC(kernel="linear", C=0.025),
        SVC(gamma=2, C=1),
        # GaussianProcessClassifier(),
        DecisionTreeClassifier(max_depth=5),
        RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1),
        MLPClassifier(alpha=1, max_iter=1000),
        AdaBoostClassifier(),
        GaussianNB(),
        QuadraticDiscriminantAnalysis(),
    ]

    classify(classifiers, names, X_train, X_test, y_train, y_test)

if __name__ == "__main__":
    main()