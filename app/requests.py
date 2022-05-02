import urllib.request, json
from .models import Articles 

# Getting api key
api_key = None
# Getting the movie base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_ARTICLES_URL']


def get_articles ():
        '''
    A function that gets a response for the articles body
    '''
        get_articles_url = 'https://newsapi.org/v2/everything?q=tesla&from=2022-04-01&sortBy=publishedAt&apiKey={}'
        with urllib.request.urlopen(get_articles_url) as url:
            get_articles_data = url.read ()
            get_articles_response = json.loads(get_articles_data)
            articles_results = None

            if get_articles_response['articles']:
                articles_results_list = get_articles_response['articles']
                articles_results = process_articles (articles_results_list)
        
        return articles_results


def process_articles (articles_list):
    '''
    Fuction that processes what the articles results are and transforms them to objects 
    '''
    articles_results = []
    for articles_items in articles_list:
        source = articles_items.get('source')
        author = articles_items.get('author')
        title = articles_items.get('title')
        url = articles_items.get('url')
        urlToImage = articles_items.get('urlToImage')
        publishedAt  = articles_items.get('publishedAt')
        content = articles_items.get('content')

        if source:
            articles_objects = Articles(author, title, url, urlToImage, publishedAt, content)

            articles_results.append(articles_objects)

    
    return articles_results

