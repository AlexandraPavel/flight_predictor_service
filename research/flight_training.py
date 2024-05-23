import json # will be needed for saving preprocessing details
import numpy as np # for data manipulation
import pandas as pd # for data manipulation
from sklearn.model_selection import train_test_split # will be used for data split
from sklearn.preprocessing import LabelEncoder # for preprocessing
from sklearn.ensemble import RandomForestClassifier # for training the algorithm
from sklearn.ensemble import ExtraTreesClassifier # for training the algorithm
import joblib # for saving algorithm and preprocessing objects

file_list = [
    'flights_02_12_2023.csv',
    # 'flights_03_12_2023.csv',
    # 'flights_04_12_2023.csv',
    # 'flights_05_12_2023.csv',
    # 'flights_06_12_2023.csv',
    # 'flights_07_12_2023.csv',
    # 'flights_08_12_2023.csv',
    # 'flights_09_12_2023.csv',
    # 'flights_10_12_2023.csv',
    # 'flights_11_12_2023.csv',
    # 'flights_12_12_2023.csv',
]

# load dataset
data_frames = pd.DataFrame()

# Read each CSV file and append its DataFrame to the list
for file in file_list:
    file_path = 'https://raw.githubusercontent.com/AlexandraPavel/PriceFlightEstimator/master/'+file
    df = pd.read_csv(file_path, skipinitialspace=True)
    data_frames = data_frames.append(df)

X = data_frames.iloc[:, 1:]
X = X.iloc[:, :-1]
y = data_frames['price']
print('Number of entries:', len(X))
print(X.head())

undefined_cells = X.isnull().sum()
print(undefined_cells)

# data split train / test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state=1234)

# fill missing values
train_mode = dict(X_train.mode().iloc[0])
X_train = X_train.fillna(train_mode)
print(train_mode)

# convert categoricals
encoders = {}
for column in [
    'date_of_enquiry',
    'departure',
    'destination',
    'flight_date',
    'flight_time',
    'arrival_time',
    'airline',
    'layovers',
    'flight_duration',
]:
    categorical_convert = LabelEncoder()
    X_train[column] = categorical_convert.fit_transform(X_train[column])
    encoders[column] = categorical_convert

# train the Random Forest algorithm
rf = RandomForestClassifier(n_estimators = 100)
rf = rf.fit(X_train, y_train)

# train the Extra Trees algorithm
et = ExtraTreesClassifier(n_estimators = 100)
et = et.fit(X_train, y_train)


# save preprocessing objects and RF algorithm
joblib.dump(train_mode, "./train_mode.joblib", compress=True)
joblib.dump(encoders, "./encoders.joblib", compress=True)
joblib.dump(rf, "./random_forest.joblib", compress=True)
joblib.dump(et, "./extra_trees.joblib", compress=True)