import wikipedia

def search_wikipedia(word):
    searchArr = wikipedia.search(word)

    wiki_results = []
    
    try:
        for result in searchArr:
            #print("result: " + result)
            wiki_results.append(wikipedia.page(result, preload=False))
    except Exception as e:
        #print("disambiguation error on " + result)
        #print(e)
        try:
            for item in e.options:
                #print("disambiguation error on " + item)
                wiki_results.append(wikipedia.page(item, preload=False))
        except Exception as i:
            try:
                for item in i.options:
                    #print("disambiguation error on " + item)
                    wiki_results.append(wikipedia.page(item, preload=False))
            except:
                pass

    return wiki_results