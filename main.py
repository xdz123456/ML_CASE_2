import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression

# Load all the data from souse file
# Get all the feature names
feature_df = pd.read_csv("features.txt", header=None)
# Get the the data of features
data_df = pd.read_csv("data.txt", header=None)
# Get all the labels
labels_df = pd.read_csv("labels.txt", header=None)


# Mapping with index of the data set
feature = np.array(feature_df)[0]
data_df.columns = feature
# Add the labels on the whole data
labels = np.array(labels_df)
data_df["labels"] = labels


# The data set already finished the data normalization
# One Hot for thr data
# data = OneHotEncoder().fit_transform(data_df)

# Wrapper
RFE(estimator=LogisticRegression(), n_features_to_select=2).fit_transform(data_df)
print("0000")
