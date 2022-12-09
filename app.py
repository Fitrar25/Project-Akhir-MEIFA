import sklearn
from flask import Flask, render_template, request
from model import load, Prediksi

app = Flask(__name__)

# load model dan scaler
load()

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/predict", methods=["POST"])
def predict():
    # menangkap data yang diinput user melalui form
    print(request.form)
    MTK_IPA = int(request.form['MTK_IPA'])
    Indo_IPA = int(request.form['Indo_IPA'])
    Eng_IPA = int(request.form['Eng_IPA'])
    Biologi_IPA = int(request.form['Biologi_IPA'])
    Kimia_IPA = int(request.form['Kimia_IPA'])
    Fisika_IPA = int(request.form['MTK_IPA'])
    MataPelajaranDisukai_IPA = int(request.form['MataPelajaranDisukai_IPA'])
    Hobi_IPA = int(request.form['Hobi_IPA'])
    Skill_IPA = int(request.form['Skill_IPA'])
    Cita2_IPA = int(request.form['Cita2_IPA'])

    # melakukan prediksi menggunakan model yang telah dibuat
    data = [[MTK_IPA,Indo_IPA,Eng_IPA,Biologi_IPA,Kimia_IPA,Fisika_IPA,MataPelajaranDisukai_IPA,Hobi_IPA,Skill_IPA,Cita2_IPA]]
    hasil = Prediksi(data)
    return render_template('index.html', hasil=hasil)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)