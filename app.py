from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

method = ['GET','POST']

@app.route('/', methods = ['GET','POST'])
def index():
    if request.method == 'POST':
        rates = float(request.form.get('rates'))
        model_reg = joblib.load('regression_DBS')
        result_reg = model_reg.predict([[rates]])
        model_tree = joblib.load('tree_DBS')
        result_tree = model_tree.predict([[rates]])
        return(render_template('index.html', result1 = result_reg, result2 = result_tree))
    else:
        return(render_template('index.html', result1 = 'waiting', result2 = 'waiting'))

if __name__ == '__main__':
    app.run()