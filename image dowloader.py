# import requests
# from pprint import pprint
# api_key='33237522-2b80cf72e6b46d28d98bf3175'
# api_url=f'https://pixabay.com/api/?key={api_key}&q=yellow+flowers&image_type=photo'
# r=requests.get(api_url)
# api_data=r.json().get('hits')

# for data in api_data:
#     images=data.get('webformatURL')
#     file=open('images.txt','a+')
#     file.writelines(images+ '\n')
#     file.close()
# import requests
# file=open('image.txt','r+')
# url_list=file.readlines()
# file.close()
# # print(url_list)
# new_url_list=[]
# for url in url_list:
#     images=url.get()
    