from typing import Union
from fastapi import FastAPI # type: ignore
from pydantic import BaseModel # type: ignore
import uvicorn # type: ignore

app = FastAPI(__name__ = '__weare__')

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool,None]=None

@app.get('/')
def read_root():
    return {"Hello":"Worlddddd"}

@app.get('/items/{item_id}')
def read_item(item_id: int, q: Union[str,None] = None):
    return {'item_id': item_id, 'q':q}

@app.put('/items/{item_id}')
def update_item(item_id: int, item: Item):
    return {'item_name': item.name, 'item_id': item_id}

def main():
    print("Hello from fastapi-example!")
    uvicorn.run('main:app', port=5000, log_level = 'info')


if __name__ == "__main__":
    main()
