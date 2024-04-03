from fastapi import APIRouter, Request
import requests
import json, time
# from ..main import get_auth_token
router = APIRouter()

url = "http://20.244.56.144/test/"
token_time  = ""
token = ""
def get_auth_token():
    global token_time, token
    if token_time < int(time.time()):
        return token
    else: 
        const_body = {
        "companyName": "SRMIST Chennai",
        "clientID": "7ca3a774-ac1e-4472-b0eb-b819db49a342",
        "clientSecret": "lsDRcOxShrZuPLby",
        "ownerName": "Shivansh Guleria",
        "ownerEmail": "ss2768@srmist.edu.in",
        "rollNo": "RA2111003010834"
    }
        res = requests.post("http://20.244.56.144/test/auth", data=json.dumps(const_body))
        print(res.json())
        token = res.json()["access_token"]
        token_time =   res.json()["access_token"] 
        return token
saved_numbers = []
prev = ""
@router.get("/numbers/{numberid}")
def processNumber(req: Request, numberid: str):
    # print(get_auth_token())
    global saved_numbers
    prev = numberid
    if prev != numberid:
        saved_numbers = []
    auth_token = get_auth_token()
    auth_token_s = "Bearer " + auth_token
    print(url + numberid)
    res = requests.get(url + numberid, headers={"Authorization": auth_token_s})
    window = 10
    print(res.text)
    nums_list = res.json()['numbers']
    print(nums_list)
    avg_sum = sum(nums_list)

    if saved_numbers:
        if saved_numbers[len(saved_numbers)-1 ] == nums_list[0]:
            new_list = saved_numbers.extend(nums_list)
            avg_sum = sum(new_list[:window])
            return {
                        "number": nums_list,
                        "windowPrevState": saved_numbers,
                        "wiondowCurrState": nums_list,
                        avg: avg
                    }
    else:
        avg = avg_sum / len(nums_list)
        saved_numbers.extend(nums_list)
        return {
            "number": nums_list,
            "windowPrevState": saved_numbers,
            "wiondowCurrState": nums_list,
            "avg": avg
        }