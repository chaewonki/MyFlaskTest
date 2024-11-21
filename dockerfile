FROM python:3.10-slim-buster

WORKDIR /flaskapp

COPY . /flaskapp/
COPY requirements.txt /flaskapp/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5002

CMD ["gunicorn", "-b", "0.0.0.0:5001", "flaskapp:app"]