from mylib.help_functions import load_team_data, get_statistics, get_median_stats, filter_top_n_teams, plot_wins, calculate_team_percentages, plot_team_percentages

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
    main(file_path_input_main, top_teams_input_main, team_name_input_main, games_per_season_input_main)
