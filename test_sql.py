import requests

# Base URL of the Flask application
BASE_URL = 'http://127.0.0.1:8080'

# Route to create a new post
CREATE_POST_URL = f'{BASE_URL}/create_post'

# JSON data for the new post
post_data = {
    'title': 'New Post',
    'content': 'This is the content of the new post.'
}

# Send a POST request to create a new post
response = requests.post(CREATE_POST_URL, json=post_data)

# Print the response
print('Response:')
print(response.json())