
# Import Flask class to create the web app,
# render_template to load HTML files,
# and request to handle incoming form data
from flask import Flask, render_template, request 

# Import NumPy for numerical operations (used for reshaping input data)
import numpy as np 

# Import pickle to load saved machine learning models
import pickle 
 
# Create a Flask application instance
app = Flask(__name__) 
 
# Define a route for the home page ('/')
# It accepts both POST (form submission) and GET (page load) requests
@app.route('/', methods=['POST', 'GET']) 
def Home(): 

    # Check if the request method is POST (i.e., user submitted the form)
    if request.method == 'POST': 
        
        # Open the saved logistic regression model file in read-binary mode
        with open('pickle_logistic.pkl', 'rb') as file: 
            # Load the trained model from the file
            model = pickle.load(file) 
         
        # Open the label encoder file (used to convert numeric predictions back to labels)
        with open('label_encoder.pkl', 'rb') as file: 
            # Load the label encoder
            le = pickle.load(file) 
 
        # Extract all values submitted from the form
        # request.form.values() returns them as strings,
        # so convert each value to float
        features = [float(x) for x in request.form.values()] 
        
        # Convert the list into a NumPy array and reshape it
        # reshape(1, -1) makes it a 2D array with 1 row (required by ML models)
        final_features = np.array(features).reshape(1, -1) 
 
        # Use the loaded model to make a prediction based on input features
        predict = model.predict(final_features) 
        
        # Convert the numeric prediction back to the original label
        # (e.g., 0 → "No", 1 → "Yes")
        result = le.inverse_transform(predict)[0] 
 
        # Render the HTML template and pass the prediction result to it
        return render_template('index.html', msg=result) 
 
    # If the request is GET (user just opened the page),
    # simply render the HTML page without any prediction
    return render_template('index.html') 
 
# Run the Flask app in debug mode
# debug=True enables auto-reload and shows errors in the browser
app.run(debug=True)



