# ChromaDB Form Application

A simple FastAPI application that uses ChromaDB to store and search form data.

## Features

- Submit text data through a web form
- Store data in ChromaDB
- Search through stored data
- Simple and clean UI
- Containerized with Chainguard Python image

## Setup

### Local Development

1. Create a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
uvicorn main:app --reload
```

### Docker

1. Build the Docker image:

```bash
docker build -t chromadb-form .
```

2. Run the container:

```bash
docker run -p 8000:8000 -v $(pwd)/db:/app/db chromadb-form
```

4. Open your browser and navigate to:

```
http://localhost:8000
```

## Usage

1. Enter text in the form and click "Submit" to store it in ChromaDB
2. Use the search form to find similar text entries
3. The data is persisted in the `db` directory

## API Endpoints

- `GET /`: Main page with the form
- `POST /submit`: Submit new text data
- `GET /search`: Search through stored data

## Notes

- When running with Docker, the `db` directory is mounted as a volume to persist data between container restarts
- The application uses Chainguard's minimal Python image for enhanced security
