FROM pytorch/pytorch:latest

WORKDIR /api

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r /api/requirements.txt

COPY ./api/ .
EXPOSE 8080

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]
# CMD ["gunicorn", "-w", "3", "-k", "uvicorn.workers.UvicornWorker", "main:app", "--bind", "127.0.0.1:8080"]
