import pandas as pd
from python_main import (
    load_team_data,
    get_statistics,
    get_median_stats,
    filter_top_n_teams,
    calculate_team_percentages,
    plot_team_percentages,
)
from io import StringIO
import matplotlib.pyplot as plt


def test_load_team_data():
    csv_data = """team,wins,losses
                    Manchester United,28,5
                    Chelsea,24,8
                    Arsenal,22,10"""
    csv_file = StringIO(csv_data)
    result_df = load_team_data(csv_file)
    assert result_df.shape == (3, 3)
    assert list(result_df.columns) == ["team", "wins", "losses"]


def test_get_statistics():
    csv_data = """team,wins,losses
                    Manchester United,28,5
                    Chelsea,24,8
                    Arsenal,22,10"""

    test_df = pd.read_csv(StringIO(csv_data))
    numeric_data = test_df[["wins", "losses"]]
    stats = get_statistics(numeric_data)
    assert round(stats.loc["mean", "wins"], 2) == 24.67
    assert round(stats.loc["max", "losses"], 2) == 10


def test_get_median_stats():
    # Simulate CSV data
    csv_data = """team,wins,losses
                    Manchester United,28,5
                    Chelsea,24,8
                    Arsenal,22,10"""

    test_df = pd.read_csv(StringIO(csv_data))
    median_stats = get_median_stats(test_df, ["wins", "losses"])
    assert median_stats["wins"] == 24, "Expected median for 'wins' is 24"
    assert median_stats["losses"] == 8, "Expected median for 'losses' is 8"


def test_filter_top_n_teams():
    csv_data = """team,wins,season
Manchester United,28,2023
Chelsea,24,2023
Liverpool,23,2023
Arsenal,22,2023
Tottenham Hotspur,20,2023
Manchester City,30,2023
Leicester City,18,2023"""

    test_df = pd.read_csv(StringIO(csv_data))
    top_teams = [
        "Manchester United",
        "Chelsea",
        "Liverpool",
        "Arsenal",
        "Tottenham Hotspur",
        "Manchester City",
    ]

    filtered_df = filter_top_n_teams(test_df, top_teams)

    assert not filtered_df.empty, "The filtered DataFrame is unexpectedly empty"
    assert len(filtered_df) == 6, "Expected 6 teams in the filtered data"
    assert all(
        team in top_teams for team in filtered_df["team"]
    ), "Filtered data contains teams not in the top 6"


def test_calculate_team_percentages():
    csv_data = """team,wins,losses,season,clean_sheet
Manchester United,28,5,2023,15
Chelsea,24,8,2023,12
Liverpool,23,7,2023,14"""

    test_df = pd.read_csv(StringIO(csv_data))

    games_per_season = 38

    result_df = calculate_team_percentages(
        test_df, "Manchester United", games_per_season
    )

    expected_win_percentage = 28 / games_per_season
    expected_clean_sheet_percentage = 15 / games_per_season

    assert result_df.shape == (1, 7), "The shape of the result DataFrame is incorrect"
    assert (
        result_df.iloc[0]["win_percentage"] == expected_win_percentage
    ), "Win percentage is not as expected"
    assert (
        result_df.iloc[0]["clean_sheet_percentage"] == expected_clean_sheet_percentage
    ), "Clean sheet percentage is not as expected"


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
    test_load_team_data()
    test_get_statistics()
    test_get_median_stats()
    test_calculate_team_percentages()
    test_plot_team_percentages()
    test_filter_top_n_teams()
