import wikipedia

def search_wikipedia(word):
    searchArr = wikipedia.search(word)

    wiki_results = []
    try: 
        try:
            for result in searchArr:
                #print("result: " + result)
                wiki_results.append(wikipedia.page(result, preload=False))
        except wikipedia.DisambiguationError as e:
            #print("disambiguation error on " + result)
            #print(e.with_traceback)
            try:
                for item in e.options:
                    #print("disambiguation error on " + item)
                    wiki_results.append(wikipedia.page(item, preload=False))
            except wikipedia.DisambiguationError as i:
                try:
                    for item in i.options:
                        #print("disambiguation error on " + item)
                        wiki_results.append(wikipedia.page(item, preload=False))
                except wikipedia.DisambiguationError:
                    pass
    except: 
        print("Something went wrong getting wikipedia results")
        pass

    return wiki_results