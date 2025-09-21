AI Workout Planner
This project is a machine learning-based workout planner that suggests a personalized workout routine based on user input.

Project Structure
README.md: This file, providing an overview of the project.

requirements.txt: A list of Python dependencies required to run the project.

data_generation.py: A script to generate synthetic workout data.

model_training.py: A script to train the machine learning model.

app.py: The Flask backend that serves the model's predictions.

index.html: The frontend user interface for the workout planner.

workout_data.csv: The generated dataset (will be created by data_generation.py).

workout_model.pkl: The trained machine learning model (will be created by model_training.py).

Step-by-Step Instructions
1. Set Up Your Environment
First, make sure you have Python 3 installed. Then, create a virtual environment to keep your project dependencies isolated.

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

2. Install Dependencies
Install all the required libraries using the requirements.txt file.

pip install -r requirements.txt

3. Generate Data
Create the synthetic dataset that our model will learn from.

python data_generation.py

This will create a file named workout_data.csv.

4. Train the Model
Now, train the machine learning model using the data you just generated.

python model_training.py

This will create a file named workout_model.pkl. This file contains the "brain" of our planner.

5. Run the Web Application
Finally, start the Flask web server to bring your application to life.

flask --app app run

Once the server is running, open your web browser and go to http://127.0.0.1:5000 to see and use your AI Workout Planner!

How It Works
Data: We create a dataset of fictional users with attributes like age, fitness level, goals, and available time. Each user is assigned a suitable workout plan.

Model: We use a simple classification model (like a Decision Tree) to learn the patterns between a user's attributes and their recommended workout plan.

Backend: The Flask application loads the trained model. When a user submits their information from the frontend, the backend uses the model to predict the best workout plan.

Frontend: A simple HTML page with a form sends the user's data to the backend and displays the recommended workout plan it receives in return.


