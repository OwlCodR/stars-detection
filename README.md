# :stars: Variable stars detection using ML algorithms

> This repository contains university project. The goal of this project is to create a program which helps people to automatically classificate variable stars or differ other objects to variable stars using machine learning algorithms.

## 🚀 Results
- In progress

## 📦 Experience
- Python
    - pandas
    - psycopg2 (Postgres SQL)
    - csv
    - astropy
    - astroquery
- Subject area
    - Basics of astronomy
    - Variable stars classification
    - Coordinate systems and units
    - Etc

## Info about database
> We use database which is the result of crossing [APASS DR9](https://vizier.cds.unistra.fr/viz-bin/VizieR-3?-source=II/336/apass9) and [GALEX AIS GR6+7](https://vizier.u-strasbg.fr/viz-bin/VizieR-3?-source=II/335/galex_ais) by [X-Macth](http://cdsxmatch.u-strasbg.fr/). 
### Fields that we will probably use to classificate type of variable star or object in the space.

| Field | Description | Example|
|---|---|---|
| [FUVmag](https://vizier.u-strasbg.fr/viz-bin/VizieR-3?-source=II/335/galex_ais) | [10.6/23.8] GALEX FUV calibrated magnitude in AB system | 21.8688 |
| [NUVmag](https://vizier.u-strasbg.fr/viz-bin/VizieR-3?-source=II/335/galex_ais) | [-10.5/4.4] NUV Kron-like elliptical aperture magnitude | 18.1355 |
| [nobs](https://vizier.cds.unistra.fr/viz-bin/VizieR-3?-source=II/336/apass9) | [2/387] Number of observed nights | 8 |
| [mobs](https://vizier.cds.unistra.fr/viz-bin/VizieR-3?-source=II/336/apass9) | [2/3476] Number of images for this field, usually nobs*5 | 40 |
| [Vmag](https://vizier.cds.unistra.fr/viz-bin/VizieR-3?-source=II/336/apass9) | [5.5/27.4] Johnson V-band magnitude. Optical V band between 500 and 600 nm | 13.551 |
| [e_Vmag](https://vizier.cds.unistra.fr/viz-bin/VizieR-3?-source=II/336/apass9) | [0/7] Vmag uncertainty | 0.066 |
| [Bmag](https://vizier.cds.unistra.fr/viz-bin/VizieR-3?-source=II/336/apass9) | [5.4/27.3] Johnson B-band magnitude. Optical B band between 400 and 500 nm | 14.209 |
| [e_Bmag](https://vizier.cds.unistra.fr/viz-bin/VizieR-3?-source=II/336/apass9) | [0/10] Bmag uncertainty | 0.075 |
| [gpmag](https://vizier.cds.unistra.fr/viz-bin/VizieR-3?-source=II/336/apass9) | **g'mag** [5.9/24.2] g'-band AB magnitude, Sloan filter. Optical B band between 400 and 500 nm | 13.851 |
| [rpmag](https://vizier.cds.unistra.fr/viz-bin/VizieR-3?-source=II/336/apass9) | **r'mag** [5.1/23.9] r'-band AB magnitude, Sloan filter. Optical R band between 600 and 750 nm | 13.376 |
| [ipmag](https://vizier.cds.unistra.fr/viz-bin/VizieR-3?-source=II/336/apass9) | **r'mag** [4.2/29.1] i'-band AB magnitude, Sloan filter. Optical I band between 750 and 1000 nm | 13.208 |
| [otype](https://simbad.u-strasbg.fr/simbad/sim-display?data=otypes) | Object type from Simbad | EB* |
| [starType](https://vizier.cds.unistra.fr/viz-bin/VizieR-3?-source=B/vsx/vsx) | Variability **Type**, as in GCVS catalog Variability type (see details of VSX type list) | EW |
| [min](https://vizier.cds.unistra.fr/viz-bin/VizieR-3?-source=B/vsx/vsx) | Magnitude at minimum, or amplitude | 0.10999999940395355 |
| [max](https://vizier.cds.unistra.fr/viz-bin/VizieR-3?-source=B/vsx/vsx) | Magnitude at maximum, or amplitude | 13.399999618530273 |
| [Period](https://vizier.cds.unistra.fr/viz-bin/VizieR-3?-source=B/vsx/vsx) | Period of the variable in days | 0.290016 |

## 📊 Metrics of classifiers
```
Train dataset:  (6683, 8) (6683,)
Test dataset:  (1671, 8) (1671,)
Nearest Neighbors
              precision    recall  f1-score   support

           0       0.95      0.97      0.96       818
           1       0.97      0.95      0.96       853

    accuracy                           0.96      1671
   macro avg       0.96      0.96      0.96      1671
weighted avg       0.96      0.96      0.96      1671

Linear SVM
              precision    recall  f1-score   support

           0       0.94      0.97      0.96       811
           1       0.97      0.94      0.96       860

    accuracy                           0.96      1671
   macro avg       0.96      0.96      0.96      1671
weighted avg       0.96      0.96      0.96      1671

RBF SVM
              precision    recall  f1-score   support

           0       0.95      0.97      0.96       816
           1       0.97      0.95      0.96       855

    accuracy                           0.96      1671
   macro avg       0.96      0.96      0.96      1671
weighted avg       0.96      0.96      0.96      1671

Decision Tree
              precision    recall  f1-score   support

           0       0.96      0.97      0.96       828
           1       0.97      0.96      0.96       843

    accuracy                           0.96      1671
   macro avg       0.96      0.96      0.96      1671
weighted avg       0.96      0.96      0.96      1671

Random Forest
              precision    recall  f1-score   support

           0       0.95      0.97      0.96       817
           1       0.97      0.95      0.96       854

    accuracy                           0.96      1671
   macro avg       0.96      0.96      0.96      1671
weighted avg       0.96      0.96      0.96      1671

Neural Net
              precision    recall  f1-score   support

           0       0.94      0.98      0.96       801
           1       0.98      0.94      0.96       870

    accuracy                           0.96      1671
   macro avg       0.96      0.96      0.96      1671
weighted avg       0.96      0.96      0.96      1671

AdaBoost
              precision    recall  f1-score   support

           0       0.95      0.97      0.96       821
           1       0.97      0.95      0.96       850

    accuracy                           0.96      1671
   macro avg       0.96      0.96      0.96      1671
weighted avg       0.96      0.96      0.96      1671

Naive Bayes
              precision    recall  f1-score   support

           0       0.94      0.97      0.95       811
           1       0.97      0.94      0.95       860

    accuracy                           0.95      1671
   macro avg       0.95      0.95      0.95      1671
weighted avg       0.95      0.95      0.95      1671

QDA
              precision    recall  f1-score   support

           0       0.94      0.97      0.95       806
           1       0.97      0.94      0.96       865

    accuracy                           0.96      1671
   macro avg       0.96      0.96      0.96      1671
weighted avg       0.96      0.96      0.96      1671

Best accuracy: Decision Tree 0.9622980251346499
```
