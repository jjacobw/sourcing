#searches for linkedins for utah founders of new-ish companies



#general founders

import time
from googlesearch import search

def find_new_startups(location="Utah", num_results=20):
    query = f"linkedin startup founder in {location} today founded this year "
    print(f"Searching Google for: {query}\n")
    
    try:
        results = search(query, num_results=num_results)
        startup_links = list(results)
        
        if not startup_links:
            print("No results found.")
        else:
            print("Found the following startup links:")
            for idx, link in enumerate(startup_links, 1):
                print(f"{idx}. {link}")
                
    except Exception as e:
        print(f"Error while searching: {e}")

if __name__ == "__main__":
    find_new_startups()