import gc
import pandas as pd
import numpy as np
# from sklearn import svm
# from sklearn import linear_model
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

train = pd.read_csv("train_pre.csv")

features = list(train.columns.values)

features.remove("problem_id")
features.remove("user_id")
features.remove("solved_status")

# clf = tree.DecisionTreeClassifier()

train = train.dropna(axis=0,how="any")

limit = len(train)

# _validation = train.ix[limit:]

X = train[features].ix[0:limit]
y = train["solved_status"].ix[0:limit]

del train
gc.collect()

# clf = linear_model.SGDClassifier(n_iter=1000)
# clf = svm.LinearSVC(C=1e5)
# clf = KNeighborsClassifier(n_neighbors = 100)
# clf = tree.DecisionTreeClassifier()
clf = RandomForestClassifier(n_estimators=100, criterion="entropy", max_features=None)
clf.fit(X,y)

# print("Accuracy = " + str(accuracy_score(_validation["solved_status"],clf.predict(_validation[features]))))

test = pd.read_csv("test_pre.csv")

X = test[features]
Id = test["Id"]

del test
gc.collect()

prediction = clf.predict(X)
prediction = map(int,prediction)

submission = pd.DataFrame({
		"Id":Id,
		"solved_status":prediction
	})

submission.to_csv("submission.csv",index=False)