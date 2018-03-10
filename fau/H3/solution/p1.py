# Python Programming.
# Homework 3, problem 1
# Instructor: Dr. Ionut Cardei
# Do not distribute.

# Tuple Input

from testif import testif

def parse_tok(tok, type_obj):
    """Parses a string tok to a type. We need that to handle bools: "True" and "False" and "0".
    We cannot rely on bool(...) constructor.
    Returns parsed element. It throws exceptions if parsing fails.
    Parameters 
    tok: the string to parse
    type_obj: a type object (e.g. int)
    """
    val = None
    if type_obj == bool:
        # get rid of extra chars around tok:
        tok = tok.strip()
        if tok.lower() == "false" or tok == "0":
            val = False
        else:
            val = True
    else:
        val = type_obj(tok)    # this may throw TypeError or ValueError

    # for debugging: print("tok={},type={},val={}".format(tok,type_obj,val))        
    return val


def parse_string(types, string, sep):
    """Parses a string with tokens of types given in param types and separated by chars in sep.
    """
    try:
        token_lst = string.split(sep)
        data_lst = []
        if len(types) != len(token_lst):
            # number of tokens entered != number of types to parse
            print("Error: number of tokens entered ({}) != number of types to parse ({}).".format(len(token_lst), len(types)))
            return ()
        
        for i in range(len(types)):
            # we could do this to cut extra whitespace chars next to separators: s = token_lst[i].strip()
            s = token_lst[i]
            elem = parse_tok(s, types[i])
            data_lst.append(elem)    
                    
    except:
        print("Parsing error for string '{}'".format(string))
        return ()
    
    return tuple(data_lst)


def parse_string_lc(types, string, sep):
    """Parses a string with tokens of types given in param types and separated by chars in sep.
    Uses a list comprehension.
    """
    try:
        token_lst = string.split(sep)
        data_lst = []
        if len(types) != len(token_lst):
            # number of tokens entered != number of types to parse
            print("Error: number of tokens entered ({}) != number of types to parse ({}).".format(len(token_lst), len(types)))
            return ()

        data_lst = [parse_tok(token_lst[i], types[i]) for i in range(len(token_lst))]
        
    except:
        print("Parsing error for string '{}'".format(string))
        return ()
    
    return tuple(data_lst)



def input_tuple(prompt, types, sep=","):
    """Reads a line from the terminal with an input prompt and parses the tokens according to
    parameter sep and a list of types.
    Returns a tuple with the parsed elements or () if parsing failed.
    
    Parameters:
    prompt: the input prompt
    types: indexable collection of type objects; e.g. [int, str, bool]
    sep: token separator
    """
    line = input(prompt)
    return parse_string(types, line, sep)
    

def input_tuple_lc(prompt, types, sep=","):
    """Like input_tuple, but with a list comprehension.
    """
    line = input(prompt)
    return parse_string_lc(types, line, sep)
    


def read_tuple(file, types, sep=","):
    """Reads a line from an open file (param file) and parses the tokens according to
    parameter sep and a list of types.
    Returns a tuple with the parsed elements or () if parsing failed.
    
    Parameters:
    file: the open file
    types: indexable collection of type objects; e.g. [int, str, bool]
    sep: token separator
    """
    line = file.readline()
    return parse_string_lc(types, line, sep)
    


## ------------------------------------------------------

def runtest_stdin():
    tup1 = parse_string([str,str,float,int,bool], "Spongebob,Squarepants,23.5,1,False", ',')
    testif(tup1 == ("Spongebob","Squarepants",23.5,1,False), "test string")

    tup2 = parse_string_lc([str,str,float,int,bool], "Spongebob,Squarepants,23.5,1,False", ',')
    testif(tup2 == ("Spongebob","Squarepants",23.5,1,False), "test string (with list comprehension)")

    # test failure case:
    tup3 = parse_string_lc([str,str,float,int,bool], "Spongebob,Squarepants,NOT A FLOAT,1,False", ',')
    testif(tup3 == (), "test failure case (expect float() to fail (with list comprehension)")
    
    tup4 = parse_string([str,str,float,int,bool], "Spongebob,Squarepants,NOT A FLOAT,1,False", ',')
    testif(tup4 == (), "test failure case (expect float() to fail")
    
        
    tup1 = input_tuple("Enter first name, last name, age (float), ID (int), fulltime (bool):", [str,str,float,int,bool])
    print(tup1)
    
    tup2 = input_tuple_lc("Enter first name, last name, age (float), ID (int), fulltime (bool):", [str,str,float,int,bool])
    print(tup2)

    
def runtest_file():
    f = open("cars.csv", "r")
    tup = read_tuple(f, (str, str, float, int, bool), ',')
    testif(tup == ("Lada","Niva",19.5,int(1987),False), "read_file")

    tup = read_tuple(f, (str, str, float, int, bool), ',')
    testif(tup == ("Porsche","911 Turbo S",17.5,1989,True), "read_file, second call")

    f.close()

## ----------------------------------------------------------

# main program:    
if __name__ == "__main__":
    runtest_stdin()
    runtest_file()
    
