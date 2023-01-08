print("To exist this program type 'quit'")
while True:
    isUniqueStr = input('Type the string \n')
    if(isUniqueStr == "quit"):
        print("bye...")
        break
    # A set is implemented as a Hash Table in Python
    charSet = set(isUniqueStr)
    if (len(charSet) == len(isUniqueStr)):
        print(isUniqueStr + " is unique")
    else:
        print(isUniqueStr + " is not unique")
    print("\n")
