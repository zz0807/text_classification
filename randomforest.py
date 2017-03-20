from sklearn.ensemble import RandomForestClassifier

data=[[0,0,0],[1,1,1],[2,2,2],[1,1,1],[2,2,2],[3,3,3],[1,1,1],[4,4,4],[5,5,5],[2,2,2]]
arget=['0','1','2','1','2','3','1','4','5','2']
rf = RandomForestClassifier()
rf.fit(data,arget)
RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',  
            max_depth=None, max_features='auto', max_leaf_nodes=None,  
            min_samples_leaf=1, min_samples_split=2,  
            min_weight_fraction_leaf=0.0, n_estimators=10, n_jobs=1,  
            oob_score=False, random_state=None, verbose=0,  
            warm_start=False)  
print rf.predict_proba([[2,2,2]])
#[[ 0.  0.  0.  0.  1.]]
