"""
Cricket Fielding Performance Analysis
Task Level: Advanced
Author: Student Sports Analyst
Purpose:
- Collect ball-by-ball fielding data
- Store data in spreadsheet format
- Calculate advanced fielding performance score
"""

import pandas as pd

# ------------------------------------------------------------------
# STEP 1: DEFINE WEIGHTS FOR PERFORMANCE METRICS
# ------------------------------------------------------------------
WEIGHTS = {
    "CP": 2,      # Clean Pick
    "GT": 3,      # Good Throw
    "C": 8,       # Catch
    "DC": -6,     # Dropped Catch
    "ST": 7,      # Stumping
    "RO": 8,      # Run Out
    "MRO": -5,    # Missed Run Out
    "DH": 6       # Direct Hit
}

# ------------------------------------------------------------------
# STEP 2: CREATE FIELDING DATASET (Sample Data)
# Each row represents a ball where a fielding event occurred
# ------------------------------------------------------------------
data = [
    # Match, Innings, Team, Player, Ball, Position, Description, Pick, Throw, Runs, Over, Venue
    [1, 1, "India", "Ravindra Jadeja", 2, "Point", "Sharp stop and clean pick", "Clean Pick", "", 2, 5, "Mumbai"],
    [1, 1, "India", "Ravindra Jadeja", 4, "Point", "Quick throw causes run out", "Good Throw", "Run Out", 3, 7, "Mumbai"],
    [1, 1, "India", "Suryakumar Yadav", 1, "Deep Cover", "Dropped a tough catch", "Drop Catch", "", -4, 10, "Mumbai"],
    [1, 1, "India", "Suryakumar Yadav", 5, "Deep Cover", "Excellent boundary save", "Clean Pick", "", 4, 12, "Mumbai"],
    [1, 1, "India", "MS Dhoni", 3, "Wicket Keeper", "Stumping off wide delivery", "", "Stumping", 3, 15, "Mumbai"],
    [1, 1, "India", "MS Dhoni", 6, "Wicket Keeper", "Missed run out chance", "", "Missed Run Out", -2, 18, "Mumbai"],
]

columns = [
    "Match No", "Innings", "Team", "Player Name", "Ballcount",
    "Position", "Short Description", "Pick", "Throw",
    "Runs", "Overcount", "Venue"
]

df = pd.DataFrame(data, columns=columns)

# ------------------------------------------------------------------
# STEP 3: CREATE PERFORMANCE COUNT PER PLAYER
# ------------------------------------------------------------------
def calculate_performance(player_df):
    CP = (player_df["Pick"] == "Clean Pick").sum()
    GT = (player_df["Pick"] == "Good Throw").sum()
    C = (player_df["Pick"] == "Catch").sum()
    DC = (player_df["Pick"] == "Drop Catch").sum()
    ST = (player_df["Throw"] == "Stumping").sum()
    RO = (player_df["Throw"] == "Run Out").sum()
    MRO = (player_df["Throw"] == "Missed Run Out").sum()
    DH = (player_df["Pick"] == "Direct Hit").sum()
    RS = player_df["Runs"].sum()

    PS = (
        CP * WEIGHTS["CP"] +
        GT * WEIGHTS["GT"] +
        C * WEIGHTS["C"] +
        DC * WEIGHTS["DC"] +
        ST * WEIGHTS["ST"] +
        RO * WEIGHTS["RO"] +
        MRO * WEIGHTS["MRO"] +
        DH * WEIGHTS["DH"] +
        RS
    )

    return PS

# ------------------------------------------------------------------
# STEP 4: GENERATE PERFORMANCE SUMMARY
# ------------------------------------------------------------------
summary = []

for player in df["Player Name"].unique():
    player_df = df[df["Player Name"] == player]
    score = calculate_performance(player_df)
    summary.append([player, score])

summary_df = pd.DataFrame(summary, columns=["Player Name", "Performance Score"])

# ------------------------------------------------------------------
# STEP 5: EXPORT DATA TO SPREADSHEET
# ------------------------------------------------------------------
df.to_csv("fielding_data.csv", index=False)
summary_df.to_csv("fielding_performance_summary.csv", index=False)

# ------------------------------------------------------------------
# STEP 6: DISPLAY RESULTS
# ------------------------------------------------------------------
print("Fielding Data:")
print(df)

print("\nFielding Performance Summary:")
print(summary_df)
