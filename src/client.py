import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def get_post(post_id):
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    response.raise_for_status()
    return response.json()

def create_post(title, body, user_id):
    response = requests.post(f"{BASE_URL}/posts", json={
        "title": title, "body": body, "userId": user_id
    })
    response.raise_for_status()
    return response.json()

def get_comments(post_id):
    response = requests.get(f"{BASE_URL}/posts/{post_id}/comments")
    response.raise_for_status()
    return response.json()
