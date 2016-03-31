import gc
import pandas
import numpy
from sklearn import preprocessing
from sklearn import svm
from sklearn.metrics import accuracy_score

train = pandas.read_csv("train_data.csv")

feature = list(train.columns.values)
feature.remove("Id")
feature.remove("Influential")

# X = train[feature]
# y = train["Influential"]

X = preprocessing.scale(train[feature])
y = train["Influential"]

# del train
# gc.collect()

# clf = svm.SVC()
clf = svm.LinearSVC(C=1e2)
# limit = int(0.8*X.shape[0])
# clf.fit(X[0:limit],y[0:limit])
# print(accuracy_score(clf.predict(X[limit:]),y[limit:]))

clf.fit(X,y)

del train
gc.collect()


test = pandas.read_csv("test_data.csv")

prediction = clf.predict(test[feature])


submission = pandas.DataFrame({
                "Id":test["Id"],
                "prediction":prediction
        })

submission.to_csv("Data-Miners_output.csv", sep=',' , header=False , index=False)
