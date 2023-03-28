FROM python:3.10.6

WORKDIR /app
COPY . /app
COPY requirements.txt requirements.txt
RUN apt update
RUN pip3 install -r requirements.txt
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
