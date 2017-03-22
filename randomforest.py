from sklearn.ensemble import RandomForestClassifier
from feature_express import fetureExpress

inc = fetureExpress('test.label', 'test1.label')
label, sentence_total = inc.test('test.label')
print label
print sentence_total
# train_data, train_label, test_data, test_label = inc.getfeature()
# rf = RandomForestClassifier()
# rf.fit(train_data, train_label)
# RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
#             max_depth=None, max_features='auto', max_leaf_nodes=None,
#             min_samples_leaf=1, min_samples_split=2,
#             min_weight_fraction_leaf=0.0, n_estimators=10, n_jobs=1,
#             oob_score=False, random_state=None, verbose=0,
#             warm_start=False)
# print rf.predict_proba(test_data)
#[[ 0.  0.  0.  0.  1.]]
