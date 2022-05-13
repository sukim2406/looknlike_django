FROM python:3.10.4

WORKDIR /home/

RUN echo "Docker secret configured"

RUN git clone https://github.com/sukim2406/looknlike_django.git

WORKDIR /home/looknlike_django/

RUN pip install -r requirements.txt

RUN pip install mysqlclient

RUN pip install gunicorn

WORKDIR /home/looknlike_django/looknlike_django/

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=looknlike_django.settings.deploy && python manage.py migrate --settings=looknlike_django.settings.deploy && gunicorn looknlike_django.wsgi --env DJANGO_SETTINGS_MODULE=looknlike_django.settings.deploy --bind 0.0.0.0:8000"]