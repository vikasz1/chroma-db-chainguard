# Use Chainguard Python image
FROM cgr.dev/chainguard/python:latest-dev

# Set working directory
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Create the db directory for ChromaDB persistence
RUN mkdir -p db

# Expose the port the app runs on
EXPOSE 8000

# Set the entrypoint to python
ENTRYPOINT ["python", "-m", "uvicorn"]

# Default command arguments
CMD ["main:app", "--host", "0.0.0.0", "--port", "8000"] 