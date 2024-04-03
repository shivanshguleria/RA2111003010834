from fastapi import APIRouter, Request, status
from fastapi import HTTPException
import requests
import json, time

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
@router.get("/categories/{categoryname}/products/{productid}")
def get_all(req: Request, numberid: str):
    # print(get_auth_token())

    auth_token = get_auth_token()
    auth_token_s = "Bearer " + auth_token

    try:

    except:   #timeout after 500ms
        raise HTTPException(status_code=408, detail="Query Timeout")