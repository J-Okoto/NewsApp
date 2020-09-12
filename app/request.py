from .models import Sources
import urllib.request, json



api_key = None
sources_url = None
articles_url = None

def configure_request(app):
    global api_key, base_url, articles_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['SOURCES_BASE_URL']
    articles_url = app.config['EVERYTHING_SOURCE_BASE_URL']