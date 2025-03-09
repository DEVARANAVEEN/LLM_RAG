import wikipediaapi
import wikipedia

# Define a user agent
USER_AGENT = "NaveenBot/1.0 (Contact: naveenaibot@yopmail.com)"

# Initialize Wikipedia API with user agent
wiki_wiki = wikipediaapi.Wikipedia(
    language='en',
    user_agent=USER_AGENT
)

def fetch_wikipedia_summary(search_query):
    """Search Wikipedia and return a summary of the best-matching topic."""
    search_results = wikipedia.search(search_query)
    
    if search_results:
        best_match = search_results[0]
        page = wiki_wiki.page(best_match)
        if page.exists():
            return page.summary
    return None
