FROM python:2.7

COPY . /app
RUN cd /app && pip install -r requirements.txt

CMD ["python", "/app/server.py"]
