# game_engine.py

import random

# --- CORE GAME STATE (LOADED FROM state.json) ---
# For now, hardcode your starting status to test the engine:
PLAYER_STATE = {
    "tokens": 500,
    "current_rank": "Rookie",
    "total_wins": 2,
    "engine_stress": 0,
    "noise_meter": 0
}

# --- CAR STATS (Mad Marauder) ---
MAD_MARAUDER = {
    "name": "Mad Marauder",
    "wins": 2,
    "upgrades": ["Predictive ECU"],
    "shift_bonus": 1.2 # Base Max Speed Multiplier
}

# --- SHIFT FUNCTION (The Core Logic) ---
def run_shift(player_input, rpm_light="Yellow"):
    """
    Simulates a gear shift and calculates the outcome, noise, and combo bonus.
    """
    if player_input == '1':
        # 1. Determine Shift Quality (Perfect, Good, Missed)
        if rpm_light == "Yellow":
            # Perfect Shift Logic
            bonus = 10  # Base token reward
            noise_impact = 0
            stress_impact = 0
            message = "PERFECT SHIFT! 🟡"
            
        elif rpm_light == "Green":
            # Good Shift Logic
            bonus = 5
            noise_impact = 5
            stress_impact = 0
            message = "GOOD SHIFT! 🟢"
            
        else: # Red or bad input
            # Missed Shift/Stall Logic
            bonus = 0
            noise_impact = 25
            stress_impact = 20
            message = "MISSED SHIFT! 🔴 (-5s Penalty)"
        
        # 2. Update Player Stats (This is the critical part)
        PLAYER_STATE["tokens"] += bonus
        PLAYER_STATE["noise_meter"] += noise_impact
        # Add stress to the Mad Marauder (This would track per-car in a full system)
        print(f"{message} | Noise: +{noise_impact}% | Tokens: +{bonus}")
        
    elif player_input == 'start_race':
        # Initial launch logic
        print("Starting Race...")

    else:
        print("Invalid Command.")

# --- INITIAL TEST ---
# To run this function, you'd use a simple loop, but for now:
# run_shift('1', rpm_light='Yellow')
# print(f"Current Tokens: {PLAYER_STATE['tokens']}")
