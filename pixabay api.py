# import requests
# from pprint import pprint
# api_key='33237522-2b80cf72e6b46d28d98bf3175'
# api_url=f'https://pixabay.com/api/?key={api_key}&q=yellow+flowers&image_type=photo'

# resopnse=requests.get(api_url)
# if resopnse.status_code==200:
#    Image=(resopnse.json())
#    user_image_url=Image.get('hits')[0].get('userImageURL')
#    print(user_image_url)
# import requests
# url_list=[
#     'https://www.thespruce.com/attract-birds-with-food-386394',
#     'https://www.hindustantimes.com/shop-now/pet-care-and-supplies/top-10-bird-foods-buying-guide-101668144685130.html',
#     'https://www.gardenersworld.com/product-guides/nature/best-bird-food/',
# ]
# for url in url_list:
#     r=requests.get(url)
#     text=f'{url}---{r.status_code}'
#     file=open('url check.txt','a+')
#     file.writelines(text+'\n')
#     file.close()
#     file=open('url check.txt','r+')
#     url_list=file.readlines()
#     file.close()
#     print(url_list)
# text='This is test file'
# file=open('Buying Guide.txt','a+')
# file.writelines(text+'\n')
# file.close()
import requests
from pprint import pprint
api_key='33237522-2b80cf72e6b46d28d98bf3175'
api_url=f'https://pixabay.com/api/?key={api_key}&q=yellow+flowers&image_type=photo'
res=requests.get(api_url)
api_data=res.json().get('hits')
pprint(api_data)

# for data in api_data:
#     image_url=data.get('webformatURL')
#     file=open('image.txt','a+')
#     file.writelines(image_url+ '\n')
#     file.close()
# import requests
# from pprint import pprint
# api_key='33237522-2b80cf72e6b46d28d98bf3175'
# api_url=f'https://pixabay.com/api/?key={api_key}&q=yellow+flowers&image_type=photo'
# r=requests.get(api_url)
# api_data=r.json().get('hits')
# for data in api_data:
#     page_url=data.get('pageURL')
#     file=open('page.txt','a+')
#     file.writelines(page_url)
#     file.close()
    


    
