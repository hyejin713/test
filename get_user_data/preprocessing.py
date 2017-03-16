import pandas
from tensorflow.contrib import skflow
import random

def parse(path):
    g = gzip.open(path, 'rb')
    for l in g:
        yield eval(l)

def getListCategory():
    i = 0
    listCategory = []
    path = '/storage1/data/input/metadata.json.gz'
    for d in parse(path):
        "salesRank": {"Toys & Games": 211836}
        salesRankData = d["salesRank"]
        category = salesRankData.keys()[0]
        listCategory.append(category)
        # rank = salesRankData.get(category)
    return listCategory
            
            
        
# Process categorical variables into ids.(category of salesRank)
le = preprocessing.LabelEncoder()

# change value
le.fit(getListCategory())
dirname = '/storage1/data/input/data_per_user/'
reviewerFolder = os.listdir(dirname)
for filename in reviewerFolder:
    full_filename = os.path.join(dirname, filename)
    if os.path.isdir(full_filename):
        train = pandas.read_csv(full_filename + '/' + filename + '.csv')
        y = (int(train.pop('overall'))>=3?1:0)
        categorical_vars = ['brand', 'categories']
        continues_vars = ['price', 'salesRank']
        X = train[categorical_vars + continues_vars].fillna(0)
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        
        # Process categorical variables into ids.
        X_train = X_train.copy()
        X_test = X_test.copy()
        categorical_var_encoders = {}
        for var in categorical_vars:
          le = LabelEncoder().fit(X_train[var])
          X_train[var + '_ids'] = le.transform(X_train[var])
          X_test[var + '_ids'] = le.transform(X_test[var])
          X_train.pop(var)
          X_test.pop(var)
          categorical_var_encoders[var] = le
                
        # classifier = skflow.TensorFlowLinearClassifier(n_classes=2, batch_size=128, steps=500, learning_rate=0.05)
        # classifier.fit(X_train, y_train)
        
        # print(accuracy_score(classifier.predict(X_test), y_test))
        
        
        
