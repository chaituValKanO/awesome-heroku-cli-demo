from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def get_items(item_id: int, count: int = 1):
    return {"App_Version: 1.1.0 - fetch": f"Fetched {count} of {item_id}"}