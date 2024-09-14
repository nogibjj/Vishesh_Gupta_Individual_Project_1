from python_main import plot_team_percentages
import matplotlib.pyplot as plt
from io import StringIO
import pandas as pd

def test_plot_team_percentages():
    csv_data = """team,wins,losses,season,clean_sheet
Manchester United,28,5,2023,15
Manchester United,26,6,2022,13"""

    test_df = pd.read_csv(StringIO(csv_data))

    games_per_season = 38
    test_df["win_percentage"] = test_df["wins"] / games_per_season
    test_df["clean_sheet_percentage"] = test_df["clean_sheet"] / games_per_season

    team_specific = test_df[test_df["team"] == "Manchester United"]

    try:
        plt.figure()
        plot_team_percentages(team_specific)
        plot_success = True
    except Exception as e:
        plot_success = False
        print(f"Plot failed: {e}")

    assert plot_success, "Plotting function failed to execute properly"

if __name__ == "__main__":
    test_plot_team_percentages()
