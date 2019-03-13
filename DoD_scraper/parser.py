import re
from .utils import get_soup
from .utils import now
from dateutil.parser import parse
from .utils import strf_to_datetime
from .utils import news_dateformat

def parse_title(soup):
    title = soup.find('div', class_= 'article-body')
    return title.find('h1').text

def parse_content(soup):
    content = soup.find('div', class_= 'article-body')
    return content.get_text()

def parse_date(soup):
    time = soup.select('time')[0]
    return parse(time.text)

def parse_page(url):
    """
    Argument
    --------
    url : str
        Web page url

    Returns
    -------
    json_object : dict
        JSON format web page contents
        It consists with
            title : article title
            time : article written time
            content : text with line separator \\n
            url : web page url
            scrap_time : scrapped time
    """

    try:
        soup = get_soup(url)


        json_object = {
            'title' : parse_title(soup),
            'time' : parse_date(soup),
            'content' : parse_content(soup),
            'url' : url,
            'scrap_time' : now()
        }
        return json_object
    except Exception as e:
        print(e)
        print('Parsing error from {}'.format(url))
        return None
