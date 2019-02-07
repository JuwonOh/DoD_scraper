import time
from .parser import parse_page
from .utils import get_soup
from .utils import news_dateformat
from .utils import user_dateformat
from .utils import strf_to_datetime

url_news = 'https://dod.defense.gov/News/Archive/?Page={}'

def get_latest_allnews(begin_date, max_num=10, sleep=1.0):
    """
    Arguments
    ---------
    begin_page : int
        Default is 1
    end_page : int
        Default is 3
    verbose : Boolean
        If True, print current status

    Returns
    -------
    links_all : list of str
        List of urls
    """
    # prepare parameters
    d_begin = strf_to_datetime(begin_date, user_dateformat)
    end_page = 72
    n_news = 0
    outdate = False

    for page in range(0, end_page+1):

        # check number of scraped news
        if n_news >= max_num or outdate:
            break

        # get urls
        links_all = []
        url = url_news.format(page)
        soup = get_soup(url)
        sub_links = soup.find_all('p', class_= 'title')
        links = [i.find('a')['href'] for i in sub_links]
        links_all += links

        # scrap
        for url in links_all:

            news_json = parse_page(url)

            # check date
            d_news = strf_to_datetime(news_json['time'], news_dateformat)
            if d_begin > d_news:
                outdate = True
                print('Stop scrapping. {} / {} news was scrapped'.format(n_news, max_num))
                print('The oldest news has been created after {}'.format(begin_date))
                break

            # yield
            yield news_json

             # check number of scraped news
            n_news += 1
            if n_news >= max_num:
                break
            time.sleep(sleep)

def get_news_urls(begin_page=1, end_page=3, verbose=True):
    """
    Arguments
    ---------
    begin_page : int
        Default is 1
    end_page : int
        Default is 3
    verbose : Boolean
        If True, print current status

    Returns
    -------
    links_all : list of str
        List of urls
    """

    links_all = []
    for page in range(0, end_page+1):
        url = url_news.format(page)
        soup = get_soup(url)
        sub_links = soup.find_all('p', class_= 'title')
        links = [i.find('a')['href'] for i in sub_links]
        links_all += links
        if verbose:
            print('get briefing statement urls {} / {}'.format(page, end_page))

    return links_all

def get_last_newpage_num():
    """
    Returns
    -------
    page : int
        Last page number.
        eg: 503 in 'https://dod.defense.gov/News/Archive/?Page=824'
    """
    last_page = []

    soup = get_soup('https://dod.defense.gov/News/Archive/?Page=2')
    last_page_list = soup.find('div', class_ = 'center-pager').find_all('li')
    last_page = [i.find('a')['href'] for i in last_page_list][-1:]
    return last_page

url_transcript = 'http://dod.defense.gov/News/Transcripts/?Page={}/'

def get_latest_alltrans(begin_date, max_num=10, sleep=1.0):
    """
    Arguments
    ---------
    begin_page : int
        Default is 1
    end_page : int
        Default is 3
    verbose : Boolean
        If True, print current status

    Returns
    -------
    links_all : list of str
        List of urls
    """
    # prepare parameters
    d_begin = strf_to_datetime(begin_date, user_dateformat)
    end_page = 72
    n_news = 0
    outdate = False

    for page in range(0, end_page+1):

        # check number of scraped news
        if n_news >= max_num or outdate:
            break

        # get urls
        links_all = []
        url = url_transcript.format(page)
        soup = get_soup(url)
        sub_links = soup.find_all('div', class_= 'title')
        links = [i.find('a')['href'] for i in sub_links]
        links_all += links

        # scrap
        for url in links_all:

            news_json = parse_page(url)

            # check date
            d_news = strf_to_datetime(news_json['time'], news_dateformat)
            if d_begin > d_news:
                outdate = True
                print('Stop scrapping. {} / {} news was scrapped'.format(n_news, max_num))
                print('The oldest news has been created after {}'.format(begin_date))
                break

            # yield
            yield news_json

             # check number of scraped news
            n_news += 1
            if n_news >= max_num:
                break
            time.sleep(sleep)


