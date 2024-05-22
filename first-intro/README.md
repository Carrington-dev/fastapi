# FastAPI Framework

If you declare similar urls it takes the one on top

for example

```
@app.get("/items/{item_id}")
def read_item(item_id: uuid.UUID, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/products/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
```

It will consider the one with UUID because it comes first