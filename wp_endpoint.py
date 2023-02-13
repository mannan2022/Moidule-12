import httpx
from pprint import pprint
base_url='https://sourceofproduct.com/wp-json/wp/v2'
post_api=f'{base_url}/posts'

response=httpx.get(post_api)

pprint(response.json())
