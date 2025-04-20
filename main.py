import os
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import chromadb
from chromadb.config import Settings
from typing import List
import uvicorn

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Initialize templates
templates = Jinja2Templates(directory="templates")

# Set cache directory from environment variable
cache_dir = os.getenv("CHROMA_CACHE_DIR", "/app/data/cache")

# Initialize ChromaDB
chroma_client = chromadb.Client(
    Settings(persist_directory="db", anonymized_telemetry=False)
)

# Create or get the collection
collection = chroma_client.get_or_create_collection(name="form_data")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/submit")
async def submit_form(text: str = Form(...)):
    # Add the text to ChromaDB
    collection.add(documents=[text], ids=[f"doc_{len(collection.get()['ids'])}"])
    return {"message": "Data stored successfully!"}


@app.get("/search")
async def search_data(query: str):
    # Search in ChromaDB
    results = collection.query(query_texts=[query], n_results=5)
    return {"results": results}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)