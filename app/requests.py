import urllib.request,json
from .models import News
# Getting api key
api_key = None
# Getting the movie base url
base_url = None
def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    
def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        news_results = None
        if get_news_response['articles']:
            news_articles_list = get_news_response['articles']
            news_results = process_results(news_articles_list)
    # print("Result",news_results)
    return news_results
def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects
    Args:
        news_list: A list of dictionaries that contain news details
    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        title = news_item.get('title')
        image = news_item.get('urlToImage')
        description = news_item.get('description')
        date = news_item.get('publishedAt')
        if title:
            news_object = News(title,id,image,description,date)
            news_results.append(news_object)
    return news_results
def get_articles(articles):
    get_news_details_url = articlesbase_url.format(articles,api_key)
    with urllib.request.urlopen(get_news_details_url) as url:
        news_details_data = url.read()
        news_details_response = json.loads(news_details_data)
        news_object = None
        if news_details_response:
            title = news_item.get('title')
            image = news_item.get('urlToImage')
            description = news_item.get('description')
            date = news_item.get('publishedAt')
            articles = news_item.get('url')
            id = news_item.get('id')
            news_object = News(title,id,image,description,date,articles)
    return news_object
def get_category(category_name):
    get_category_url = base_url.format(category_name,api_key)
    with urllib.request.urlopen(get_category_url) as url:
        get_category_data = url.read()
        get_category_response = json.loads(get_category_data)
        get_category_results = None
        if get_category_response['articles']:
            get_category_list = get_category_response['articles']
            get_category_results = process_results(get_category_list)
    return get_category_results


def search_articles(articles_name):
    search_articles_url = 'http://newsapi.org/v2/everything/search?q={}&apiKey=&query={}'.format(api_key,movie_name)
    with urllib.request.urlopen(search_articles_url) as url:
        search_articles_data = url.read()
        search_articles_response = json.loads(search_aricles_data)

        search_articles_results = None

        if search_articles_response['results']:
            search_articles_list = search_aricles_response['results']
            search_articles_results = process_results(search_articles_list)


    return search_articles_results















