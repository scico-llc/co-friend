FROM python:slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app/ .

CMD ["python", "main.py"]