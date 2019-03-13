import argparse
import json
import os
import re
from DoD_scraper import get_latest_allnews
from DoD_scraper import get_latest_alltrans
from DoD_scraper import get_latest_allrelease
from DoD_scraper import get_latest_advisor
from DoD_scraper import get_latest_speech
from DoD_scraper import strf_to_datetime
from DoD_scraper import news_dateformat


def save(json_obj, directory):
    url = json_obj['url']
    category = [p for p in url.split('/') if p][-4]
    title = [p for p in url.split('/') if p][-1]
    dt = json_obj['time']
    name = '{}-{}-{}_{}_{}'.format(dt.year, dt.month, dt.day, category, re.sub("[\/:*?\<>|]","", title[:50]))
    filepath = '{}/{}.json'.format(directory, name)
    with open(filepath, 'w', encoding='utf-8') as fp:
        json.dump(json_obj, fp, indent=2, ensure_ascii=False, sort_keys=True, default=str)

def scraping(begin_date, max_num, sleep, directory, verbose):

    n_exceptions = 0
#transcript
    for i, json_obj in enumerate(get_latest_alltrans(begin_date, max_num, sleep)):
        try:
            save(json_obj, directory)
        except Exception as e:
            n_exceptions += 1
            print(e)
            continue

        if verbose:
            title = json_obj['title']
            time = json_obj['time']
            print('[{} / {}] ({}) {}'.format(i+1, max_num, time, title))

    if n_exceptions > 0:
        print('Exist %d transcripts exceptions ' % n_exceptions)
# Releases
    for i, json_obj in enumerate(get_latest_allrelease(begin_date, max_num, sleep)):
        try:
            save(json_obj, directory)
        except Exception as e:
            n_exceptions += 1
            print(e)
            continue

        if verbose:
            title = json_obj['title']
            time = json_obj['time']
            print('[{} / {}] ({}) {}'.format(i+1, max_num, time, title))

    if n_exceptions > 0:
        print('Exist %d newsrealease exceptions' % n_exceptions)
# advisor
    for i, json_obj in enumerate(get_latest_advisor(begin_date, max_num, sleep)):
        try:
            save(json_obj, directory)
        except Exception as e:
            n_exceptions += 1
            print(e)
            continue

        if verbose:
            title = json_obj['title']
            time = json_obj['time']
            print('[{} / {}] ({}) {}'.format(i+1, max_num, time, title))

    if n_exceptions > 0:
        print('Exist %d advisor exceptions' % n_exceptions)

# speech
    for i, json_obj in enumerate(get_latest_speech(begin_date, max_num, sleep)):
        try:
            save(json_obj, directory)
        except Exception as e:
            n_exceptions += 1
            print(e)
            continue

        if verbose:
            title = json_obj['title']
            time = json_obj['time']
            print('[{} / {}] ({}) {}'.format(i+1, max_num, time, title))

    if n_exceptions > 0:
        print('Exist %d speech exceptions' % n_exceptions)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--begin_date', type=str, default='2018-07-01', help='datetime YYYY-mm-dd')
    parser.add_argument('--directory', type=str, default='./output/', help='Output directory')
    parser.add_argument('--max_num', type=int, default=1000, help='Maximum number of news to be scraped')
    parser.add_argument('--sleep', type=float, default=1.0, help='Sleep time for each news')
    parser.add_argument('--verbose', dest='VERBOSE', action='store_true')

    args = parser.parse_args()
    begin_date = args.begin_date
    directory = args.directory
    max_num = args.max_num
    sleep = args.sleep
    VERBOSE = args.VERBOSE

    # check output directory
    if not os.path.exists(directory):
        os.makedirs(directory)

    scraping(begin_date, max_num, sleep, directory, VERBOSE)

if __name__ == '__main__':
    main()
