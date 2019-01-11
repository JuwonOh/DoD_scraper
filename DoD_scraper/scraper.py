import re
import time
from .utils import get_soup

def get_latest_allnews(last_date, sleep=1.0):
    """
    Artuments
    ---------
    last_date : Date
    sleep : float
        Sleep time. Default 1.0 sec
    """

    raise NotImplemented

patterns_transcript = [
    re.compile('https://dod.defense.gov/News/Transcripts/[\w]+')]
url_transcript = 'http://dod.defense.gov/News/Transcripts/?Page={}/'

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


patterns_speeches = [re.compile('https://dod.defense.gov/News/Speeches/[\w]+')]
url_speeches = 'https://dod.defense.gov/News/Speeches/?Page={}'

def get_speeches_urls(begin_page=1, end_page=3, verbose=True):
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

def get_last_page_num():
    """
    Returns
    -------
    page : int
        Last page number.
        eg: 503 in 'https://dod.defense.gov/News/Transcripts/?Page=62'
    """
    raise NotImplemented
