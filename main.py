import requests as rq
import json

# URLS
MAIN_URL = "http://195.82.179.158:5000/"
LOGIN_URL = "http://195.82.179.158:5000/api/user/login"
DATASET_URL = "http://195.82.179.158:5000/api/dataset/"
COCO_EXPORT_URL = "http://195.82.179.158:5000/api/dataset/{}/coco"

# PATH TO DIRECTORY IN WITCH YOU WANT TO SAVE EXPORT
DIR_PATH = r"C:\Users\User\Desktop\tutaj"
USERNAME = ""
PASSWORD = ""
def extract():
    # login
    url = "http://195.82.179.158:5000/api/user/login"
    # HERE TYPE IN YOUR PASSWORD AND LOGIN
    payload = {"password": PASSWORD,"username": USERNAME}
    headers = {'Content-Type': "application/json"}
    response = rq.request("POST", url, json=payload, headers=headers)
    # auth cookies
    cookies = response.cookies
    # get datasets info
    datasets = rq.get(DATASET_URL, cookies=cookies)
    # extract IDs from datasets to list

    ids_lst = list()

    for row in datasets.json():
        ids_lst.append(row['id'])
    # export /dataset/{dataset_id}/coco
    print("DOWNLOADING EXPORTS...")
    counterDwnl = 1
    export_lst = list()
    for val in ids_lst:
        response = rq.get(COCO_EXPORT_URL.format(val),cookies=cookies)
        export_lst.append(response.text)
        print("DOWNLOADING FILE:",counterDwnl)
        counterDwnl = counterDwnl + 1

    # SAVE JSON FILES
    counter = 1
    for export in export_lst:
        path = DIR_PATH+'\export{}.json'.format(counter)
        with open(path, 'w') as f:
            json.dump(export, f)
        counter = counter + 1
        print("EXPORTING FILE", counter + "PATH:", path)

if __name__ == '__main__':
    extract()