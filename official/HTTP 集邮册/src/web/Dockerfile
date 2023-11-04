FROM tiangolo/uwsgi-nginx-flask:python3.11

ENV UWSGI_PROCESSES 1
ENV UWSGI_CHEAPER 0
RUN pip install pyOpenSSL==23.2.0 gevent==23.9.1
COPY ./app /app