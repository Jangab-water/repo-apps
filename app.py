from fastapi import FastAPI
from json import dumps
import uvicorn

core=FastAPI()

@core.get('/')
@core.get('/api')
async def home():
    return dumps({"hello":"world"})

if __name__=="__main__":
    uvicorn.run(core, host="0.0.0.0", port=8000)