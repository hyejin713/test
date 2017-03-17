import pandas as pd
import tensorflow as tf
from sklearn import metrics, cross_validation
import random
import os
import numpy as np

COLUMNS = ["asin","price","salesRank","brand","categories","overall"]
FEATURES = ["price","overall"]
LABEL = "overall"

def input_fn(data_set):
    feature_cols = {k: tf.constant(data_set[k].values) for k in FEATURES}
    # print(data_set[LABEL].values)
    labels = tf.constant(data_set[LABEL].values)
    return feature_cols, labels

dirname = '/storage1/data/output/'
# reviewerFolder = os.listdir(dirname)
# for filename in reviewerFolder:
#     full_filename = os.path.join(dirname, 'A3SP1IWWAGJCAV')
#     if os.path.isdir(full_filename):
print("filename: " + "/storage1/data/output/AUCXT9K30SHYF/AUCXT9K30SHYF.csv")
reviewFileName = "/storage1/data/output/AUCXT9K30SHYF/AUCXT9K30SHYF.csv"
random.seed(42)
loadData = pd.read_csv(reviewFileName, skipinitialspace=True,
                           skiprows=1, header=None, names=COLUMNS)
loadData['overall'] = (loadData['overall'] >= 3.0).astype(int)
training_set = loadData[["price","overall"]]
# print(training_set)
pd.to_numeric(training_set["price"])
test_set = loadData[["price","overall"]]

prediction_set = loadData[["price","overall"]]

print(training_set.dtypes)
print(test_set.dtypes)
print(prediction_set.dtypes)

feature_cols = [tf.contrib.layers.real_valued_column(k)
                for k in FEATURES]

regressor = tf.contrib.learn.DNNClassifier(feature_columns=feature_cols,
                                            hidden_units=[10],
                                            n_classes=2,
                                            model_dir="/storage1/tmp")
regressor.fit(input_fn=lambda: input_fn(training_set), steps=5000)

# Evaluate accuracy.
ev = regressor.evaluate(input_fn=lambda: input_fn(test_set), steps=1)
loss_score = ev["loss"]
print("Loss: {0:f}".format(loss_score))

results = regressor.evaluate(input_fn=lambda: input_fn(test_set), steps=1)
for key in sorted(results):
    print "%s: %s" % (key, results[key])

y = regressor.predict(input_fn=lambda: input_fn(prediction_set))
print ("Predictions: {}".format(str(y)))