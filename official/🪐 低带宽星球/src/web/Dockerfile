# modified from tiangolo/uwsgi-nginx-flask (Apache 2.0)
FROM ustclug/debian:12

RUN apt update && apt install --no-install-recommends -y libjxl-devtools libjxl-tools nginx \
    supervisor python3-pip adduser python3-dev gcc
RUN pip install pyOpenSSL==23.2.0 gevent==23.9.1 flask==2.2.5 uWSGI==2.0.22 --break-system-packages
RUN adduser --system --no-create-home --disabled-login --disabled-password --group nginx
COPY uwsgi.ini /etc/uwsgi/uwsgi.ini
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY nginx.conf /etc/nginx/nginx.conf
COPY stop-supervisor.sh /etc/supervisor/stop-supervisor.sh
ENV UWSGI_INI /app/uwsgi.ini
ENV UWSGI_CHEAPER 0
ENV UWSGI_PROCESSES 1
COPY ./app /app
WORKDIR /app

CMD ["supervisord"]