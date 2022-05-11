# Copyright (c) 2022 OwlCodR (Max)
# https://github.com/OwlCodR

from postgres_config import user, password, host, port
from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn import svm
from sklearn.linear_model import SGDClassifier

import psycopg2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def classify(classifiers, X_train, X_test, y_train, y_test):
    best_accuracy = 0

    for classifier in classifiers:
        classifier.fit(X_train, y_train)

        prediction = classifier.predict(X_test)
        
        accuracy = accuracy_score(prediction, y_test)

        print(accuracy)
        print(classification_report(prediction, y_test))

        if accuracy > best_accuracy:
            best_accuracy = accuracy
        
    print('Best accuracy: ', best_accuracy)


def setStarsRatio(df, ratio):
    """
    Returns dataframe with stars ratio 
    that says how many times the number of 
    stars will exceed the number of other objects
    """

    notStarsCount = len(df['isStar'].loc[df['isStar'] == 0].index)
    starsCount = len(df['isStar'].loc[df['isStar'] == 1].index)

    print('notStarsCount:', notStarsCount)
    print('starsCount:', starsCount)

    df = df.sort_values('isStar')

    print('Shape before setting ratio:', df.shape)
    df = df.drop(df.index[notStarsCount * ratio:])
    print('Shape after setting ratio:', df.shape)

def main():
    table_name = 'stars3'

    print('Connecting to database...')
    con = psycopg2.connect(user=user, password=password, host=host, port=port)
    cur = con.cursor()
    print('Done!')

    sql = f'''SELECT "FUVmag", "e_FUVmag", "NUVmag", "e_NUVmag", "Vmag", "e_Vmag", "Bmag", "e_Bmag", "otype" FROM {table_name}'''

    df = pd.read_sql_query(sql, con)
    print('Table:\n', df)

    df['isStar'] = np.where(
        (df['otype'] == 'Star') | (df['otype'].str.contains('\*') == True), 1, 0)
    
    # df = setStarsRatio(df, 1)

    df_features = df[df.columns[:-2]]
    print('Features:\n', df_features)

    df_labels = df['isStar']
    print('Labels:\n', df_labels)

    plt.title("Stars")
    df_labels.hist()
    plt.show()

    # plt.title("Objects types")
    # df['otype'].hist()
    # plt.show()

    X_train, X_test, y_train, y_test = train_test_split(df_features, df_labels, test_size=0.1)

    print('Train dataset: ', X_train.shape, y_train.shape)
    print('Test dataset: ', X_test.shape, y_test.shape)

    max_iter = np.ceil(10**6 / (y_train.shape[0]))
    
    classify([
            svm.SVC(),
            GaussianNB(),
            LogisticRegression(max_iter=max_iter),
            KNeighborsClassifier(n_neighbors=5),
            SGDClassifier(max_iter=max_iter)
        ], 
        X_train, X_test, y_train, y_test
    )

if __name__ == "__main__":
    main()