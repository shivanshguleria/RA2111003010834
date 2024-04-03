from fastapi import APIRouter, Request, status
from fastapi import HTTPException
import requests
import json, time
# from ..main import get_auth_token
router = APIRouter()
times = 0.5
url = "http://20.244.56.144/test/"
token_time  = ""
token = ""
def get_auth_token():  
    global token_time, token
    if token != "" and int(token_time) > int(time.time()):  #Check if token is valid
        return token
    else: 
        const_body = {
    "companyName": "SRMIST Chennai",
    "clientID": "39e3a877-d891-4080-8909-210c086f7fa4",
    "clientSecret": "NnBfzwGxpFtPcTHv",
    "ownerName": "Shivansh Guleria",
    "ownerEmail": "ss2768@srmist.edu.in",
    "rollNo": "RA2111003010834"
}
        res = requests.post("http://20.244.56.144/test/auth", data=json.dumps(const_body), timeout=times)
        print(res.json())
        token = res.json()["access_token"]
        token_time =   res.json()["expires_in"] 
        return token
saved_numbers = []
prev = ""
@router.get("/numbers/{numberid}")
def processNumber(req: Request, numberid: str):
    # print(get_auth_token())
    global saved_numbers
    prev = numberid
    if prev != numberid:
        print("sdfsfd")
        saved_numbers = []
    auth_token = get_auth_token()
    auth_token_s = "Bearer " + auth_token
    print(url + numberid)
    try:
        res = requests.get(url + numberid, headers={"Authorization": auth_token_s}, timeout=times)
        window = 10
        print(res.text)
        nums_list = res.json()['numbers']
        print(nums_list)
        avg_sum = sum(nums_list)
        print(saved_numbers , "adfasf")
        
        if saved_numbers and len(saved_numbers) != 0 and saved_numbers[len(saved_numbers)-1 ] == nums_list[0]:  #check if stored list is in continuation
            new_list = saved_numbers.extend(nums_list)
            avg_sum = sum(new_list[:window])                     #slice array according to window size
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
    except:   #timeout after 500ms
        raise HTTPException(status_code=408, detail="Query Timeout")