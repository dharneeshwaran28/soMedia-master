# Dockerfile.login
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput --settings=soMedia.settings_login

EXPOSE 8080

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080", "--settings=soMedia.settings_login"]



