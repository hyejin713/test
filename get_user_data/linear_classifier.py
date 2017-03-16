import pandas
from tensorflow.contrib import skflow
import random

dirname = '/storage1/data/input/data_per_user/'
reviewerFolder = os.listdir(dirname)
for filename in reviewerFolder:
    full_filename = os.path.join(dirname, filename)
    if os.path.isdir(full_filename):
        train = pandas.read_csv(full_filename + '/' + filename + '.csv')
        
        random.seed(42)
        y, X = (train['Survived']>=3?1:0), train[['Age', 'SibSp', 'Fare']].fillna(0)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        classifier = skflow.TensorFlowLinearClassifier(n_classes=2, batch_size=128, steps=500, learning_rate=0.05)
        classifier.fit(X_train, y_train)
        
        print(accuracy_score(classifier.predict(X_test), y_test))
