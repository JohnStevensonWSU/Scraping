import wikipedia as w

SEARCH_TERM_LIMIT = 5
OUTPUT_FILE = "output.txt"

class Page:
  
    def __init__(self, title, summary, image, url):
        self.title = title
        self.summary = summary
        self.image = image
        self.url = url

def getSearchTerm():
    term = input("What would you like to search for? ")
    temp = w.suggest(term)
    if temp != None:
        validation = input("Did you mean " + temp + "? (y/n) ")
        if validation == "y":
            term = temp
    return term

def findPages(term):
    titles = returnTitles(term)
    pages = returnPages(titles)
    return pages

def returnTitles(term):
    return w.search(term, SEARCH_TERM_LIMIT)

def returnPages(titles):
    pages = []
    for i in titles:
        pages.append(w.page(i))
    return pages

def scanPages(pages):
    Pages = []
    for i in pages:
        Pages.append(Page(i.title, i.summary, i.images[0], i.url))
    return Pages

def storePages(Pages):
    write = open(OUTPUT_FILE, 'w')
    write.write("ID,Title,Summary,Image,URL\n")
    j = 0
    for i in Pages:
        write.write(str(j) + ",\"" + i.title + "\",\"" + i.summary + "\"," + i.image + ",\"" + i.url + "\"\n")
        j = j + 1
    write.close()

def main():
    searchTerm = getSearchTerm()
    print(searchTerm)

    pages = findPages(searchTerm)
    print(pages)

    Pages = scanPages(pages)
    print(Pages)

    storePages(Pages)

main()
