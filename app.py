import pickle
from flask import Flask, request, render_template
import numpy as np

app = Flask(__name__)

# Load the trained model
with open('model/model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get data from the form
        Gender = int(request.form['Gender'])  # Assuming Gender is numeric (0 or 1)
        Age = float(request.form['Age'])
        AcademicPressure = float(request.form['Academic Pressure'])
        WorkPressure = float(request.form['Work Pressure'])
        CGPA = float(request.form['CGPA'])
        StudySatisfaction = float(request.form['Study Satisfaction'])
        JobSatisfaction = float(request.form['Job Satisfaction'])
        SleepDuration = float(request.form['Sleep Duration'])  # Numeric
        DietaryHabits = float(request.form['Dietary Habits'])  # Numeric
        HadSuicidalThoughts = float(request.form['suicidalThoughts'])  # Numeric
        WorkStudyHours = float(request.form['Work/Study Hours'])
        FinancialStress = float(request.form['Financial Stress'])
        FamilyHistory = float(request.form['Family History'])  # Numeric

        # Prepare the data for prediction
        input_data = np.array([[Gender, Age, AcademicPressure, WorkPressure, CGPA, StudySatisfaction, 
                                JobSatisfaction, SleepDuration, DietaryHabits, HadSuicidalThoughts, 
                                WorkStudyHours, FinancialStress, FamilyHistory]])

        # Make a prediction
        prediction = model.predict(input_data)

        # Display the prediction result
        return render_template('index.html', prediction_text=f'Predicted Depression Level: {prediction[0]}')

if __name__ == "__main__":
    app.run(debug=True)
