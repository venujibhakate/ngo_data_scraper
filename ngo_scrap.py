from bs4 import BeautifulSoup
import requests
import pprint
import json

url = "https://www.giveindia.org/certified-indian-ngos"
def scrap_top_list():
    list_name = []
    list_cause = []
    list_state = []
    ngo_details_list = []
    res = requests.get(url)
    soup = BeautifulSoup(res.text,"html.parser")
    main_div = soup.find_all('div',class_='col')
    table = soup.find("table",class_="jsx-697282504 certified-ngo-table") 
    tr = table.find_all("tr",class_="jsx-697282504")
    td = table.find_all("td",class_="jsx-697282504 nonprofit-name-desktop")
    for j in tr:
        td = j.find_all("td",class_="jsx-697282504")
        for name in td[:1]:
            name_text = name.text
            list_name.append(name_text)
        for cause in td[1:2]:
            cause_text = cause.text
            list_cause.append(cause_text)
        for state in td[2:3]:
            state_text = state.text
            list_state.append(state_text)
        # pprint.pprint(list_state)
        ngo_details_dic = {}
        ngo_details_dic["name"] = list_name
        ngo_details_dic["cause"] = list_cause
        ngo_details_dic["state"] = list_state

        ngo_details_list.append(ngo_details_dic)
    return ngo_details_list
scrap_ngo_data = scrap_top_list()

