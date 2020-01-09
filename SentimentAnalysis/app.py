from flask import Flask, request, render_template, json
import pickle

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    vect = pickle.load(open('vect.pkl','rb'))
    prediction = model.predict(vect.transform([request.form.get("comment")]))
    return render_template('index.html', prediction_text='Yorum analiz sonucu: $ {}'.format(prediction))

@app.route('/predicts',methods=['POST'])
def predicts():
    if model:
        vect = pickle.load(open('vect.pkl','rb'))
        prediction = model.predict(vect.transform([request.form.get("comment")]))
        return str(prediction)
    else:
        return ('No model here to use')
    

if __name__  == '__main__':
    model = pickle.load(open('model.pkl','rb'))
    app.run(debug=True)