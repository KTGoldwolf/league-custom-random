FROM python:3.5

RUN pip install Flask
RUN pip install requests

WORKDIR /app
ADD . /app

EXPOSE 80

CMD ["python", "run.py"]