def get_trans_urls(begin_page=1, end_page=3, verbose=True):
    """
    Arguments
    ---------
    begin_page : int
        Default is 1
    end_page : int
        Default is 3
    verbose : Boolean
        If True, print current status

    Returns
    -------
    links_all : list of str
        List of urls
    """

    links_all = []
    for page in range(begin_page, end_page+1):
        url = url_transcript.format(page)
        soup = get_soup(url)
        sub_links = soup.find_all('div', class_= 'title')
        links = [i.find('a')['href'] for i in sub_links]
        links_all += links
        if verbose:
            print('get briefing statement urls {} / {}'.format(page, end_page))

    return links_all

def get_lastts_page_num():
    """
    Returns
    -------
    page : int
        Last page number.
        eg: 503 in 'http://dod.defense.gov/News/Transcripts/?Page='
    """
    last_page = []

    soup = get_soup('http://dod.defense.gov/News/Transcripts/?Page=')
    last_page_list = soup.find('div', class_ = 'center-pager').find_all('li')
    last_page = [i.find('a')['href'] for i in last_page_list][-1:]
    return last_page

url_release = 'https://dod.defense.gov/News/Releases/?Page={}'

def get_latest_allrelease(begin_date, max_num=10, sleep=1.0):
    """
    Arguments
    ---------
    begin_page : int
        Default is 1
    end_page : int
        Default is 3
    verbose : Boolean
        If True, print current status

    Returns
    -------
    links_all : list of str
        List of urls
    """

    # prepare parameters
    d_begin = strf_to_datetime(begin_date, user_dateformat)
    end_page = 72
    n_news = 0
    outdate = False

    for page in range(0, end_page+1):

        # check number of scraped news
        if n_news >= max_num or outdate:
            break

        # get urls
        links_all = []
        url = url_release.format(page)
        soup = get_soup(url)
        sub_links = soup.find_all('div', class_= 'title')
        links = [i.find('a')['href'] for i in sub_links]
        links_all += links

        # scrap
        for url in links_all:

            news_json = parse_page(url)

            # check date
            d_news = strf_to_datetime(news_json['time'], news_dateformat)
            if d_begin > d_news:
                outdate = True
                print('Stop scrapping. {} / {} news was scrapped'.format(n_news, max_num))
                print('The oldest news has been created after {}'.format(begin_date))
                break

            # yield
            yield news_json

             # check number of scraped news
            n_news += 1
            if n_news >= max_num:
                break
            time.sleep(sleep)


def get_release_urls(begin_page=1, end_page=3, verbose=True):
    """
    Arguments
    ---------
    begin_page : int
        Default is 1
    end_page : int
        Default is 3
    verbose : Boolean
        If True, print current status

    Returns
    -------
    links_all : list of str
        List of urls
    """

    links_all = []
    for page in range(begin_page, end_page+1):
        url = url_release.format(page)
        soup = get_soup(url)
        sub_links = soup.find_all('div', class_= 'title')
        links = [i.find('a')['href'] for i in sub_links]
        links_all += links
        if verbose:
            print('get briefing statement urls {} / {}'.format(page, end_page))

    return links_all

def get_lastre_num():
    """
    Returns
    -------
    page : int
        Last page number.
        eg: 503 in 'https://dod.defense.gov/News/Releases/?Page=2'
'
    """
    last_page = []

    soup = get_soup("https://dod.defense.gov/News/Releases/?Page=2")
    last_page_list = soup.find('div', class_ = 'center-pager').find_all('li')
    last_page = [i.find('a')['href'] for i in last_page_list][-1:]
    return last_page

url_advisor = 'https://dod.defense.gov/News/Advisories/?Page={}'

def get_latest_advisor(begin_date, max_num=10, sleep=1.0):
    """
    Arguments
    ---------
    begin_page : int
        Default is 1
    end_page : int
        Default is 3
    verbose : Boolean
        If True, print current status

    Returns
    -------
    links_all : list of str
        List of urls
    """
    # prepare parameters
    d_begin = strf_to_datetime(begin_date, user_dateformat)
    end_page = 72
    n_news = 0
    outdate = False

    for page in range(0, end_page+1):

        # check number of scraped news
        if n_news >= max_num or outdate:
            break

        # get urls
        links_all = []
        url = url_advisor.format(page)
        soup = get_soup(url)
        sub_links = soup.find_all('div', class_= 'title')
        links = [i.find('a')['href'] for i in sub_links]
        links_all += links

        # scrap
        for url in links_all:

            news_json = parse_page(url)

            # check date
            d_news = strf_to_datetime(news_json['time'], news_dateformat)
            if d_begin > d_news:
                outdate = True
                print('Stop scrapping. {} / {} news was scrapped'.format(n_news, max_num))
                print('The oldest news has been created after {}'.format(begin_date))
                break

            # yield
            yield news_json

             # check number of scraped news
            n_news += 1
            if n_news >= max_num:
                break
            time.sleep(sleep)

