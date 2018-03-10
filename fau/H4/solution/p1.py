# Python Programming.
# Homework 4, problem 1
# Instructor: Dr. Ionut Cardei
# Do not distribute.


import csv


def read_ranking(f):
    """
    Can be called with the file of ratings ranking or with the file of top grossing rankings.
    Both files have the same format, with the last column having different meaning.
    Score (below) will be either the ratings score (e.g. 8.9) or US box office grossing $$.
    
    Returns tuple ({(title,year):(rank,score)}, [(rank, (title,year), score)])
    First is a dictionary indexed by (title, year) and with value (rank, score).
    Second is a sorted list with tuples (rank, (title,year), score).

    For the top rating file the line format is: Rank,Title,Year,IMDB Rating.
    For the top grossing file the line format is: Rank,Title,Year,USBoxOffice$$
    May throw parsing and IO exceptions.
    The csv module helps parsing titles containing comma, such as "Monsters, Inc."

    precondition: f is an open CSV file
    """
    rdr = csv.reader(f)
    next(rdr)     # skip header
    # tr_lst is a list with one tuple per movie: (year, title, year, score)
    t_lst = [(int(ls[0]), ls[1], int(ls[2]), float(ls[3])) for ls in rdr]

    # tr_dict is a dict with key (title,year) and value tuples (rank, score):
    t_dct = { (ls[1], ls[2]):(ls[0], ls[3]) for ls in t_lst }

    # in case the file does not come already sorted:
    # sorted list with tuples (rank, (title,year):
    t_ranked_lst = sorted([(ls[0], (ls[1], ls[2]), ls[3]) for ls in t_lst ])
    return (t_dct, t_ranked_lst)
    

def read_casts(f):
    """
    Returns a dictionary {(title,year):(Director,Actor1,Actor2,Actor3,Actor4,Actor5)}
    File format: Title,Year,Director,Actor1,Actor2,Actor3,Actor4,Actor5
    Parses the casts file.
    May throw parsing and IO exceptions.
    precondition: f is an open CSV file
    """
    rdr = csv.reader(f)
    # dictionary comprehension for each list returned by reader:
    casts_dct = {(ml[0], int(ml[1])):(ml[2], ml[3],ml[4],ml[5],ml[6],ml[7])
                 for ml in rdr}
    return casts_dct


def top_mv_directors(top_dct, cast_dct, top_mv_lst):
    """Return a ranked list of (director, movie_count) tuples in top_mv_lst.
    Will throw KeyError if a (title,year) is not found in the cast dictionary.
    This function works both for top rated and top grossing movie files/data structures.

    precondition: parameters are properly initialized
    """
    counts_dct = {}   # for counting movies in a top ranked list with director name as key
    for mv_ls in top_mv_lst:
        mv_yr = mv_ls[1]      # (movie, year) tuple in list with ratings ranked list
        director_name = cast_dct[mv_yr][0]
        counts_dct[director_name] = 1 + counts_dct.get(director_name, 0)    # use default 0 if not in already

    # get list with (count,director) tuples
    count_dir_lst = [(count, director_name) for director_name,count in counts_dct.items()]
    return sorted(count_dir_lst, reverse=True)          # reverse=True sorts in descending order


def top_rated_actors(top_dct, cast_dct, top_mv_lst):
    """Return a ranked list of (count, actor) tuples where count is the number of times
    the actor is in the top rated movie list top_mv_lst.
    Will throw KeyError if a (title,year) is not found in the cast dictionary.
    This function works both for top rated and top grossing movie files/data structures.

    precondition: parameters are properly initialized
    """
    counts_dct = {}   # for counting actors in a top ranked list with actor name as key
    for mv_ls in top_mv_lst:
        mv_yr = mv_ls[1]      # (movie, year) tuple in list with ratings ranked list

        # iterate over actors sublist:
        for ac in cast_dct[mv_yr][1:]:
            counts_dct[ac] = 1 + counts_dct.get(ac, 0)
            
    # get list with (count,director) tuples
    count_act_lst = [(count, actor) for actor,count in counts_dct.items()]
    return sorted(count_act_lst, reverse=True)


def combined_score(ratings_rank, grossings_rank):
    """Returns the combined score based on ratings and gross.
    precondition: 0 < precondition, parameters <= 250
    """
    return 500 - ratings_rank - grossings_rank


