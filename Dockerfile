FROM python:3.9-slim-buster

WORKDIR /app

ENV FLASK_APP src/main.py

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

# CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]