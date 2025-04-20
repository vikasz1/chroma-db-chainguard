
FROM cgr.dev/chainguard/python:latest-dev as dev

WORKDIR /app

RUN python -m venv venv
ENV PATH="/app/venv/bin":$PATH
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Set ENVs
ENV HF_HOME=/app/.cache
ENV XDG_CACHE_HOME=/app/.cache
RUN mkdir -p /app/.cache
RUN sed -i 's|DOWNLOAD_PATH = .*|DOWNLOAD_PATH = Path("/app/data") / "chroma" / "onnx_models" / MODEL_NAME|' venv/lib/python3.*/site-packages/chromadb/utils/embedding_functions.py
RUN echo "Vikas maury"

# FROM cgr.dev/chainguard/python:latest

WORKDIR /app

COPY . .
# COPY --from=dev /app/venv /app/venv
ENV PATH="/app/venv/bin:$PATH"

EXPOSE 8000

ENTRYPOINT ["python", "main.py"]