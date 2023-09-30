from main import app  

# TESTING ROUTE CONNECTION /
def test_index_route():
    client = app.test_client()  
    response = client.get('/')  
    assert response.status_code == 200 

# TESTING ROUTE CONNECTION /COW
def test_cow_route():
    client = app.test_client()
    response = client.get('/cow')
    assert response.status_code == 200