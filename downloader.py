# import requests
# file=open('images.txt','r+')
# url_list=file.readlines()
# file.close()
# new_url=[]
# for url in url_list:
#     image=url.strip('\n')
#     new_url.append(image)
# # print(new_url)
# single_url_list=new_url[0]
# # print(single_url_list)
# res=requests.get(single_url_list)
# file=open('image.jpg','wb')
# file.write(res.content)
# file.close()
import requests
file=open('images.txt','r+')
url_list=file.readlines()
file.close()
# print(url_list)
new=[]
for url in url_list:
    list_one=url.strip('\n')
    new.append(list_one)
# print(new)
singel=new[0]
# print(singel)
response=requests.get(singel)
file=open('pixabay.jpg','wb')
file.write(response.content)
file.close()
