from sklearn.svm import SVC
from sklearn.externals import joblib
import numpy as np
from feature_extractor import get_feature_matrix,process_test_file,get_test_matrix


X=get_feature_matrix(1,134)
#y=np.concatenate((np.ones((1,50)).astype("int32"),2*np.ones((1,50)).astype("int32")),axis=1).T
train_key=np.concatenate((np.ones((1,134)).astype("int32"),2*np.ones((1,134)).astype("int32")),axis=1).T
train_key=np.ravel(train_key)



X_test=get_test_matrix(1,93)
test_key=np.concatenate((2*np.ones((1,60)).astype("int32"),np.ones((1,33)).astype("int32")),axis=1).T
test_key=np.ravel(test_key)


clf=SVC(kernel="rbf")
clf.fit(X,train_key)

train_prediction=clf.predict(X)

train_accuracy=(np.sum(train_key==train_prediction))/268
test_prediction=clf.predict(X_test)
test_accuracy=(np.sum(test_key==test_prediction))/93
print("train_accuracy ",train_accuracy)
print("test_accuracy ",test_accuracy)
#print(clf.predict(X_test))
joblib.dump(clf,"trained_model.pkl")

#print(clf.predict(X_test.reshape(1,-1)))
