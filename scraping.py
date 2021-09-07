import wikipedia as w

def getSearchTerm():
    term = input("What would you like to search for?\n")
    temp = w.suggest(term)
    if temp != None:
        term = temp

    return term

def main():
    searchTerm = getSearchTerm()


main()
