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

def searchTitles(term):
    return w.search(term, SEARCH_TERM_LIMIT)

def searchPages(titles):
    pages = []
    for i in titles:
        pages.append(w.page(i))
    return pages

def main():
    searchTerm = getSearchTerm()
    print(searchTerm)

    pageTitles = searchTitles(searchTerm)
    print(pageTitles)

    pages = searchPages(pageTitles)
    print(pages)
    

main()
