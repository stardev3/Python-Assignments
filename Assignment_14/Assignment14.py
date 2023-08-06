import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

def ChkAccuracy(Data,Target):

    Data_train, Data_test, Target_train, Target_test = train_test_split(Data, Target, test_size=0.5)
    Clasifier = KNeighborsClassifier()

    Clasifier.fit(Data_train, Target_train)
    Predictions = Clasifier.predict(Data_test)

    Accuracy = accuracy_score(Target_test, Predictions)
    return Accuracy

def MarvellousPlayPredictor(data_path):

    data = pd.read_csv(data_path,index_col=0)

    print("Size of actual dataset is : ",len(data))

    feature_names = ['Weather','Temperature']

    print("Names of features",feature_names)

    weather = data.Weather
    Temperature = data.Temperature
    play = data.Play

    le = preprocessing.LabelEncoder()

    weather_encoded = le.fit_transform(weather)
    print(weather_encoded)

    temp_encoded = le.fit_transform(Temperature)
    label = le.fit_transform(play)

    print(temp_encoded)

    features = list(zip(weather_encoded,temp_encoded))

    model = KNeighborsClassifier(n_neighbors = 3)

    model.fit(features,label)

    predicted = model.predict([[0,2]])

    if predicted:
        print("You can Play")
    else:
        print("You cannot Play")

    Accuracy = ChkAccuracy(features,label)
    return Accuracy

def main():
    print("-----------ML Application-------------")

    Ret = MarvellousPlayPredictor("PlayPredictor.csv")
    print("Accuracy of Data Model is : ",Ret*100)

if __name__ == "__main__":
    main()