from typing import Union
from fastapi import FastAPI, Header, Cookie, HTTPException # type: ignore
from pydantic import BaseModel # type: ignore
import uvicorn # type: ignore
from fastapi.responses import RedirectResponse, JSONResponse # type: ignore

app = FastAPI(__name__ = '__weare__')

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool,None]=None

class Item2(BaseModel):
    name: str
    description: Union[str,None] = None
    price: float
    tax: Union[float,None] = None

@app.get('/')
def read_root():
    return {"Hello":"Worlddddd"}

@app.get('/items/{item_id}')
def read_item(item_id: int, q: Union[str,None] = None):
    return {'item_id': item_id, 'q':q}

@app.put('/items/{item_id}')
def update_item(item_id: int, item: Item):
    return {'item_name': item.name, 'item_id': item_id}

@app.get('/try_items/')
def try_items(skip:int = 0, limit:int = 20):
    return {'skip':skip, 'limit':limit}

@app.post('/items2/')
def create_item2(item: Item2):
    return item

@app.get('/header/')
def get_header(user_agent: str = Header(None), session_token: str = Cookie(None)):
    return {'User-Agent': user_agent, 'Session-Token': session_token}

@app.get('/redirect')
def redirect():
    return RedirectResponse(url = '/header/')

@app.get('/testerror/{item_id}')
def test_error(item_id: int):
    if item_id==42:
        raise HTTPException(status_code = 404, detail = 'nonono')
    return {'item_id':item_id}

@app.get('/set_response_header/{item_id}')
def set_response_header(item_id: int):
    content = {'item_id': item_id}                            # what return as result
    headers = {'X-Custom-Header': 'this is the return value'}      # what return in response header
    return JSONResponse(content = content, headers = headers)

def main():
    print("Hello from fastapi-example!")
    uvicorn.run('main:app', port=5000, log_level = 'info')


if __name__ == "__main__":
    main()
