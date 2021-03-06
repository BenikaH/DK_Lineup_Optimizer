from __future__ import division
from NFL.NFL_Lineup_Generator import NFLLineupGenerator
from NFLGeneralMultipliers import *
import numpy

# taking ratio between projected_points / ppg then std_dev + min projected_points

TEAM_BLACKLIST = ()
PLAYER_BLACKLIST = ()


def NFLFormulaFour(lineup, player_holder):
    if not NFLLineupGenerator.lineup_under_salary_cap(lineup):
        return -100000
    else:
        fitness = get_lineup_player_scores(lineup)
        team_multiplier = get_team_multiplier(lineup)
        games_multiplier = get_game_multiplier(lineup, player_holder.games)
        black_list_multipler = get_blacklist_muiltiplier(lineup, PLAYER_BLACKLIST, TEAM_BLACKLIST)
        return fitness * team_multiplier * games_multiplier * black_list_multipler

def get_player_score(player):
    if not player.projected_points:
        return -100
    if player.projected_points < 5:
        return -100
    if player.ppg <= 5:
        return -100
    return player.projected_points

def get_lineup_player_scores(lineup):
    fitness = []
    for p in lineup:
        fitness_score = get_player_score(p)
        fitness.append(fitness_score)
        p.special_stat = fitness_score
    return sum(fitness) #* (numpy.std(numpy.array(fitness))/ sum(fitness))