def get_advisor_urls(begin_page=1, end_page=3, verbose=True):
    """
    Arguments
    ---------
    begin_page : int
        Default is 1
    end_page : int
        Default is 3
    verbose : Boolean
        If True, print current status

    Returns
    -------
    links_all : list of str
        List of urls
    """

    links_all = []
    for page in range(begin_page, end_page+1):
        url = url_advisor.format(page)
        soup = get_soup(url)
        sub_links = soup.find_all('div', class_= 'title')
        links = [i.find('a')['href'] for i in sub_links]
        links_all += links
        if verbose:
            print('get briefing statement urls {} / {}'.format(page, end_page))

    return links_all


def get_lastad_page_num():
    """
    Returns
    -------
    page : int
        Last page number.
        eg: 503 in 'https://dod.defense.gov/News/Advisories/?Page=2'
'
    """
    last_page = []

    soup = get_soup("https://dod.defense.gov/News/Advisories/?Page=2")
    last_page_list = soup.find('div', class_ = 'center-pager').find_all('li')
    last_page = [i.find('a')['href'] for i in last_page_list][-1:]
    return last_page

url_speeches = 'https://dod.defense.gov/News/Speeches/?Page={}'

def get_latest_speech(begin_date, max_num=10, sleep=1.0):
    """
    Arguments
    ---------
    begin_page : int
        Default is 1
    end_page : int
        Default is 3
    verbose : Boolean
        If True, print current status

    Returns
    -------
    links_all : list of str
        List of urls
    """
    # prepare parameters
    d_begin = strf_to_datetime(begin_date, user_dateformat)
    end_page = 72
    n_news = 0
    outdate = False

    for page in range(0, end_page+1):

        # check number of scraped news
        if n_news >= max_num or outdate:
            break

        # get urls
        links_all = []
        url = url_speeches.format(page)
        soup = get_soup(url)
        sub_links = soup.find_all('p', class_= 'title')
        links = [i.find('a')['href'] for i in sub_links]
        links_all += links

        # scrap
        for url in links_all:

            news_json = parse_page(url)

            # check date
            d_news = strf_to_datetime(news_json['time'], news_dateformat)
            if d_begin > d_news:
                outdate = True
                print('Stop scrapping. {} / {} news was scrapped'.format(n_news, max_num))
                print('The oldest news has been created after {}'.format(begin_date))
                break

            # yield
            yield news_json

             # check number of scraped news
            n_news += 1
            if n_news >= max_num:
                break
            time.sleep(sleep)

def get_speech_urls(begin_page=1, end_page=3, verbose=True):
    """
    Arguments
    ---------
    begin_page : int
        Default is 1
    end_page : int
        Default is 3
    verbose : Boolean
        If True, print current status

    Returns
    -------
    links_all : list of str
        List of urls
    """

    links_all = []
    for page in range(begin_page, end_page+1):
        url = url_speeches.format(page)
        soup = get_soup(url)
        sub_links = soup.find_all('p', class_= 'title')
        links = [i.find('a')['href'] for i in sub_links]
        links_all += links
        if verbose:
            print('get briefing statement urls {} / {}'.format(page, end_page))

    return links_all


def get_lastsp_page_num():
    """
    Returns
    -------
    page : int
        Last page number.
        eg: 503 in 'https://dod.defense.gov/News/Speeches/?Page=2'
'
    """
    last_page = []

    soup = get_soup("https://dod.defense.gov/News/Speeches/?Page=2")
    last_page_list = soup.find('div', class_ = 'center-pager').find_all('li')
    last_page = [i.find('a')['href'] for i in last_page_list][-1:]
    return last_page
