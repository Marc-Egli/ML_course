# -*- coding: utf-8 -*-
"""Exercise 3.

Split the dataset based on the given ratio.
"""


import numpy as np


def split_data(x, y, ratio, seed=1):
    """
    split the dataset based on the split ratio. If ratio is 0.8 
    you will have 80% of your data set dedicated to training 
    and the rest dedicated to testing
    """
    # set seed
    np.random.seed(seed)
    x_train = []
    y_train = []
    x_test = []
    y_test = []
    for a in range(len(y)):
        if np.random.uniform() <= ratio :
            x_train.append(x[a])
            y_train.append(y[a])
        else :
            x_test.append(x[a])
            y_test.append(y[a])
    return np.array(x_train) , np.array(x_test) , np.array(y_train) , np.array(y_test)
