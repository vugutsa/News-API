from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_news,get_articles,search_articles
# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    # Getting news sources
    independent = get_news('independent')
    techcrunch = get_news('techcrunch')
    focus = get_news('focus')
    title = 'Home - Welcome to News website online'
    search_news = request.args.get('news_query')
    if search_news:
        return redirect(url_for('.search', category_name = search_news))
    else:
        return render_template('index.html', title = title, independent = independent, focus = focus, techcrunch = techcrunch)
@main.route('/articles/')
def articles():
    '''
    View article page function that returns the news articles details page and its data
    '''
    news = get_articles(articles)
    title = f'{news.title}'
    articles = Articles.get_articles(news.url)
    return render_template('articles.html',title = title,news = news,articles = articles)
@main.route('/categories/<category_name>')
def category(category_name):
    '''
    method that returns the categories page
    '''
    category = get_category(category_name)
    title = f'{category_name}'
    return render_template('categories.html', title = title, category = category)
@main.route('/categories/entertainment')
def entertainment():
    '''
    method that returns the categories page
    '''
    sports = get_category('entertainment')
    title = 'ENTERTAINMENT'
    return render_template('categories.html', title = title, entertainment = entertainment)
@main.route('/categories/sport')
def sports():
    '''
    method that returns the categories page
    '''
    sports = get_category('sports')
    title = 'SPORTS'
    return render_template('categories.html', title = title, sports = sports)

@main.route('/categories/business')
def business():
    '''
    method that returns the categories page
    '''
    business = get_category('business')
    title = 'BUSINESS'
    return render_template('categories.html', title = title, business = business)
@main.route('/search/<category_name>')
def search(category_name):
    '''
    View function to display the search results
    '''
    category_list = category.split(" category_name")
    category_format = "+".join(news_list
    searched_news = search_category(category_format)
    title = f'search results for {category_name}'
    return render_template('search.html',news = searched_news)





