from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def read_item(name: str = "Default Value "):
    return {"item_id": "Hello world ",
            "name":name

            }

