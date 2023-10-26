from fastapi import FastAPI, Body

app = FastAPI()

database = {}

# Create a GET ReST API
@app.get("/api")
def first_api():
  return {"msg":"hello_world"}

# Create a GET ReST API with path parameters
@app.get("/books/{path_param}")
def first_apiV2(path_param: str):
  return {"msg": path_param}

# Create a GET ReST API with query parameters
@app.get("/books/")
def first_apiV3(title: str):
  return {"msg": title}

# Create a GET ReST API with path parameters AND query parameters
@app.get("/books/{title}")
def first_apiV4(title: str, publish_year: int):
  return {"title": title, "publish_year": int}

# Create a POST ReST API
@app.post("/books/create_book")
def first_apiV5(new_book=Body()):
  print(new_book)
  return {"msg": new_book}

# Create a PUT ReST API
@app.put("/book/isbn")
def update_book(isbn: str, title: str):
  if isbn in database:
    database[isbn] = title
    return {"msg":"title of the book updated"}
  else:
    database[isbn] = title
    return {"msg":"The book has been added"}

# Create a DELETE ReST API

@app.delete("/book/isbn")
def delete_book(isbn: str):
  if isbn in database:
    del database[isbn]
    return {"msg":"book has been deleted"}
  else:
    return {"msg":f"There is no book matched with {isbn}"}