def top_combined_movies(tr_dct, tg_dct):
    """Return a sorted list with (rank, score, movie_title, year) tuples
    where the score is combined from the ratings rank and the grossing rank.
    precondition: parameters are properly initialized
    """
    i = 1   
    score_lst = []
    for mv_yr in tr_dct:
        if mv_yr in tg_dct:
            score = combined_score(tr_dct[mv_yr][0], tg_dct[mv_yr][0])
            # add a tuple with useful info: (score, title, yr, ratings_rank, grossing_rank)
            score_lst.append((score, mv_yr[0], mv_yr[1], tr_dct[mv_yr][0], tg_dct[mv_yr][0]))

    sorted_score_lst = sorted(score_lst, reverse=True)    # sorted by score
    combined_scores_lst = []
    for (score, title, yr, ratings_rank, grossing_rank) in sorted_score_lst:
        combined_scores_lst.append((i, score, title, yr, ratings_rank, grossing_rank))
        i += 1
    return combined_scores_lst


def actors_movie_gross_split(mv_yr, tg_dct, cast_dct):
    """returns the gross split per actor for a particular movie-year mv_yr as a dictionary.
    precondition: parameters are properly initialized
    """
    split = 16.0 / 31      # split for first-billed actor
    actor_split_dct = {}
    gross = tg_dct[mv_yr][1]
    for ac in cast_dct[mv_yr][1:]:     # element 0 in cast_dct is the director
        actor_split_dct[ac] = actor_split_dct.get(ac, 0) + split * gross
        split /= 2.0     # half will be split by remaining actors on the list
    return actor_split_dct


def top_grossing_actors(tg_dct, cast_dct):
    """return ranked list with actors and how much they "earned" based on the
    split from the problem.
    precondition: parameters are properly initialized
    """
    actor_total_dct = {}    
    # iterate over movies:
    for mv_yr in tg_dct:
        # get the split for the current (movie,year):
        actor_split_dct = actors_movie_gross_split(mv_yr, tg_dct, cast_dct)

        # now add the movie split for each actor to the total for each actor:
        for ac in actor_split_dct:
            actor_total_dct[ac] = actor_total_dct.get(ac, 0) + actor_split_dct[ac]

    actor_total_lst = [(total, actor) for (actor,total) in actor_total_dct.items()]

    # sort list on total:
    sorted_actor_totals = sorted(actor_total_lst, reverse=True)

    # create new list with rank prepended to each tuple:
    return [(1+index, total, actor) for (index, (total, actor)) in enumerate(sorted_actor_totals)]
    #  enumerate([x,y,z]) returns an iterator over collection (0,x), (1,y), (2,z)
        

def top_gross_actor_pairs(tg_dct, cast_dct):
    """returns a sorted list with: [rank, total, (actor1, actor2)]
    whith the total for an actor pair, where tuple (actor1, actor2) are sorted lexicographically.
    precondition: parameters are properly initialized
    """
    # the algorithm is:
    # act_pair_dct = {}   # an empty dictionary keyed by sorted pair of actor names
    # for each top-grossing movie m:
    #     compute actor_gross_dct   # a dictionary with gross$$ allocation per actor for movie m
    #     for each sorted pair (a1,a2) of actors playing in movie m:
    #          act_pair_dct[(a1,a2)] += actor_gross_dct[a1] + actor_gross_dct[a2]
    # return act_pair_dct
    act_pair_dct = {}
    for mv_yr in tg_dct:
        actor_split_dct = actors_movie_gross_split(mv_yr, tg_dct, cast_dct)
        actor_lst = cast_dct[mv_yr][1:]

        # generate pairs of actors in this movie:
        n = len(actor_lst)      # number of actors in list (5 currently)
        for i in range(0,n-1):
            for j in range(i+1, n):
                # sorted() returns a list and we need a tuple since it's used as key in a dictionary
                actor_pair = tuple(sorted((actor_lst[i], actor_lst[j])))
                # add to pair total the $$ for actor1 and the $$ for actor2:
                act_pair_dct[actor_pair] = actor_split_dct[actor_lst[i]] + actor_split_dct[actor_lst[j]] \
                    + act_pair_dct.get(actor_pair, 0)
            
    sl = sorted([(pair_total, actor1, actor2) for ((actor1, actor2), pair_total) in act_pair_dct.items()], reverse=True)
    return [(rank, pair_total, actor1, actor2) for (rank, (pair_total, actor1, actor2)) in enumerate(sl)]



# Homework part a)
def print_top_rated_directors(tr_dct, casts_dct, tr_rank_lst):
    """print the sorted list of the directors with the most movies in the top rated movies file
    precondition: parameters are properly initialized
    """
    print("List with top rated directors")
    print("-" * 50)
    sorted_dir_lst = top_mv_directors(tr_dct, casts_dct, tr_rank_lst)
    print("\n".join([str(tup) for tup in sorted_dir_lst]))
    print("\n\n")


