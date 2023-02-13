# import requests
# import base64
# rest_countries='https://restcountries.com/v3.1/all'
# res=requests.get(rest_countries)
# api_data=res.json()
# countries=[]
# for data in api_data:
#     country_name=data.get('name').get('offical')
#     countries.append(country_name)
# user='mannan'
# password='123456'
# credential=f'{user}:{password}'
# token=base64.b64decode(credential.encode())
# headers={'Authorization':f'Basic {token.decode("utf-8")}'}
# wp_endspoint='https//localhost/wp/wp-josn/wp/v2/categories'
# for country in countries:
#     data={'name':country}
#     r=requests.post(wp_endspoint,data=data,headers=headers,verify=False)
# import requests
# import base64
# rest_countries='https://restcountries.com/v3.1/all'
# res=requests.get(rest_countries)
# country_data=res.json()
# countries=[]
# for data in country_data:
#     country_name=data.get('name').get('officical')
#     countries.append(country_name)

# wp_endspoint='https//localhost/wp/wp-josn/wp/v2/categories'
# user='hasmir'
# password='12345666'
# # credential=f'{user}:{password}'
# token=base64.b64decode(f'{user}:{password}'.encode())
# headers={'Authorization':f'Basic {token.decode("utf-8")}'}
# for country in countries:
#     data={
#         'name':country,
#     }
# r=requests.post(wp_endspoint,data=data,headers=headers,verify=False)
# import requests
# rest_countries='https://restcountries.com/v3.1/all'
# r=requests.get(rest_countries)
# api_data=r.json()
# Counries=[]
# for data in api_data:
#     Country_name=data.get('name').get('official')
#     Counries.append(Country_name)
# user='Rubel'
# Password='123455'
# credential=f'{user}:{Password}'
# token=base64.b64decode(credential.encode())
# headers={'Authorization'f'Basic {token.decode("utf-8")}'}
# data={
#     'name':country,
# }
# api_endspoint='https//localhost/wp/wp-josn/wp/v2/categories'
# res=requests.post(api_endspoint,data=data,headers=headers,verify=False)
# import requests
# res_counries='https://restcountries.com/v3.1/all'
# r=requests.get(res_counries)
# api_data=r.json()
# Countries=[]
# for data in api_data:
#     country_name=data.get('name').get('official')
#     Countries.append(country_name)

# wp_endspoint='https//localhost/wp/wp-josn/wp/v2/categories'
# user='hasmie'
# password='1233555'
# credential=f'{user}:{password}'
# token=base64.b64decode(credential.encode())
# headers={'Authorization':f'Basic {token.decode("utf-8")}'}
# for counrty in Countries:
#     data={'name':counrty}
#     res=requests.post(wp_endspoint,data=data,headers=headers,verify=False)
import requests
import base64
rest_countries='https://restcountries.com/v3.1/all'
res=requests.get(rest_countries)
api_data=res.json()
countries=[]
for data in api_data:
    country_name=data.get('name').get('official')
    counries.append(country_name)

api_endspoint='https//localhost/wp/wp-josn/wp/v2/categories'
user='mannan'
password='12345566'
credential=f'{user}:{password}'
token=base64.b64decode(credential.encode())
headers={'Authorization':f'Basic {token.decode("utf-8")}'}
for country in countries:
    data={'name':country}
    r=requests.post(api_endspoint,data=data,headers=headers,verify=False)
