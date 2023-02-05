FROM python:3.9.16-slim-buster

WORKDIR /var/www/html

ENV PORT 80

COPY ./requirements.txt ./requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "app.py"]