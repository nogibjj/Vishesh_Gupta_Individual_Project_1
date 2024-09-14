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


# Function to filter top 6 teams
def filter_top_n_teams(team_data, top_teams):
    return team_data[team_data["team"].isin(top_teams)][
        ["team", "wins", "season"]
    ].reset_index(drop=True)


# Function to plot wins for top 6 teams
def plot_wins(top_6_teams):
    plt.figure(figsize=(12, 8))
    for team in top_6_teams["team"].unique():
        team_specific = top_6_teams[top_6_teams["team"] == team]
        plt.plot(team_specific["season"], team_specific["wins"], marker="o", label=team)

    plt.xlabel("Season")
    plt.ylabel("Wins")
    plt.title("Season Wins for Each Team")
    plt.legend(title="Team")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("top 6 teams win")
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
def plot_team_percentages(team_specific):
    plt.figure(figsize=(10, 6))
    plt.plot(
        team_specific["season"],
        team_specific["win_percentage"],
        label="Win Percentage",
        marker="o",
    )
    plt.plot(
        team_specific["season"],
        team_specific["clean_sheet_percentage"],
        label="Clean Sheet Percentage",
        marker="o",
    )

    plt.xlabel("Season")
    plt.ylabel("Percentage")
    plt.title("Comparison of Win Percentage and Clean Sheet Percentage")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig("win_clean_sheet_relation")
    plt.close()


def main(file_path, top_teams, team_name, games_per_season):
    # Load data
    team_data = load_team_data(file_path)

    # Get stats
    print(get_statistics(team_data))
    print(
        get_median_stats(
            team_data, ["wins", "losses", "goals", "total_yel_card", "total_red_card"]
        )
    )

    # Filter top 6 teams and plot
    top_6_teams = filter_top_n_teams(team_data, top_teams)
    plot_wins(top_6_teams)

    # Calculate and plot win and clean sheet percentages for the selected team
    team_percentages = calculate_team_percentages(
        team_data, team_name, games_per_season
    )
    plot_team_percentages(team_percentages)


if __name__ == "__main__":
    # File path and variables
    file_path = "stats.csv"
    top_teams = [
        "Manchester United",
        "Chelsea",
        "Liverpool",
        "Arsenal",
        "Tottenham Hotspur",
        "Manchester City",
    ]
    team_name = "Manchester United"
    games_per_season = 38.0

    # Run main function
    main(file_path, top_teams, team_name, games_per_season)
