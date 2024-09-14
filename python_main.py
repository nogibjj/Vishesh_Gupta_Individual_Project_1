import pandas as pd
import matplotlib.pyplot as plt

# Function to load data
def load_team_data(file_path):
    return pd.read_csv(file_path)

# Function to get basic statistics
def get_statistics(team_data):
    return team_data.describe()

# Function to get median values for selected columns
def get_median_stats(team_data, columns):
    return team_data[columns].median()

# Function to filter top teams
def filter_top_n_teams(team_data, top_teams_list):
    return team_data[team_data["team"].isin(top_teams_list)][
        ["team", "wins", "season"]
    ].reset_index(drop=True)

# Function to plot wins for top teams
def plot_wins(top_teams_data):
    plt.figure(figsize=(12, 8))
    for team in top_teams_data["team"].unique():
        team_specific = top_teams_data[top_teams_data["team"] == team]
        plt.plot(team_specific["season"], team_specific["wins"], marker="o", label=team)

    plt.xlabel("Season")
    plt.ylabel("Wins")
    plt.title("Season Wins for Each Team")
    plt.legend(title="Team")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("top_teams_wins.png")
    plt.close()

# Function to calculate win and clean sheet percentages for a team
def calculate_team_percentages(team_data, team_name, games_per_season):
    team_specific = team_data[team_data["team"] == team_name][
        ["team", "wins", "losses", "season", "clean_sheet"]
    ].reset_index(drop=True)
    team_specific["win_percentage"] = team_specific["wins"] / games_per_season
    team_specific["clean_sheet_percentage"] = (
        team_specific["clean_sheet"] / games_per_season
    )
    return team_specific

# Function to plot win and clean sheet percentages
def plot_team_percentages(team_percentages_data):
    plt.figure(figsize=(10, 6))
    plt.plot(
        team_percentages_data["season"],
        team_percentages_data["win_percentage"],
        label="Win Percentage",
        marker="o",
    )
    plt.plot(
        team_percentages_data["season"],
        team_percentages_data["clean_sheet_percentage"],
        label="Clean Sheet Percentage",
        marker="o",
    )

    plt.xlabel("Season")
    plt.ylabel("Percentage")
    plt.title("Comparison of Win Percentage and Clean Sheet Percentage")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig("win_clean_sheet_relation.png")
    plt.close()

def main(file_path_input, top_teams_input, team_name_input, games_per_season_input):
    # Load data
    team_data = load_team_data(file_path_input)

    # Get stats
    print(get_statistics(team_data))
    print(
        get_median_stats(
            team_data, ["wins", "losses", "goals", "total_yel_card", "total_red_card"]
        )
    )

    # Filter top teams and plot
    top_teams_data = filter_top_n_teams(team_data, top_teams_input)
    plot_wins(top_teams_data)

    # Calculate and plot win and clean sheet percentages for the selected team
    team_percentages_data = calculate_team_percentages(
        team_data, team_name_input, games_per_season_input
    )
    plot_team_percentages(team_percentages_data)

if __name__ == "__main__":
    # File path and variables
    file_path_input = "stats.csv"
    top_teams_input = [
        "Manchester United",
        "Chelsea",
        "Liverpool",
        "Arsenal",
        "Tottenham Hotspur",
        "Manchester City",
    ]
    team_name_input = "Manchester United"
    games_per_season_input = 38.0

    # Run main function
    main(file_path_input, top_teams_input, team_name_input, games_per_season_input)