# part b): Displays a ranking (descending) of the directors with the most movies in the top
# grossing list. 
def print_top_grossing_directors(tg_dct, casts_dct, tg_rank_lst):
    """print the sorted list of the directors with the most movies in the top rated movies file.
    precondition: parameters are properly initialized
    """
    print("List with top grossing directors")
    print("-" * 50)
    sorted_dir_lst = top_mv_directors(tg_dct, casts_dct, tg_rank_lst)
    print("\n".join([str(tup) for tup in sorted_dir_lst]))
    print("\n\n")


# part c): Displays a ranking (descending) of the actors with the most movie credits from the top rated list.
def print_top_rated_actors(tr_dct, casts_dct, tr_rank_lst):
    """print the sorted list of the actors with the most movies in the top rated movies file.
    precondition: parameters are properly initialized"""
    print("List with top rated actors")
    print("-" * 50)
    sorted_act_lst = top_rated_actors(tr_dct, casts_dct, tr_rank_lst)
    print("\n".join([str(tup) for tup in sorted_act_lst]))
    print("\n\n")


# part d): Displays a ranking of movies (descending) based on a combined rating/grossing score. The score for
# a movie with rating rank r and grossing rank g is 500-r-g. Exclude movies that are only on one list and
# not on the other. Print only the top 5 movie titles, with their year, with a proper title above.
def print_top_combined_lst(tr_dct, tg_dct):
    """prints ranking of movies (descending) based on a combined rating/grossing score.
    precondition: parameters are properly initialized
    """
    print("List with top movies (combined score)")
    print("-" * 50)
    combined_lst = top_combined_movies(tr_dct, tg_dct)
    print("\n".join([str(tup) for tup in combined_lst]))
    print("\n\n")





# part e): Displays a ranking (descending) with the actors who brought in the most box office money,
# based on the top grossing movie list. For a movie with gross ticket sales amount s,
# the 5 actors on the cast list will split amount s using the formula in the homework.
def print_top_grossing_actors(tg_dct, cast_dct):
    """prints list with top-grossing actors.
    precondition: parameters are properly initialized
    """
    print("List with top grossing actors")
    print("-" * 50)
    act_lst = top_grossing_actors(tg_dct, cast_dct)
    #print("\n".join([str(tup) for tup in act_lst]))

    # limit to top 100:
    for (rank, gross, actor) in act_lst[:100]:
        print("{:>4} {:>.0f} {:<}".format(rank, gross, actor))
    print("\n\n")



# part f): Displays a ranking (descending) with the pairs of actors who brought in the most box office
# money for movies in which they acted together. For a movie with gross ticket sales amount s,
# the 5 actors on the cast list will split amount s.
def print_top_grossing_actor_pairs(tg_dct, cast_dct):
    """prints list with top-grossing actor pairs.
    precondition: parameters are properly initialized
    """
    print("List with top grossing actor pairs (pair in alphabetical order)")
    print("-" * 50)
    act_pair_lst = top_gross_actor_pairs(tg_dct, cast_dct)

    # limit to top 100:
    for (rank, pair_total, actor1, actor2) in act_pair_lst[:100]:
        print("{:<5}  {:>12.0f}  {:20}  {:20}".format(rank, pair_total, actor1, actor2))
    print("\n\n")





try:
    cast_f = None
    topranked_f = None
    topgrossing_f = None
    cast_f = open("imdb-top-casts.csv", "r")
    casts_dct = read_casts(cast_f)

    topranked_f = None
    topranked_f = open("imdb-top-rated.csv", "r")
    (tr_dct, tr_rank_lst) = read_ranking(topranked_f)

    topgrossing_f = open("imdb-top-grossing.csv", "r")
    (tg_dct, tg_rank_lst) = read_ranking(topgrossing_f)

    #print(casts_dct)
    #print(tr_dct)
    #print(tr_rank_lst)

    # a)
    print_top_rated_directors(tr_dct, casts_dct, tr_rank_lst)

    # b)
    print_top_grossing_directors(tg_dct, casts_dct, tg_rank_lst)


    # c)
    print_top_rated_actors(tr_dct, casts_dct, tr_rank_lst)

    # d)
    print_top_combined_lst(tr_dct, tg_dct)

    # e)
    print_top_grossing_actors(tg_dct, casts_dct)


    # f)
    print_top_grossing_actor_pairs(tg_dct, casts_dct)
    
except ValueError as err:
    print("Error:", err)
except FileNotFoundError as err:
    print("Error:", err)
except:
    print("Error")
    exit(1)
finally:
    if cast_f:
        cast_f.close()
    if topranked_f:
        topranked_f.close()

