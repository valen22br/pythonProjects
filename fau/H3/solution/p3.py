# Python Programming.
# Homework 3, problem 2
# Instructor: Dr. Ionut Cardei
# Do not distribute.

from testif import testif

"""
Homework 3
Problem 3.  LeBron Worship.
"""

def parse_float(s):
    """Parse a float from a string. Deals with "" by returning None.
    """
    s = s.strip()
    if s == "":
        return None
    else:
#        print("s=[{}]".format(s))
        return float(s)

def parse_line(s, string_pos_lst, sep=","):
    """Returns a list with tokens parsed from string s.
    s: the string
    string_pos_lst: list with index positions for columns in sting format
    sep: the token separator
    """
    toks = s.split(sep)
    return [toks[i] if i in string_pos_lst else parse_float(toks[i])
            for i in range(len(toks))]


# part a):
def get_csv_data(f, string_pos_lst, sep=","):
    """Parses a csv file with separator sep and string positions given by
    list string_pos_lst.
    Returns a nested list with a list for each row in the file.
    May throw exception ValueError if float parsing fails.
    """
    if sep == "":
        raise ValueError("invalid separator ''")
    data_lst = []
    data_lst.append(f.readline().strip().split(sep))    # header
    # the remainder of this file:
    data_lst += [parse_line(s, string_pos_lst, sep) for s in f]
    return data_lst
            

# part b):   with list comprehensions
def get_columns(data_lst, cols_lst):
    """Returns selected columns as lists from a list created by get_csv_data().
    The columns are given in the order requried using the cols_lst list.
    data_lst: the nested list with rows
    cols_lst: a list with column names, as identified in the table header list, data_lst[0]
    """

    def find(x, lst):
        """find element x in list lst. Returns index (>=0) if found, or -1."""
        try:
            return lst.index(x)
        except ValueError:
            return -1
        
    # get column# corresponding to column names from the heading (case sensitive!):
    col_idx_lst = [find(col_name, data_lst[0]) for col_name in cols_lst]

    # for invalid column names the values in col_idx_lst will be -1. Filter them:
    col_idx_lst = [col_idx for col_idx in col_idx_lst if col_idx >= 0]

    # range(1, len(data_lst)) to skip the heading in the first row:
    selected_cols_lst = [[data_lst[i][j] for i in range(1, len(data_lst))]
                             for j in col_idx_lst]
    return selected_cols_lst


def get_columns_no_lc(data_lst, cols_lst):
    """Same as get_columns(), but without list comprehensions.
    Read and compare.
    """
    selected_cols_lst = []
    for col_name in cols_lst:
        try:
            col_idx = data_lst[0].index(col_name)
        except ValueError:     # bad name
            continue
        col_lst = []
        for i in range(1,len(data_lst)):
            col_lst.append(data_lst[i][col_idx])
        selected_cols_lst.append(col_lst)
    return selected_cols_lst


# testing:
def test_parsing():
    data_lst = parse_line("2003-04,19,CLE,NBA,SG,79,79", [0,2,3,4], ",")
    testif(data_lst == ["2003-04",19,"CLE","NBA","SG",79,79], "simple test for parsing")



def main():
    """The main part of the program."""    
    try:
        # part a)
        print("Part a):")
        test_parsing()

        string_pos_lst = [0,2,3,4]
        bb_file = open("lb-james.csv", "r")
        bb_lst = get_csv_data(bb_file, string_pos_lst, ",")
        print(bb_lst[:4])

        # part b)
        print("\n\nPart b:")
        yearly_lst = bb_lst[:-4]    # skip last 4 rows (with summary info)
        headings_lst = ["Age", "Season", "Pos", "3P", "PTS"]
        selected_cols = get_columns(yearly_lst, headings_lst)
        for i in range(len(selected_cols)):
            print(headings_lst[i], selected_cols[i])


        # part c):
        import pylab     # you can import anywhere; does not have to be at the top.
        print("\n\nPart c:")

        # we add a second figure to what was required.
        
        headings_pct_lst = ["Season", "3P%", "2P%", "FT%"]
        selected_pct_cols = get_columns(yearly_lst, headings_pct_lst)
        for i in range(len(selected_pct_cols)):
            print(headings_pct_lst[i], selected_pct_cols[i])

        n = len(selected_pct_cols[1])
        pylab.ylabel("%")
        linemodes = ["gx-", "rx-", "bx-"]

        #pylab.figure(1)
        pylab.subplot(1,2,1)        
        for i in range(len(headings_pct_lst) - 1):
            pylab.plot(selected_pct_cols[i+1], linemodes[i], label=headings_pct_lst[1+i])

        pylab.xticks(range(n), selected_pct_cols[0], rotation=45)
        pylab.legend(loc='upper right', shadow=True)
        pylab.xlabel("Season")
        pylab.title("Lebron James' shooting %")
        pylab.axis([0, n, 0, 1])
        pylab.grid()

        # second figure:

        headings_pts_lst = ["Season", "MP", "PTS"]
        selected_pts_cols = get_columns(yearly_lst, headings_pts_lst)
        for i in range(len(selected_pts_cols)):
            print(headings_pts_lst[i], selected_pts_cols[i])

        n = len(selected_pts_cols[1])
        linemodes = ["gx-", "rx-"]

        #pylab.figure(2)
        pylab.subplot(1,2,2)        
        for i in range(len(headings_pts_lst) - 1):
            pylab.plot(selected_pts_cols[i+1], linemodes[i], label=headings_pts_lst[1+i])

        pylab.xticks(range(n), selected_pts_cols[0], rotation=45)
        pylab.legend(loc='upper right', shadow=True)
        pylab.xlabel("Season")
        pylab.title("Minutes and point totals per game")
        pylab.axis([0, n, 0, 48])
        pylab.grid()
                
        pylab.show()
        
    finally:
        bb_file.close()  # close file regardless of exceptions
        


if __name__ == "__main__":
    main()
    
