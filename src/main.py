from fastapi import FastAPI
from src.client import get_post, create_post, get_comments

app = FastAPI()

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/posts/{post_id}")
async def read_post(post_id: int):
    return await get_post(post_id)

@app.post("/posts")
async def write_post(title: str, body: str, user_id: int):
    return await create_post(title, body, user_id)

@app.get("/posts/{post_id}/comments")
async def read_comments(post_id: int):
    return await get_comments(post_id)
