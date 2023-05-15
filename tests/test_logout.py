import jwt
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_logout(client):
    token = jwt.encode({'sub': '1234567890', 'iat': 1516239022}, 'your_secret_key_here', algorithm='HS256')
    headers = {'Authorization': token}

    response = client.post('/logout', headers=headers)

    assert response.status_code == 200
    assert response.json['success'] == True
    assert response.json['message'] == 'Logged out successfully.'