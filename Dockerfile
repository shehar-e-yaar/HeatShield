FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN python run_pipeline.py
EXPOSE 8080
CMD ["python", "-m", "http.server", "8080", "--directory", "site"]
