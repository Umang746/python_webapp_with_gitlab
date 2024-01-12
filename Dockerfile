FROM python:latest

WORKDIR  /app

ADD . /app

RUN pip install Flask

CMD ["python" , "app.py"]
