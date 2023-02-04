FROM python:3.9.16-slim-buster

WORKDIR /var/www/html

ENV PORT 80

RUN pip install --upgrade pip
RUN pip install Flask

CMD ["python", "app.py"]