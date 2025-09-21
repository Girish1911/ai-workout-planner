FlexAI: Your Personal AI Workout Planner
FlexAI is a smart web application that generates personalized workout plans based on your fitness level and target muscle group. Powered by Python, Flask, and a real-world Kaggle dataset, it provides dynamic and varied exercise routines to help you reach your fitness goals.

✨ Features
Dynamic Workout Generation: Get a multi-exercise plan tailored to your selections.

Intelligent Fallback Logic: If no "Expert" exercises are found, the app smartly suggests "Intermediate" ones, ensuring you always get a plan.

Specialized "Full Body" Routine: Select "Full Body" to get a comprehensive workout covering all major muscle groups.

Real-World Data: Utilizes the "Mega Gym Dataset" from Kaggle for a wide variety of exercises.

Clean, Responsive UI: A simple and intuitive interface built with Tailwind CSS.

🛠️ Technology Stack
Backend: Python, Flask, Pandas, Joblib

Frontend: HTML, Tailwind CSS, JavaScript

Server: Gunicorn

Deployment: Render

🚀 Getting Started
Follow these instructions to get a local copy up and running.

1. Prerequisites
Make sure you have the following installed on your system:

Git

Python 3.10+

2. Clone the Repository
Open your terminal or command prompt and clone the repository:

git clone [https://github.com/Girish1911/ai-workout-planner.git](https://github.com/Girish1911/ai-workout-planner.git)
cd ai-workout-planner

3. Create and Activate a Virtual Environment
It is crucial to use a virtual environment to manage project dependencies.

On Windows (PowerShell):

python -m venv venv
.\venv\Scripts\Activate

On macOS / Linux:

python3 -m venv venv
source venv/bin/activate

You should see (venv) at the beginning of your terminal prompt.

4. Install Dependencies
Install all the required Python libraries from the requirements.txt file:

pip install -r requirements.txt

5. Download the Dataset
This project uses the "Mega Gym Dataset" from Kaggle.

Download the file from here: https://www.kaggle.com/datasets/niharika41298/mega-gym-dataset

Place the mega_gym.csv file directly inside your project folder (ai-workout-planner/).

🏃‍♀️ Usage
To run the application, you must first process the dataset and then start the web server.

1. Generate the Logic File (One-Time Step)
Run the training script to process the mega_gym.csv file. This creates the workout_logic.pkl file that the application needs to generate plans.

python model_training.py

You only need to do this once.

2. Run the Web Application
Start the Flask server using the following command:

python -m flask --app backend run

Your terminal will show that the server is running. You can now view the application by opening your web browser and navigating to:
http://127.0.0.1:5000

🌐 Live Demo
This application has been successfully deployed on Render. You can try it live here:

https://ai-workout-planner-w6mh.onrender.com

(Note: The free tier on Render may cause the first load to be slow. Please be patient!)

📂 Project File Structure
ai-workout-planner/
│
├── templates/
│   └── index.html         # The main frontend file
│
├── .gitignore             # Tells Git which files to ignore
├── backend.py             # The main Flask application logic
├── model_training.py      # Script to process the dataset
├── requirements.txt       # List of Python dependencies
├── mega_gym.csv           # The raw dataset (must be downloaded)
├── workout_logic.pkl      # The processed data file (generated)
└── README.md              # You are here!
