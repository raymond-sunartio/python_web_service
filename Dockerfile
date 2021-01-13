FROM python:3.8.6

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONIOENCODING=UTF-8

ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8

RUN groupadd --system django \
  && useradd --system --uid 900 --create-home --gid django django

RUN mkdir /app
ADD . /app

RUN pip install --upgrade pip
RUN pip install -r /app/requirements/dev.txt
RUN ln -s /app/run_tests.sh /usr/bin/run_tests.sh

WORKDIR /app
USER django

CMD gunicorn --env DJANGO_SETTINGS_MODULE=config.settings.dev -b :80 config.wsgi
