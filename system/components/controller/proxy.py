# Python Standard Libraries
import string
import random
# External Libraries
from proxyscrape import create_collector, get_collector, add_resource_type, get_proxyscrape_resource
# Components
#
# Random string
def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
# Make Collector
def make_collector():
    random_string = get_random_string(10)
    http_collector = create_collector(random_string, 'https')
    resource_name = get_proxyscrape_resource(proxytype='http', timeout=5000, ssl='yes', anonymity='all', country='us') 
    add_resource_type(random_string, resource_name)
    return http_collector
# Setup Proxies
def setup_new_proxies(http_collector):   
    proxy_http = http_collector.get_proxy()
    proxy_https = http_collector.get_proxy({'type':'https'})
    proxies={
        'http': f'http://{proxy_http.host}:{proxy_http.port}',
        'https' : f'https://{proxy_https.host}:{proxy_https.port}'
    }
    return proxies
