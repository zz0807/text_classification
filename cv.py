from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
import numpy as np


def k_fold(X, y):
   results = []
   X = np.array(X)
   y = np.array(y)
   sample_leaf_options = list(range(1, 500, 3))
   n_estimators_options = list(range(1, 1000, 5))
   max_feature_options = ['auto','log2']
   for leaf_size in sample_leaf_options:
      for n_estimators_size in n_estimators_options:
         for feature_size in max_feature_options:
            rf = RandomForestClassifier(max_features=feature_size,n_estimators=n_estimators_size,min_samples_leaf=leaf_size)
            scores = cross_val_score(rf, X, y, cv=10)
            results.append((leaf_size, n_estimators_size,feature_size,scores.mean()))
   print(max(results, key=lambda x: x[3]))

