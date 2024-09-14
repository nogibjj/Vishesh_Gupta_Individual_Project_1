from mylib.help_functions import (
    load_team_data,
    get_statistics,
    get_median_stats,
    filter_top_n_teams,
    plot_wins,
    calculate_team_percentages,
)
import matplotlib.pyplot as plt

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
    plt.show()

def save_to_md():
    with open("summary_statistics.md", "a", encoding="utf-8") as file:
        file.write("\n")
        file.write("![Top Teams Wins](top_teams_wins.png)\n")
        file.write("![Win and Clean Sheet Percentages](win_clean_sheet_relation.png)\n")


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
    file_path_input_main = "stats.csv"
    top_teams_input_main = [
        "Manchester United",
        "Chelsea",
        "Liverpool",
        "Arsenal",
        "Tottenham Hotspur",
        "Manchester City",
    ]
    team_name_input_main = "Manchester United"
    games_per_season_input_main = 38.0

    # Run main function
    main(
        file_path_input_main,
        top_teams_input_main,
        team_name_input_main,
        games_per_season_input_main,
    )
    save_to_md()
