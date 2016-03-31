import gc 	
import pandas as pd

train = pd.read_csv("submissions.csv")
users = pd.read_csv("users.csv")

train = train.merge(users,how='inner',on='user_id')

del users
gc.collect()

problems = pd.read_csv("problems.csv")

train = train.merge(problems,how='inner',on='problem_id')

del problems
gc.collect()

features = list(train.columns.values)

features.remove("skills")
features.remove("execution_time")
features.remove("result")
features.remove("language_used")

train = train[train.solved_status != "UK"]

train.loc[train["solved_status"] == "AT" , "solved_status"] = float(0)
train.loc[train["solved_status"] == "SO" , "solved_status"] = float(1)

train.loc[train["result"] == "PAC" , "result"] = 0.0
train.loc[train["result"] == "AC" , "result"] = 1.0
train.loc[train["result"] == "TLE" , "result"] = 2.0
train.loc[train["result"] == "CE" , "result"] = 3.0
train.loc[train["result"] == "RE" , "result"] = 4.0
train.loc[train["result"] == "WA" , "result"] = 5.0

train.loc[train["level"] == "V-E" , "level"] = 0.0
train.loc[train["level"] == "E" , "level"] = 1.0
train.loc[train["level"] == "E-M" , "level"] = 2.0
train.loc[train["level"] == "M" , "level"] = 3.0
train.loc[train["level"] == "M-H" , "level"] = 4.0
train.loc[train["level"] == "H" , "level"] = 5.0

language = pd.unique(train.language_used.values.ravel())

for i in range(len(language)):
	if str(language[i]) != "nan":
		train.loc[train["language_used"] == language[i] , "language_used"] = i

tag1 = pd.unique(train.tag1.values.ravel())

for i in range(len(tag1)):
	if str(tag1[i]) != "nan":
		train.loc[train["tag1"] == tag1[i] , "tag1"] = i

tag2 = pd.unique(train.tag2.values.ravel())

for i in range(len(tag2)):
	if str(tag2[i]) != "nan":
		train.loc[train["tag2"] == tag2[i] , "tag2"] = i

tag3 = pd.unique(train.tag3.values.ravel())

for i in range(len(tag3)):
	if str(tag3[i]) != "nan":
		train.loc[train["tag3"] == tag3[i] , "tag3"] = i

tag4 = pd.unique(train.tag4.values.ravel())

for i in range(len(tag4)):
	if str(tag4[i]) != "nan":
		train.loc[train["tag4"] == tag4[i] , "tag4"] = i

tag5 = pd.unique(train.tag5.values.ravel())

for i in range(len(tag5)):
	if str(tag5[i]) != "nan":
		train.loc[train["tag5"] == tag5[i] , "tag5"] = i

train.loc[train["user_type"] == "S" , "user_type"] = 0.0
train.loc[train["user_type"] == "W" , "user_type"] = 1.0
train.loc[train["user_type"] == "NA" , "user_type"] = 2.0

for i in range(len(features)):
	train[features[i]] = train[features[i]].fillna(train[features[i]].value_counts().idxmax())

# value_counts().idxmax()

train = train[features].dropna(axis=0,how="any")

print(len(train))
train.drop_duplicates(inplace=True)
print(len(train))

train[features].to_csv("train_pre.csv",index=False)