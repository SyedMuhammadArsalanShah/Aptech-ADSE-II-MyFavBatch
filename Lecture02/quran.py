import requests



response = requests.get("https://api.alquran.cloud/v1/surah")


if response.status_code==200:
    meriSurahList=response.json()["data"]
    for i in meriSurahList:
        print(i["englishName"])