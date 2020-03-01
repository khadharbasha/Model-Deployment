#importing libraries
from flask import Flask, render_template, request
from sklearn.externals import joblib

#creating instance of the class
app=Flask(__name__)

#to tell flask what url shoud trigger the function index()
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/result", methods=['POST'])
def predict():
    print("I am here in predict function")
    print(request.method)
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            print(data)
            years_of_experience = float(data["experience"])
            print(years_of_experience)

            # load the model from disk
            lin_reg = joblib.load("./linear_regression_model.pkl")
            print(lin_reg.intercept_)
            
        except ValueError:
            return render_template("result.html", salary="Please enter a number.")

        print("Prediction = ", lin_reg.predict([[years_of_experience]]))
        Prediction = lin_reg.predict([[years_of_experience]])
    
    print(type(Prediction))
    salary = Prediction.tolist()
    print(salary)

    return render_template("result.html", prediction=salary[0])

if __name__ == "__main__":
	app.run(port = 8000, debug=True)
