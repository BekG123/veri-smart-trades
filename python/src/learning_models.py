import numpy as np

# load data 
from data_preprocessing import final_tree

# start learning 

def find_best_tree_splitting(X, gradients, hessians, lambda_=1):
    """
    Finds the optimal split for an XGBoost tree using gradient boosting and hessian information
    
    Parameters:
    X (np.ndarray): Feature matrix of shape (n_samples, n_features)
    gradients (np.ndarray): First derivatives of loss
    hessians (np.ndarray): Second derivatives of loss
    lambda_ (float): L2 regularization parameter
    
    Returns:
    dict: Best split information containing:
        - 'feature': Best feature index to split
        - 'threshold': Best split threshold
        - 'gain': Computed gain for this split
        - 'left_value': Leaf value for left child
        - 'right_value': Leaf value for right child
    """
    best_split = {
        'feature': None,
        'threshold': None,
        'gain': -np.inf,
        'left_value': 0,
        'right_value': 0
    }
    
    n_samples, n_features = X.shape
    G_total = gradients.sum()
    H_total = hessians.sum()
    
    for feature in range(n_features):
        # Get sorted feature values and indices
        feature_values = X[:, feature]
        sorted_indices = np.argsort(feature_values)
        sorted_values = feature_values[sorted_indices]
        
        # Initialize running sums
        G_left = 0.0
        H_left = 0.0
        
        # Calculate midpoints between sorted values
        for i in range(1, n_samples):
            # Skip duplicate values
            if sorted_values[i] == sorted_values[i-1]:
                continue
                
            # Current threshold (midpoint)
            threshold = (sorted_values[i] + sorted_values[i-1]) / 2
            
            # Update running sums
            G_left += gradients[sorted_indices[i-1]]
            H_left += hessians[sorted_indices[i-1]]
            
            G_right = G_total - G_left
            H_right = H_total - H_left
            
            # Calculate gain (XGBoost's formula)
            gain = (G_left**2 / (H_left + lambda_) +
                    G_right**2 / (H_right + lambda_) -
                    (G_total**2) / (H_total + lambda_))
            
            # Update best split if this is better
            if gain > best_split['gain']:
                best_split['feature'] = feature
                best_split['threshold'] = threshold
                best_split['gain'] = gain
                best_split['left_value'] = -G_left / (H_left + lambda_)
                best_split['right_value'] = -G_right / (H_right + lambda_)
    
    return best_split

# Initial guess 

# Implementation of gamma-pruning

# Thresholds

