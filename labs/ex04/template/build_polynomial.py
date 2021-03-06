# -*- coding: utf-8 -*-
"""implement a polynomial basis function."""

import numpy as np


def build_poly(x, degree):
    """polynomial basis functions for input data x, for j=0 up to j=degree."""
    # ***************************************************
    # INSERT YOUR CODE HERE
    # polynomial basis function: TODO
    # this function should return the matrix formed
    # by applying the polynomial basis to the input data
    # ***************************************************
    poly_matrix = np.array(np.ones(len(x)))
    for d in range(1,degree+1) :
        poly_matrix = (np.vstack((poly_matrix,x**d)))
        
    return poly_matrix
