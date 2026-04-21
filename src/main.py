from fastapi import FastAPI
from src.client import get_post, create_post, get_comments

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/posts/{post_id}")
def read_post(post_id: int):
    return get_post(post_id)

@app.post("/posts")
def write_post(title: str, body: str, user_id: int):
    return create_post(title, body, user_id)

@app.get("/posts/{post_id}/comments")
def read_comments(post_id: int):
    return get_comments(post_id)
