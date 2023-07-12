
def test_home(client):
    response = client.get("/get-name")
    print(response)
    assert b'SE4I project' in response.data
    
