from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import chromadb
from chromadb.config import Settings
import os
from typing import List

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Initialize templates
templates = Jinja2Templates(directory="templates")

# Initialize ChromaDB
chroma_client = chromadb.Client(Settings(
    persist_directory="db",
    anonymized_telemetry=False
))

# Create or get the collection
collection = chroma_client.get_or_create_collection(name="form_data")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/submit")
async def submit_form(text: str = Form(...)):
    # Add the text to ChromaDB
    collection.add(
        documents=[text],
        ids=[f"doc_{len(collection.get()['ids'])}"]
    )
    return {"message": "Data stored successfully!"}

@app.get("/search")
async def search_data(query: str):
    # Search in ChromaDB
    results = collection.query(
        query_texts=[query],
        n_results=5
    )
    return {"results": results} 