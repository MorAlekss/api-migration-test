import httpx

BASE_URL = "https://jsonplaceholder.typicode.com"

async def get_post(post_id):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/posts/{post_id}")
        response.raise_for_status()
        return response.json()

async def create_post(title, body, user_id):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{BASE_URL}/posts", json={
            "title": title, "body": body, "userId": user_id
        })
        response.raise_for_status()
        return response.json()

async def get_comments(post_id):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/posts/{post_id}/comments")
        response.raise_for_status()
        return response.json()
