from fastapi.testclient import TestClient
from ..src.main import app

client = TestClient(app)
database = {}
def test_first_api():
  response = client.get("/api")
  assert response.status_code == 200
  assert response.json() == {"msg": "hello_world"}


def test_first_apiV2():
    test_param = "sample"
    response = client.get(f"/books/{test_param}")
    assert response.status_code == 200
    assert response.json() == {"msg": test_param}

def test_first_apiV3():
    test_title = "test_title"
    response = client.get(f"/books/?title={test_title}")
    assert response.status_code == 200
    assert response.json() == {"msg": test_title}

def test_first_apiV4():
    test_title = "test_book"
    test_year = 2023
    response = client.get(f"/books/{test_title}?publish_year={test_year}")
    assert response.status_code == 200
    assert response.json() == {'msg': 'test_book'}

def test_first_apiV5():
    test_book = "sample_book"
    response = client.post("/books/create_book", json="sample_book")
    assert response.status_code == 200
    assert response.json() == {"msg": test_book}

def test_update_book():
    test_isbn = "123456"
    test_title = "sample_title"
    response = client.put(f"/book/isbn?isbn={test_isbn}&title={test_title}")
    assert response.status_code == 200
    if test_isbn in database:
        expected_msg = "title of the book updated"
    else:
        expected_msg = "The book has been added"
    assert response.json() == {"msg": expected_msg}

def test_delete_book():
    test_isbn = "123456"
    response = client.delete(f"/book/isbn?isbn={test_isbn}")
    assert response.status_code == 200
    expected_msg = ""
    if test_isbn in database:
        expected_msg = "book has been deleted"
    else:
        expected_msg = f"There is no book matched with {test_isbn}"
    assert response.json() == {"msg": 'book has been deleted'}