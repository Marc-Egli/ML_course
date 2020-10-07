# -*- coding: utf-8 -*-
"""Function used to compute the loss."""
import numpy as np

def compute_loss(y, tx, w):
    """Calculate the loss.

    You can calculate the loss using mse or mae.
    """
    # ***************************************************
    # INSERT YOUR CODE HERE
    # TODO: compute loss by MSE / MAE
    # ***************************************************
    return np.sum(np.power(y - tx@w,2))/len(y)
