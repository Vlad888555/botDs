from bs4 import BeautifulSoup
import requests

#summoner = str(input("Ник/Регион "))
#values = summoner.split('/')
#if len(values) == 2:
#    summoner_hrel = values[0].strip().lower()
#    ru = values[1].strip().lower()
#else:
#    print("Некорректный формат ввода. Пожалуйста, используйте разделитель '/' для ввода значений.")
#
#pegion = ["br", "eune", "euw", "jp", "kr", "lan", "las", "na", "oce", "ru", "tr", "ph", "sg", "th", "tw", "vn"]
#
#if ru .upper() in pegion:


#url = f"https://www.leagueofgraphs.com/ru/summoner/{ru}/{summoner_hrel}"
#print(url)

#создание копи html

cookies = {
    'usprivacy': '1---',
    '_lc2_fpi': '13533c70212a--01haq3q97r8qgkwv5ajb23trf9',
    '_ga': 'GA1.1.1783720130.1695140259',
    '_gcl_au': '1.1.2119751212.1695140259',
    '_cc_id': '20d6976250529cc84dc4372c209af978',
    '_sharedid': 'bb41045b-34fb-4062-a31a-319eea85f474',
    '_pbjs_userid_consent_data': '3524755945110770',
    '_lr_env_src_ats': 'false',
    'panoramaId_expiry': '1699591030030',
    'panoramaId': 'c15eb0a134c01d82af26740979a7a9fb927ab7ea741f6d531241c73405403e2e',
    'ccuid': '2db838f4-28ee-45b6-9f45-72dfcd9e604b',
    '_li_dcdm_c': '.leagueofgraphs.com',
    'lolg_euconsent': 'nitro',
    '_lr_retry_request': 'true',
    'cto_bundle': 'grbp4F94d3JXSGZla0FwcWpXb2pxMFBWdGwlMkYlMkZKVkZIMWNrViUyRnBQOUxkaTdZVktIbWVNOEZjNCUyRnpzVHZwM3F6RVFOc0wzSHBSWHNrSyUyRkRmWHh4aExaRWJNQTJMNzJDSVdlMzAyY3lFQnEwVFZnU3VOTzAwTDZpYWNUYTU5cDZpUG43aGMlMkY3NWlBNWJPJTJCQnVOcHQyaUtyWnZkem5UeGFpN1UySzdsSzFNelZLcmg4VVhBM0cyNGMyUVZrUDFqemdNT2hBYml1ZUF6ZWxSejFVSDZUNDNyQ2NmMnclM0QlM0Q',
    'cto_bundle': 'grbp4F94d3JXSGZla0FwcWpXb2pxMFBWdGwlMkYlMkZKVkZIMWNrViUyRnBQOUxkaTdZVktIbWVNOEZjNCUyRnpzVHZwM3F6RVFOc0wzSHBSWHNrSyUyRkRmWHh4aExaRWJNQTJMNzJDSVdlMzAyY3lFQnEwVFZnU3VOTzAwTDZpYWNUYTU5cDZpUG43aGMlMkY3NWlBNWJPJTJCQnVOcHQyaUtyWnZkem5UeGFpN1UySzdsSzFNelZLcmg4VVhBM0cyNGMyUVZrUDFqemdNT2hBYml1ZUF6ZWxSejFVSDZUNDNyQ2NmMnclM0QlM0Q',
    'cto_bidid': '7aQUNF9hdDJzJTJGZG9LM0hneEZqVTJzJTJGc0RIZTJwclFZTiUyQmFiTUpMV0U3T1RlYmZYWE4xN2FSWXBsSnE4R1pTJTJGZmJrUXdvNUxFa051c2wzSERSTFphUDM0M1FyWDN1JTJGbXlYR2FERFdsWW14SlVLSWdUQlRHcjRSSENKTkxSZ0gwJTJCOEpzbA',
    'cto_bundle': '1GRdJl94d3JXSGZla0FwcWpXb2pxMFBWdGx5RFBnWDFJWjh6RmdWcDVFdml2MW8zbFBaVzJlZ1hyVkl1TnhNSXdwakRXR01nQmFZNXpKQVEyeldhV3h6dmNVTEtaa0hLQXJnblJNcDR4dzZFSGg1SUVjZjRNNXEzJTJCZW45UzhYckVaaWMyWTRsMHlhZExraEs1dkJRSVVNTkwlMkYlMkJzMmZFMFVOJTJCdFY5JTJGd0xtTjJRRyUyQjhUd05yd05VWGVsS28lMkIyaWglMkZ4OGslMkJiWFJWZjBQJTJGclAlMkJtRFpXdVJOMmRBdyUzRCUzRA',
    '__gads': 'ID=c83ff6638635bdac:T=1695140260:RT=1699540669:S=ALNI_MbtTeiGD6jjuL_E4RVb8DHer3c_Uw',
    '__gpi': 'UID=00000c78f259b71e:T=1695140260:RT=1699540669:S=ALNI_MZ57G2QNvtvjusxsY4KLmk7SNCfLg',
    '_ga_S6BZBBF9MM': 'GS1.1.1699540191.4.1.1699540845.60.0.0',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    # 'Cookie': 'usprivacy=1---; _lc2_fpi=13533c70212a--01haq3q97r8qgkwv5ajb23trf9; _ga=GA1.1.1783720130.1695140259; _gcl_au=1.1.2119751212.1695140259; _cc_id=20d6976250529cc84dc4372c209af978; _sharedid=bb41045b-34fb-4062-a31a-319eea85f474; _pbjs_userid_consent_data=3524755945110770; _lr_env_src_ats=false; panoramaId_expiry=1699591030030; panoramaId=c15eb0a134c01d82af26740979a7a9fb927ab7ea741f6d531241c73405403e2e; ccuid=2db838f4-28ee-45b6-9f45-72dfcd9e604b; _li_dcdm_c=.leagueofgraphs.com; lolg_euconsent=nitro; _lr_retry_request=true; cto_bundle=grbp4F94d3JXSGZla0FwcWpXb2pxMFBWdGwlMkYlMkZKVkZIMWNrViUyRnBQOUxkaTdZVktIbWVNOEZjNCUyRnpzVHZwM3F6RVFOc0wzSHBSWHNrSyUyRkRmWHh4aExaRWJNQTJMNzJDSVdlMzAyY3lFQnEwVFZnU3VOTzAwTDZpYWNUYTU5cDZpUG43aGMlMkY3NWlBNWJPJTJCQnVOcHQyaUtyWnZkem5UeGFpN1UySzdsSzFNelZLcmg4VVhBM0cyNGMyUVZrUDFqemdNT2hBYml1ZUF6ZWxSejFVSDZUNDNyQ2NmMnclM0QlM0Q; cto_bundle=grbp4F94d3JXSGZla0FwcWpXb2pxMFBWdGwlMkYlMkZKVkZIMWNrViUyRnBQOUxkaTdZVktIbWVNOEZjNCUyRnpzVHZwM3F6RVFOc0wzSHBSWHNrSyUyRkRmWHh4aExaRWJNQTJMNzJDSVdlMzAyY3lFQnEwVFZnU3VOTzAwTDZpYWNUYTU5cDZpUG43aGMlMkY3NWlBNWJPJTJCQnVOcHQyaUtyWnZkem5UeGFpN1UySzdsSzFNelZLcmg4VVhBM0cyNGMyUVZrUDFqemdNT2hBYml1ZUF6ZWxSejFVSDZUNDNyQ2NmMnclM0QlM0Q; cto_bidid=7aQUNF9hdDJzJTJGZG9LM0hneEZqVTJzJTJGc0RIZTJwclFZTiUyQmFiTUpMV0U3T1RlYmZYWE4xN2FSWXBsSnE4R1pTJTJGZmJrUXdvNUxFa051c2wzSERSTFphUDM0M1FyWDN1JTJGbXlYR2FERFdsWW14SlVLSWdUQlRHcjRSSENKTkxSZ0gwJTJCOEpzbA; cto_bundle=1GRdJl94d3JXSGZla0FwcWpXb2pxMFBWdGx5RFBnWDFJWjh6RmdWcDVFdml2MW8zbFBaVzJlZ1hyVkl1TnhNSXdwakRXR01nQmFZNXpKQVEyeldhV3h6dmNVTEtaa0hLQXJnblJNcDR4dzZFSGg1SUVjZjRNNXEzJTJCZW45UzhYckVaaWMyWTRsMHlhZExraEs1dkJRSVVNTkwlMkYlMkJzMmZFMFVOJTJCdFY5JTJGd0xtTjJRRyUyQjhUd05yd05VWGVsS28lMkIyaWglMkZ4OGslMkJiWFJWZjBQJTJGclAlMkJtRFpXdVJOMmRBdyUzRCUzRA; __gads=ID=c83ff6638635bdac:T=1695140260:RT=1699540669:S=ALNI_MbtTeiGD6jjuL_E4RVb8DHer3c_Uw; __gpi=UID=00000c78f259b71e:T=1695140260:RT=1699540669:S=ALNI_MZ57G2QNvtvjusxsY4KLmk7SNCfLg; _ga_S6BZBBF9MM=GS1.1.1699540191.4.1.1699540845.60.0.0',
    'Referer': 'https://www.leagueofgraphs.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://www.leagueofgraphs.com/api/is-recording/SVcwSXZ4dXdzOGIySjNEOXQ5VWJ6WVF0dGZvQ3FjOWVFUFo0Z05hODdvTT0=',
    cookies=cookies,
    headers=headers,
)


