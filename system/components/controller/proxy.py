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
    result_str = ''.join(random.choice(letters) for _ in range(length))
    return result_str
# Make Collector
def make_collector():
    random_string = get_random_string(10)
    http_collector = create_collector(random_string, 'https')
    print("https")
    #resource_name = get_proxyscrape_resource(proxytype='http', timeout=5000, ssl='yes', anonymity='all', country='us') 
    #add_resource_type("resource", resource_name)
    print("end https")
    return http_collector
# Setup Proxies
def setup_new_proxies(http_collector):   
    print("entered setup")
    proxy_http = http_collector.get_proxy()
    print("here")
    proxy_https = http_collector.get_proxy({'type':'https'})
    print("here")
    proxies={
        'http': f'http://{proxy_http.host}:{proxy_http.port}',
        'https' : f'https://{proxy_https.host}:{proxy_https.port}'
    }
    return proxies
