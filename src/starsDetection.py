from postgres_config import user, password, host, port
from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
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


table_name = 'stars3'

def main():
    print('Connecting to database...')
    con = psycopg2.connect(user=user, password=password, host=host, port=port)
    cur = con.cursor()
    print('Done!')

    sql = f'SELECT "FUVmag", "e_FUVmag", "NUVmag", "e_NUVmag", "Vmag", "e_Vmag", "Bmag", "e_Bmag", "otype" FROM {table_name}'

    df = pd.read_sql_query(sql, con)
    print('Table:\n', df)

    df['isStar'] = np.where((df['otype'] == 'Star') | (df['otype'].str.contains('\*') == True), 1, 0)

    notStarsCount = len(df['isStar'].loc[df['isStar'] == 0].index)
    starsCount = len(df['isStar'].loc[df['isStar'] == 1].index)

    # df = df.sort_values('isStar')

    print('notStarsCount:', notStarsCount)
    print('starsCount:', starsCount)

    # print('Shape before preprocessing:', df.shape)
    # df = df.drop(df.index[notStarsCount * 2:])
    # print('Shape after preprocessing:', df.shape)
    
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

    X_train, X_test, y_train, y_test = train_test_split(df_features, df_labels, test_size=0.1, random_state=0)

    print('Train dataset: ', X_train.shape, y_train.shape)
    print('Test dataset: ', X_test.shape, y_test.shape)

    svc = svm.SVC()
    svc.fit(X_train, y_train)

    svc_pred = svc.predict(X_test)

    print('SVC:', accuracy_score(svc_pred, y_test))
    print(classification_report(svc_pred, y_test))



    log = LogisticRegression(max_iter=np.ceil(10**6 / y_train.shape[0]))
    log.fit(X_train, y_train)

    log_pred = log.predict(X_test)

    print('LogisticRegression:', accuracy_score(log_pred, y_test))
    print(classification_report(log_pred, y_test))




    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train, y_train)

    knn_pred = knn.predict(X_test)

    print('KNeighborsClassifier:', accuracy_score(knn_pred, y_test))
    print(classification_report(knn_pred, y_test))



    sgd = SGDClassifier(max_iter=np.ceil(10**6 / y_train.shape[0]))
    sgd.fit(X_train, y_train)

    sgd_pred = sgd.predict(X_test)

    print('SGDClassifier:', accuracy_score(sgd_pred, y_test))
    print(classification_report(sgd_pred, y_test))


if __name__ == "__main__":
    main()