# CptS 355 - Spring 2022 - Assignment 3 - Python

# Please include your name and the names of the students with whom you discussed any of the problems in this homework
# Name: Jillian Plahn 
# Collaborators: 

debugging = False
def debug(*s): 
     if debugging: 
          print(*s)

## problem 1 - all_games - 8%
def all_games(wsu_games):
     new_game_log = {}
     for year,wsu_games in wsu_games.items():
          for team,scores in wsu_games.items():
               if team not in new_game_log.keys():
                    new_game_log[team] = {}
               new_game_log[team][year] = scores
     return new_game_log

from functools import reduce
## problem 2 - common_teams - 15%
def common_teams (wsu_games):
# get the total number of years games have been played
     number_years = len(wsu_games.keys())
# will store common_teams in new dict
     common_teams = {}
# go through all the years and games and store data in common_teams, with format:
# Team : [(score, score)... ]
     for year, wsu_games in wsu_games.items():
          for team, scores in wsu_games.items():
               if team not in common_teams.keys():
                    common_teams[team] = []
               common_teams[team].append(scores)
# find teams that should be removed as they do not have scores for total years
     remove_teams = []
     for team, team_scores in common_teams.items():
          if len(team_scores) != number_years:
               remove_teams.append(team)
# remove the teams from common_teams
     for i in remove_teams:
          del common_teams[i]
     return common_teams

## problem 3 - get_wins - 16%
def get_wins(wsu_games, team):
     #gives year and score for the given team [(year, (score))]
     map_result = list(map(lambda x: (x[0],x[1].get(team)), wsu_games.items()))
     # filters out the scores that are not wins for the team 
     map_helper = lambda t: tuple(filter(lambda x: x[1] != None and x[1][0] > x[1][1], t))
     map_result = list(map_helper(map_result))
     return map_result

## problem 4 - wins_by_year - 16%
def check_win(wsu_score, opp_score):
    if(wsu_score > opp_score):
        return 1
    return 0

def wins_by_year(wsu_games): 
     year_wins_by_game = list(map(lambda year_scores:(year_scores[0], list(map(lambda scores: check_win(scores[0], scores[1]), list(year_scores[1].values())))), wsu_games.items()));
     year_total_wins = list(map(lambda yw: (yw[0], reduce(lambda a,b:a+b, yw[1])), year_wins_by_game))
     return (year_total_wins)

## problem 5 - longest_path - 16% 
def helper_function(listOfLists, dict):
    #make a copy of the list
    copiedList = listOfLists.copy()
    #getting the paths (the things that A can touch)
    for nodes, paths in dict.items():
        if len(paths) == 1:
            #theres only one thing the node can go to so append
            copiedList.append(paths)
        elif len(paths) > 1:
            # there is multiple things it can go to so need to make a copy and append
            copiedList.append(paths)
    return copiedList

def update_paths(update_ll, update_dict):
    # need to go through the list of lists sublists to append
    for sub_list in update_ll:
        # make a copy of the sub_list to keep for updating
        copy_sub_list = sub_list.copy()
       
        #-1 gives you last item in a list, then get that items paths
        sub_list_last = copy_sub_list[-1]
        sub_list_last_paths = get_node_paths(sub_list_last, update_dict)
       
        len_sub_list_last_paths = len(sub_list_last_paths)
       
        # keep track of updates, as after first one need to update the update_ll
        sub_lists_updated = 0
        # for each path off of the last value in a given sub list, update
        for path in sub_list_last_paths:
            #if sub_list[0] != 'A':
                #print("not head_node: ")
           
            # NEED TO ADD CODE: IF YOU HAVE A LOOP IN YOUR GRAPH/DICT, YOU NEED TO NOT
            # TO APPEND THAT VALUE
            # when appending if value is in list the delet it check sublist  
            # sublist.count C if 0 add it if not zero

            # first one, so just update the orginal sub list
            if sub_lists_updated == 0:
                sub_list.append(path)
                sub_lists_updated = sub_lists_updated + 1
            # after updating the first one, need to update the update_ll with a new sub list
            elif sub_lists_updated != 0:
                temp_sub_list = copy_sub_list.copy()
                temp_sub_list.append(path)
                update_ll.append(temp_sub_list)

# for a given node, get the paths
def get_node_paths(get_node, get_graph):
    node_paths = {}
    for key, value in get_graph.items():
        if(key == get_node):
            node_paths = value
    return node_paths

# helper function to get the full count of items in the list of list
# needed to know when you are not adding anymore items, as each sublist's last value
# is the deliminator
def get_size(get_ll):
    size_count = 0
    for sub_list in get_ll:
        size_count = size_count + len(sub_list)
    return size_count

def longest_path(graph, node):
    # start with empty list
    listOfLists = []
   
    # add node as first list
    listOfLists.append([node])
    listOfLists_len = len(listOfLists)
   
    # make first update to the lists in lists of lists and get the size
    # so you can loop through until update_paths size before being called
    # and after being called are the same
    size_count_prev = 0
    update_paths(listOfLists, graph)
    size_count_cur = get_size(listOfLists)
   
   # keep calling until the size are the same
    while size_count_prev != size_count_cur:
          size_count_prev = size_count_cur
          update_paths(listOfLists, graph)
         
   
     # find the longest sublist in list of paths and return the length of longest sublist 
    maxPathLength = max(len(x) for x in listOfLists)

    return maxPathLength


## problem 6 - counter - 20% 