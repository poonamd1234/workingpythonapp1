FROM python:3.10-slim

WORKDIR /aiBot

COPY . /aiBot/

RUN apt-get update && \
    apt-get install python3-dev -y && \
    chmod +x envSetup.sh && \
    ./envSetup.sh && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE=django_chatbot.settings

CMD ["/aiBot/env/bin/gunicorn", "django_chatbot.wsgi:application", "--bind", "0.0.0.0:8000"]
