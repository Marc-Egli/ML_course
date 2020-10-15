# -*- coding: utf-8 -*-
"""Exercise 3.

Ridge Regression
"""

import numpy as np
from costs import compute_mse

def ridge_regression(y, tx, lambda_):
    """implement ridge regression."""
    # ***************************************************
    # INSERT YOUR CODE HERE
    # ridge regression: TODO
    # ***************************************************
    toinverse = tx.transpose() @ tx
    w = np.linalg.inv(toinverse + 2*lambda_*tx.shape[0]*np.identity(toinverse.shape[0])) \
        @ (tx.transpose() @ y)
    
    loss = compute_mse(y,tx,w)
    return loss, w
