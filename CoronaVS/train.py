import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import pickle

df = pd.read_csv('CoronaData.csv')
def data_split(data,ratio):
    np.random.seed(42)
    shuffle=np.random.permutation(len(data))
    test_data_len=int(len(data)*ratio)
    test_indices=shuffle[:test_data_len]
    train_indices=shuffle[test_data_len:]
    return data.iloc[test_indices], data.iloc[train_indices]

test,train = data_split(df,0.25)
X_train=train[["Fever","BodyPain","Age","Runnynose","DiffBreathing","Travel"]].to_numpy()
X_test=test[["Fever","BodyPain","Age","Runnynose","DiffBreathing","Travel"]].to_numpy()
Y_train=train[["Probability"]].to_numpy().reshape(1500,)
Y_test=test[["Probability"]].to_numpy().reshape(499,)
clf= LogisticRegression()
clf.fit(X_train,Y_train)

file=open('model.pkl','wb')
pickle.dump(clf,file)
file.close()





