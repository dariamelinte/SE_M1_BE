import json
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_login(client):
    data = {
        "email": "test@example.com",
        "password": "testpassword"
    }
    response = client.post('/login', data=json.dumps(data), content_type='application/json')
    
    assert response.status_code == 200
    assert response.content_type == 'application/json'
    
    response_data = json.loads(response.data)
    
    assert response_data.get('success') == True
    assert response_data.get('message') == 'Completely logged in.'
    assert response_data.get('credential').get('email') == 'test@example.com'
    assert response_data.get('jwt') is not None