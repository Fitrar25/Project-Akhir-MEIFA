import pickle

# global variable
global model

def load():
    global model
    model = pickle.load(open('model/model_ds.pkl', 'rb'))

def Prediksi(data):
    Prediction = model.predict(data)
    pred = Prediction
    rec_str = pred.item()[:]
    return rec_str

