import wikipedia

def search_wikipedia(word):
    searchArr = wikipedia.search(word)

    wiki_results = []
    
    try:
        for result in searchArr:
            #print("result: " + result)
            wiki_results.append(wikipedia.page(result))
    except Exception as e:
        #print("disambiguation error on " + result)
        #print(e)
        try:
            for item in e.options:
                #print("disambiguation error on " + item)
                wiki_results.append(wikipedia.page(item))
        except Exception as i:
            try:
                for item in i.options:
                    #print("disambiguation error on " + item)
                    wiki_results.append(wikipedia.page(item))
            except:
                pass
    
    if not wiki_results:
        wiki_results[0] = "Sorry. We are unable to retrieve Wikipedia data at this time. Please try again later"

    return wiki_results