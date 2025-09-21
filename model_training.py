import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

print("Starting data processing for the Kaggle dataset...")

# Load the dataset
try:
    df = pd.read_csv('mega_gym.csv')
    print("mega_gym.csv loaded successfully.")
except FileNotFoundError:
    print("\n[FATAL ERROR] 'mega_gym.csv' not found in the project folder.")
    print("Please download it from Kaggle and place it in the same directory as this script.")
    exit()

# Select and clean relevant columns
df = df[['Title', 'Desc', 'Type', 'BodyPart', 'Equipment', 'Level']]
df.dropna(inplace=True)
print(f"Dataset shape after cleaning: {df.shape}")

# Initialize encoders for categorical data
encoders = {
    'Type': LabelEncoder(),
    'BodyPart': LabelEncoder(),
    'Equipment': LabelEncoder(),
    'Level': LabelEncoder()
}

# We are not actually using the encoded values in the new logic,
# but we save them in case we want to use them in the future.
# The main purpose is to have the original text data available.

# Save the cleaned dataframe and the encoders together in one file
saved_data = {
    'data': df,  # We are saving the original text data, not the encoded data
    'encoders': encoders
}

joblib.dump(saved_data, 'workout_logic.pkl')

print("\nData processing complete!")
print("Cleaned data and encoders have been successfully saved to 'workout_logic.pkl'.")

