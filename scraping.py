import wikipedia as w

SEARCH_TERM_LIMIT = 5

def getSearchTerm():
    term = input("What would you like to search for? ")
    temp = w.suggest(term)
    if temp != None:
        validation = input("Did you mean " + temp + "? (y/n) ")
        if validation == "y":
            term = temp

    return term

def search(term):
    return w.search(term, SEARCH_TERM_LIMIT)

def main():
    searchTerm = getSearchTerm()
    print(searchTerm)

    pages = search(searchTerm)
    print(pages)


main()
