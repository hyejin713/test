from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections
import csv
import os
from os import path
import random
import tempfile
import time

import numpy as np
from tensorflow.contrib.framework import deprecated
from tensorflow.python.platform import gfile

Dataset = collections.namedtuple('Dataset', ['data', 'target', 'num_examples'])
Datasets = collections.namedtuple('Datasets', ['train', 'validation', 'test'])

def load_csv_with_header(filename,
                         target_dtype,
                         features_dtype,
                         target_column=-1):
    """Load dataset from CSV file with a header row."""
    with gfile.Open(filename) as csv_file:
        data_file = csv.reader(csv_file)
        header = next(data_file)
        n_samples = int(header[0])
        n_features = int(header[1])
        data = np.zeros((n_samples, n_features), dtype=features_dtype)
        target = np.zeros((n_samples,), dtype=target_dtype)

        for i, row in enumerate(data_file):
            target[i] = np.asarray(row.pop(target_column), dtype=target_dtype)
            data[i] = np.asarray(row, dtype=features_dtype)

    return Dataset(data=data, target=target, num_examples=n_samples)


def load_review_data(data_path=None):
    """Load Boston housing dataset.

    Args:
        data_path: string, path to boston dataset (optional)

    Returns:
      Dataset object containing data in-memory.
    """
    if data_path is None:
        module_path = path.dirname(__file__)
        data_path = path.join(module_path, 'data', 'boston_house_prices.csv')
    return load_csv_with_header(
        data_path,
        target_dtype=np.float,
        features_dtype=np.float)

# print(load_boston("./data/make_data.csv"))

