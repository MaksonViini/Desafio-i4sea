FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .

COPY runtime.sh .

COPY parse_request.sh .

RUN pip install -r requirements.txt

COPY ./src .

EXPOSE 8080

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8080"]