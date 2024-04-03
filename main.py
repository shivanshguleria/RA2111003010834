from fastapi import FastAPI

import requests,json
from q1 import numbers
from q2 import products
app = FastAPI()


def get_auth_token():
    const_body = {
    "companyName":"SRMIST Chennai",
    "clientID": "7ca3a774-ac1e-4472-b0eb-b819db49a342",
    "clientSecret": "lsDRcOxShrZuPLby",
    "ownerName": "Shivansh Guleria",
    "rollNo": "RA2111003010834",
    "ownerEmail": "ss2768@srmist.edu.in"
}

    res = requests.post("http://20.244.56.144/test/auth", data=json.dumps(const_body))
    return res.access_token

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

app.include_router(numbers.router)
app.include_router(products.router)