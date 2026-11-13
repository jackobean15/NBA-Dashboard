import pandas as pd
from nba_api.stats.endpoints import leaguegamefinder
from nba_api.stats.library.parameters import SeasonTypeAllStar

season = "2026-27"

player_games = leaguegamefinder.LeagueGameFinder(
    season_nullable=season,
    season_type_nullable=SeasonTypeAllStar.regular,
    player_or_team_abbreviation="P",
    )

df = player_games.get_data_frames()[0]
print(df.shape)
df.head()

stats = df[[
    "GAME_ID",
    "GAME_DATE",
    "PLAYER_ID",
    "PLAYER_NAME",
    "TEAM_ABBREVIATION",
    "MATCHUP",

    "MIN",
    "FGM",
    "FGA",
    "FTM",
    "FTA",
    "FG3M",
    "OREB",
    "DREB",
    "REB",
    "AST",
    "STL",
    "BLK",
    "TOV",
    "PTS",
    "WL"
]].sort_values(["GAME_DATE", "GAME_ID"])
stats.to_csv("nba_2026_27_player_game_stats_updatedlast.csv", index=False)
