from flask import render_template,request,redirect, url_for
from . import main
from ..models import Sources
from ..request import get_sources,get_articles


# Views
@main.route('/')
def index():

    general_news = get_sources('general')
    business_news = get_sources('business')
    entertainment_news = get_sources('entertainment')
    sports_news = get_sources('sports')
    technology_news = get_sources('technology')
    science_news = get_sources('science')
    health_news = get_sources('health')

    title = 'Welcome to Newsbytes'
    
    return render_template('index.html', title=title, General=general_news, Business=business_news,
                           Entertainment=entertainment_news, Sports=sports_news, Technology=technology_news,
                           Science=science_news, Health=health_news)


@main.route('/articles/<source_id>&<int:per_page>')
def articles(source_id,per_page):
    '''
    Function that returns articles based on their sources
    '''

    news_source = get_articles(source_id,per_page)
    title = f'{source_id} | All Articles'
    return render_template('articles.html',title=title,name=source_id,news=news_source)
