from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd
import random

# Initialize the Flask application
app = Flask(__name__)

# --- Load Preprocessed Data and Encoders ---
try:
    saved_data = joblib.load('workout_logic.pkl')
    df = saved_data['data']
    encoders = saved_data['encoders']
    # IMPORTANT: Drop any rows where crucial text is missing to prevent errors
    df.dropna(subset=['Title', 'Desc', 'BodyPart', 'Level'], inplace=True)
    print("Model and encoders loaded successfully!")
except FileNotFoundError:
    print("[ERROR] workout_logic.pkl not found. Please run model_training.py first.")
    df = None
    encoders = None
except Exception as e:
    print(f"[ERROR] An error occurred while loading the model: {e}")
    df = None
    encoders = None

# --- Route for the Home Page ---
@app.route('/')
def home():
    """Renders the main page."""
    return render_template('index.html')

# --- Route for Workout Prediction ---
@app.route('/predict', methods=['POST'])
def predict():
    """
    Receives user input, intelligently filters the dataset, and returns a dynamic workout plan.
    Includes fallback logic and special handling for "Full Body" workouts.
    """
    if df is None or encoders is None:
        return jsonify({'error': 'Server is not ready. Model data missing.'}), 500

    try:
        data = request.get_json(force=True)
        level = data['level']
        body_part = data['body_part']

        # --- NEW: Special handling for "Full Body" ---
        if body_part == 'Full Body':
            workout_plan_list = []
            major_muscle_groups = {
                'Chest': 'Chest',
                'Back': 'Lats|Back',
                'Legs': 'Quadriceps|Hamstrings|Glutes',
                'Shoulders': 'Shoulders',
                'Arms': 'Biceps|Triceps'
            }

            levels_in_order = ['Expert', 'Intermediate', 'Beginner']
            start_index = levels_in_order.index(level)

            for group_name, group_search_term in major_muscle_groups.items():
                exercise_found = False
                # Fallback logic for each muscle group in the full body workout
                for i in range(start_index, len(levels_in_order)):
                    current_level = levels_in_order[i]
                    level_mask = df['Level'] == current_level
                    group_mask = df['BodyPart'].str.contains(group_search_term, case=False, regex=True)
                    
                    possible_exercises = df[level_mask & group_mask]
                    
                    if not possible_exercises.empty:
                        workout_plan_list.append(possible_exercises.sample(n=1))
                        exercise_found = True
                        break # Found an exercise for this group, move to the next group
                
                if not exercise_found:
                    print(f"Could not find any {group_name} exercise for the selected level or fallbacks.")

            if not workout_plan_list:
                return jsonify({'error': f'Could not generate a Full Body workout for "{level}" level. Not enough variety in the dataset.'})
            
            workout_plan_df = pd.concat(workout_plan_list)
            workout_plan = workout_plan_df.to_dict(orient='records')
            return jsonify(workout_plan)

        # --- Existing Logic for specific muscle groups (NOW MORE ROBUST) ---
        body_part_map = {
            'Back': 'Lats|Lower Back|Middle Back|Traps',
            'Legs': 'Quadriceps|Hamstrings|Glutes|Calves|Adductors',
            'Arms': 'Biceps|Triceps|Forearms',
            'Core': 'Abdominals',
            'Shoulders': 'Shoulders|Traps', # <-- Expanded to include Traps
            'Chest': 'Chest' # Kept specific to avoid confusion with triceps exercises
        }
        
        search_term = body_part_map.get(body_part, body_part)

        levels_in_order = ['Expert', 'Intermediate', 'Beginner']
        start_index = levels_in_order.index(level)
        
        filtered_df = pd.DataFrame()
        
        for i in range(start_index, len(levels_in_order)):
            current_level = levels_in_order[i]
            level_mask = df['Level'] == current_level
            body_part_mask = df['BodyPart'].str.contains(search_term, case=False, regex=True)
            
            attempt_df = df[level_mask & body_part_mask]
            
            if not attempt_df.empty:
                filtered_df = attempt_df
                print(f"Found exercises for '{body_part}' at '{current_level}' level (fallback from '{level}').")
                break

        if filtered_df.empty:
            return jsonify({'error': f'No exercises found for "{body_part}" at any difficulty level. Please try another muscle group.'})

        num_exercises = min(5, len(filtered_df))
        workout_plan = filtered_df.sample(n=num_exercises).to_dict(orient='records')

        return jsonify(workout_plan)

    except Exception as e:
        print(f"[ERROR] An error occurred during prediction: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': 'An unexpected server error occurred. Please check logs.'}), 500

# --- Run the App ---
if __name__ == '__main__':
    app.run(debug=True)

