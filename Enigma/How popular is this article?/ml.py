import gc
import numpy
import pandas
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error

train = pandas.read_csv("train.csv", header = None)

feature = range(270)
feature.remove(0)
feature.remove(269)

train.loc[train[1] == "Sunday" , 1] = 0.0
train.loc[train[1] == "Monday" , 1] = 1.0
train.loc[train[1] == "Tuesday" , 1] = 2.0
train.loc[train[1] == "Wednesday" , 1] = 3.0
train.loc[train[1] == "Thursday" , 1] = 4.0
train.loc[train[1] == "Friday" , 1] = 5.0
train.loc[train[1] == "Saturday" , 1] = 6.0

train.loc[train[2] == "Sunday" , 2] = 0.0
train.loc[train[2] == "Monday" , 2] = 1.0
train.loc[train[2] == "Tuesday" , 2] = 2.0
train.loc[train[2] == "Wednesday" , 2] = 3.0
train.loc[train[2] == "Thursday" , 2] = 4.0
train.loc[train[2] == "Friday" , 2] = 5.0
train.loc[train[2] == "Saturday" , 2] = 6.0


X = train[feature]
y = train[269]

del train
gc.collect()

limit = int(0.3*X.shape[0])

# clf = linear_model.LinearRegression()
clf = make_pipeline(PolynomialFeatures(2), linear_model.LinearRegression())
clf.fit(X[0:limit],y[0:limit])
print(mean_squared_error(clf.predict(X[limit:]),y[limit:]))

# clf.fit(X,y)

test = pandas.read_csv("test.csv", header = None)

test.loc[test[1] == "Sunday" , 1] = 0.0
test.loc[test[1] == "Monday" , 1] = 1.0
test.loc[test[1] == "Tuesday" , 1] = 2.0
test.loc[test[1] == "Wednesday" , 1] = 3.0
test.loc[test[1] == "Thursday" , 1] = 4.0
test.loc[test[1] == "Friday" , 1] = 5.0
test.loc[test[1] == "Saturday" , 1] = 6.0

test.loc[test[2] == "Sunday" , 2] = 0.0
test.loc[test[2] == "Monday" , 2] = 1.0
test.loc[test[2] == "Tuesday" , 2] = 2.0
test.loc[test[2] == "Wednesday" , 2] = 3.0
test.loc[test[2] == "Thursday" , 2] = 4.0
test.loc[test[2] == "Friday" , 2] = 5.0
test.loc[test[2] == "Saturday" , 2] = 6.0


prediction = clf.predict(test[feature])

submission = pandas.DataFrame({
                "Id":test[0],
                "Prediction":prediction
            })

submission.to_csv("Data-Miners_output.csv", sep=',' , header=False , index=False)
