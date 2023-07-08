FROM pytorch/pytorch:latest

WORKDIR /api

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r /api/requirements.txt

COPY ./api/ .
EXPOSE 8080

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]
# CMD ["gunicorn", "main:app", "-w", "1", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:8080"]






