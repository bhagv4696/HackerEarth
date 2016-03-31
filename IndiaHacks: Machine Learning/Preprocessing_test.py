import gc
import pandas as pd

test_modified = pd.read_csv("test.csv")
users = pd.read_csv("users.csv")

test_modified = test_modified.merge(users,how='inner',on='user_id')

del users
gc.collect()

problems = pd.read_csv("problems.csv")

test_modified = test_modified.merge(problems,how='inner',on='problem_id')

del problems
gc.collect()

features = list(test_modified.columns.values)

features.remove("skills")

test_modified.loc[test_modified["level"] == "V-E" , "level"] = 0.0
test_modified.loc[test_modified["level"] == "E" , "level"] = 1.0
test_modified.loc[test_modified["level"] == "E-M" , "level"] = 2.0
test_modified.loc[test_modified["level"] == "M" , "level"] = 3.0
test_modified.loc[test_modified["level"] == "M-H" , "level"] = 4.0
test_modified.loc[test_modified["level"] == "H" , "level"] = 5.0
test_modified.loc[test_modified["level"] == "O" , "level"] = 0

tag1 = pd.unique(test_modified.tag1.values.ravel())

for i in range(len(tag1)):
	if str(tag1[i]) != "nan":
		test_modified.loc[test_modified["tag1"] == tag1[i] , "tag1"] = i

tag2 = pd.unique(test_modified.tag2.values.ravel())

for i in range(len(tag2)):
	if str(tag2[i]) != "nan":
		test_modified.loc[test_modified["tag2"] == tag2[i] , "tag2"] = i

tag3 = pd.unique(test_modified.tag3.values.ravel())

for i in range(len(tag3)):
	if str(tag3[i]) != "nan":
		test_modified.loc[test_modified["tag3"] == tag3[i] , "tag3"] = i

tag4 = pd.unique(test_modified.tag4.values.ravel())

for i in range(len(tag4)):
	if str(tag4[i]) != "nan":
		test_modified.loc[test_modified["tag4"] == tag4[i] , "tag4"] = i

tag5 = pd.unique(test_modified.tag5.values.ravel())

for i in range(len(tag5)):
	if str(tag5[i]) != "nan":
		test_modified.loc[test_modified["tag5"] == tag5[i] , "tag5"] = i

test_modified.loc[test_modified["user_type"] == "S" , "user_type"] = 0.0
test_modified.loc[test_modified["user_type"] == "W" , "user_type"] = 1.0
test_modified.loc[test_modified["user_type"] == "NA" , "user_type"] = 2.0

for i in range(len(features)):
	test_modified[features[i]] = test_modified[features[i]].fillna(test_modified[features[i]].value_counts().idxmax())

# value_counts().idxmax()

test_modified = test_modified.dropna(axis=0,how="any")

print(len(test_modified))
test_modified.drop_duplicates(inplace=True)
print(len(test_modified))

test_modified[features].to_csv("test_pre.csv",index=False)