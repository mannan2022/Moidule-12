# import requests
# from pprint import pprint
# api_key='33237522-2b80cf72e6b46d28d98bf3175'
# api_url=f'https://pixabay.com/api/?key={api_key}&q=yellow+flowers&image_type=photo'
# res=requests.get(api_url)
# api_data=res.json().get('hits')
# for url in api_data:
#     image_url=url.get('webformatURL')
#     file=open('images.txt','a+')
#     file.writelines(image_url+'\n')
#     file.close()
# import requests
# from pprint import pprint
# api_ke='33237522-2b80cf72e6b46d28d98bf3175'
# url=f'https://pixabay.com/api/?key={api_ke}&q=yellow+flowers&image_type=photo'
# res=requests.get(url)
# api=res.json().get('hits')
# for url in api:
#     image=api.get('webformateurl')
#     file=open('images','a+')
#     file.writelines(image+'\n')
#     file.close()
# from requests import get
# file=open('images.txt','r+')
# url_list=file.readlines()
# file.close()
# new_url=[]
# for url in url_list:
#     image_link=url.strip('\n')
#     new_url.append(image_link)
# singel_url=new_url[0]
# r=get(singel_url)
# file=open('images.jpg','wb')
# file.write(r.content)
# file.close()
# from requests import get
# file=open('images.txt','r+')
# url_list=file.readlines()
# file.close()
# new_url=[]
# for url in url_list:
#     image_url=url.strip('\n')
#     new_url.append(image_url)
# singel_url=new_url[1]
# res=get(singel_url)
# file=open('images.jpg','wb')
# file.write(res.content)
# file.close()
# from requests import get
# file=open('images.txt','r+')
# url_list=file.readlines()
# file.close()
# new_url=[]
# for url in url_list:
#     image_url=url.strip('\n')
#     new_url.append(image_url)
# singel_url=new_url[3]
# resp=get(singel_url)
# file=open('pixaba.jpg','wb')
# file.write(resp.content)
# file.close()
# from requests import get
# file=open('images.txt','r')
# url_list=file.readlines()
# file.close()
# i=0
# for url in url_list:
#     url=url.strip('\n')
#     r=get(url)
#     file=open(f'images/{i}.jpg','wb')
#     file.write(r.content)
#     file.close()
#     i+=1
from requests import get
file=open('images.txt','r')
url=file.readlines()
file.close()
i=0
for link in url:
    url=link.strip('\n')
    res=get(url)
    file=open(f'hasmir/{i}.jpg','wb')
    file.write(res.content)
    file.close
    i+=1
    import requests
    file=open('images.txt','r')
    text=file.readlines()
    file.close()
    i=0
    for url in text:
        link=url.strip('\n')
        r=requests.get(link)
        file=open(f'rubel/{i}.jpg','wb')
        file.write(r.content())
        file.close()