from flask import render_template,request
from . import main
from ..models import Sources
from ..request import get_sources


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