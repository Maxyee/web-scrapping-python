from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup


def simple_get(url):
    
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None
    
    except RequestException as e:
        log_error('Error during requrest to {0} : {1}'.format(url,str(e)))
        return None

def is_good_response(resp):

    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1 )


def log_error(e):

    print(e)


def get_names():

    url = 'http://www.fabpedigree.com/james/mathmen.htm'
    response = simple_get(url)

    if response is not None:
        html = BeautifulSoup(response,'html.parser')
        names = set()
        for li in html.select('li'):
            for name in li.text.split('\n'):
                if len(name) > 0:
                    names.add(name.strip())
        
        return list(names)

    raise Exception('Error retrieving contents at {}'.format(url))

    
raw_html = simple_get('http://www.fabpedigree.com/james/mathmen.htm')
html = BeautifulSoup(raw_html, 'html.parser')

for i, li in enumerate(html.select('li')):
    print(i,li.text)