import pandas as pd
import numpy as np
import random

# --- Configuration ---
NUM_SAMPLES = 5000

# --- Lists of Options ---
FITNESS_LEVELS = ['Beginner', 'Intermediate', 'Advanced']
GOALS = ['Lose Weight', 'Build Muscle', 'Improve Endurance', 'General Fitness']
TIME_PER_SESSION = [20, 30, 45, 60] # in minutes

# --- Workout Plan Definitions ---
# Each plan is a dictionary with exercises for different muscle groups.
WORKOUT_PLANS = {
    'Beginner Weight Loss': {
        'Warm-up': '5 min jogging',
        'Workout': '3x10 Bodyweight Squats, 3x10 Push-ups (on knees), 3x10 Lunges (each leg), 3x30s Plank',
        'Cardio': '15 min brisk walking',
        'Cool-down': '5 min stretching'
    },
    'Beginner Muscle Build': {
        'Warm-up': '5 min dynamic stretching',
        'Workout': '3x8 Dumbbell Goblet Squats, 3x8 Dumbbell Bench Press, 3x8 Dumbbell Rows, 3x10 Bicep Curls, 3x10 Tricep Dips (on bench)',
        'Cardio': '10 min light cycling',
        'Cool-down': '5 min stretching'
    },
    'Intermediate Weight Loss': {
        'Warm-up': '5 min jump rope',
        'Workout': '4x12 Barbell Squats, 4x12 Bench Press, 4x12 Pull-ups (assisted if needed), 3x15 Leg Press',
        'Cardio': '20 min HIIT (e.g., sprints on treadmill)',
        'Cool-down': '5 min foam rolling'
    },
    'Intermediate Muscle Build': {
        'Warm-up': '5 min rowing',
        'Workout': '4x10 Deadlifts, 4x10 Overhead Press, 4x10 Bent-over Rows, 3x12 Dumbbell Flyes, 3x12 Skull Crushers',
        'Cardio': '15 min incline walking',
        'Cool-down': '5 min stretching'
    },
    'Advanced Weight Loss': {
        'Warm-up': '10 min dynamic mobility',
        'Workout': '5x5 Heavy Squats, 5x5 Heavy Bench Press, 5x5 Heavy Deadlifts, 3xAMRAP Pull-ups',
        'Cardio': '30 min interval running',
        'Cool-down': '10 min stretching and foam rolling'
    },
    'Advanced Muscle Build': {
        'Warm-up': '10 min light cardio and mobility',
        'Workout': '5/3/1 program for main lifts (Squat, Bench, Deadlift, OHP), Accessory work: 4x12 Lat Pulldowns, 4x12 Leg Curls, 4x15 Calf Raises',
        'Cardio': 'None (focus on lifting)',
        'Cool-down': '10 min stretching'
    },
    'Endurance Builder': {
        'Warm-up': '10 min light jogging',
        'Workout': 'Circuit Training: 3 rounds of (15x Kettlebell Swings, 15x Box Jumps, 15x Burpees, 1 min rest)',
        'Cardio': '45 min steady-state running or cycling',
        'Cool-down': '10 min stretching'
    },
    'General Fitness': {
        'Warm-up': '5 min dynamic stretches',
        'Workout': 'Full Body: 3x12 Goblet Squats, 3x12 Push-ups, 3x12 Dumbbell Rows, 3x12 Overhead Press, 3x30s Plank',
        'Cardio': '20 min on elliptical or bike',
        'Cool-down': '5 min stretching'
    }
}

plan_names = list(WORKOUT_PLANS.keys())

# --- Data Generation Logic ---
data = []

for _ in range(NUM_SAMPLES):
    age = np.random.randint(18, 65)
    fitness_level = random.choice(FITNESS_LEVELS)
    goal = random.choice(GOALS)
    time_available = random.choice(TIME_PER_SESSION)
    
    # --- Rule-based Plan Assignment ---
    # This is where we create the "logic" our ML model will learn
    assigned_plan = ''
    if goal == 'Lose Weight':
        if fitness_level == 'Beginner':
            assigned_plan = 'Beginner Weight Loss'
        elif fitness_level == 'Intermediate':
            assigned_plan = 'Intermediate Weight Loss'
        else:
            assigned_plan = 'Advanced Weight Loss'
    elif goal == 'Build Muscle':
        if fitness_level == 'Beginner':
            assigned_plan = 'Beginner Muscle Build'
        elif fitness_level == 'Intermediate':
            assigned_plan = 'Intermediate Muscle Build'
        else:
            assigned_plan = 'Advanced Muscle Build'
    elif goal == 'Improve Endurance':
        assigned_plan = 'Endurance Builder'
    else: # General Fitness
        assigned_plan = 'General Fitness'

    # Add some noise/randomness to make the dataset more realistic
    if random.random() < 0.1: # 10% chance to get a random plan
        assigned_plan = random.choice(plan_names)

    data.append([age, fitness_level, goal, time_available, assigned_plan])

# --- Create and Save DataFrame ---
df = pd.DataFrame(data, columns=['age', 'fitness_level', 'goal', 'time_available', 'workout_plan'])

# Save to CSV
df.to_csv('workout_data.csv', index=False)

print(f"Successfully generated {NUM_SAMPLES} samples and saved to workout_data.csv")
print(df.head())
