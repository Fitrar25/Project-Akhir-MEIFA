import pickle
import pandas as pd

# global variable
global model

def load():
    global model
    model = pickle.load(open('model/model_ds.pkl', 'rb'))

df = df_rec = pd.read_csv("model/survey.csv")
df_rec = df_rec[['ProgramStudi','TipeStudi']]
df_rec.drop_duplicates(inplace=True)


def Recommender(X):
    a = df_rec[df_rec['TipeStudi']==X].values
    b = a[:,0]
    return b

def Prediksi(data):
    Prediction = model.predict(data)
    pred = Prediction
    rec_str = pred.item()[:]
    return rec_str

def detail(data):
    Prediction = model.predict(data)
    pred = Prediction
    rec_str = pred.item()[:]
    rec = Recommender(rec_str)
    return rec
