from postgres_config import user, password, host, port
from starsDetection import classify
from starsDetection import setRatio

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
from sklearn import preprocessing

import psycopg2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import re

def main():
    table_name = 'stars3'

    print('Connecting to database...')
    con = psycopg2.connect(user=user, password=password, host=host, port=port)
    print('Done!')

    simbad_vstar_types = [
        'V\*', 'Irregular_V\*', 'Orion_V\*', 'Eruptive\*', 'Erupt\*RCrB', 'RCrB_Candidate', 'RotV\*', 'RotV\*alf2CVn', 'Pulsar', 'BYDra', 'RSCVn', 'PulsV\*', 'RRLyr', 'Cepheid', 'PulsV\*delSct', 'PulsV\*RVTau', 'PulsV\*WVir', 'PulsV\*bCep', 'deltaCep', 'gammaDor', 'pulsV\*SX', 'LPV\*', 'Mira', 'SN'
    ]

    # TODO: Try to add candidates too
    regExp = f"^({'|'.join(simbad_vstar_types)})$"
    print(regExp)

    vstars_pattern = re.compile(regExp)

    sql = f'''SELECT "FUVmag", "e_FUVmag", "NUVmag", "e_NUVmag", "Vmag", "e_Vmag", "Bmag", "e_Bmag", "starType", "otype" FROM {table_name}'''

    df = pd.read_sql_query(sql, con)
    print('Table:\n', df)

    df['isVariableStar'] = np.where(
        (df['starType'].isnull() == False) | (df['otype'].str.match(vstars_pattern) == True), 1, 0)

    df = setRatio(df, 'isVariableStar', 1, False)

    df_features = df[df.columns[:-3]]
    print('Features:\n', df_features)

    df_labels = df['isVariableStar']
    print('Labels:\n', df_labels)

    plt.title("Stars")
    df_labels.hist()
    plt.show()

    X_train, X_test, y_train, y_test = train_test_split(
        df_features, df_labels, test_size=0.2)

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