#req = requests.get(url, headers=headers)
#src = req.text
#print(src)
#with open("index.html", "w", encoding="utf-8") as file:
#    file.write(src)


with open("index.html", encoding="utf-8") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")

#уровень
bannerSubtitle = soup.find(class_="bannerSubtitle")
print(bannerSubtitle.text.strip())

#ранг
leagueTier = soup.find(class_="leagueTier")
print(f"Ранг: {leagueTier.text.strip()}")

#приметы
tagTitile_list = []
tagTitle_rank = soup.find_all(class_="tag requireTooltip brown")
for item in tagTitle_rank:
    tagTitile_list.append(item.text.strip())

tagTitile_green = soup.find_all(class_="tag requireTooltip green withLink")
for item in tagTitile_green:
    tagTitile_list.append(item.text.strip())

tagTitile_yellow = soup.find_all(class_="tag requireTooltip yellow withLink")
for item in tagTitile_yellow:
    tagTitile_list.append(item.text.strip())

tagTitile_red = soup.find_all(class_="tag requireTooltip red withLink")
for item in tagTitile_red:
    tagTitile_list.append(item.text.strip())
print(tagTitile_list)

#Всего игр и винрейт
pie_chart_small = soup.find(id="graphDD2")
print(f"Всего Сыграно: {pie_chart_small.text.strip()} за этот сплит")
pie_chart_small1 = soup.find(id="graphDD3")
print(f"Винрейт {pie_chart_small1.text.strip()} за все игры в этом сплите")

#Игры в одиночная
pie_chart_small2 = soup.find(id="graphDD4")
print(f"Сыграно {pie_chart_small2.text.strip()} в ранговой")
pie_chart_small3 = soup.find(id="graphDD5")
print(f"Винрайт {pie_chart_small3.text.strip()} в ранговой")








