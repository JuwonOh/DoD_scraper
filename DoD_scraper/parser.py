import re
from .utils import get_soup
from .utils import now

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
        title = soup.find('div', class_= 'article-body').find('h1').text
        time = soup.select('time')[0].text
        phrases = soup.find('div', class_= 'article-body')
        content = ''.join(re.split('[0-9]{1,2}, [0-9]{4}', re.sub('\n|\r|\xa0', '', phrases.text))[1:])

        json_object = {
            'title' : title,
            'time' : time,
            'content' : content,
            'url' : url,
            'scrap_time' : now()
        }
        return json_object
    except Exception as e:
        print(e)
        print('Parsing error from {}'.format(url))
        return None
