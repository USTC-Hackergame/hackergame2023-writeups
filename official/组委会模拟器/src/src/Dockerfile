# Builder: build Vue project
# Why 18.17.1? https://github.com/nodejs/node/issues/49911
FROM node:18.17.1 AS VueBuilder

RUN npm install -g pnpm
ADD frontend /frontend
WORKDIR /frontend
RUN pnpm install --frozen-lockfile && pnpm run build

# modified from tiangolo/uwsgi-nginx-flask (Apache 2.0)
FROM ustclug/debian:12
RUN apt update && apt install --no-install-recommends -y nginx \
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
COPY --from=VueBuilder /frontend/dist /var/www
COPY ./backend/app /app
WORKDIR /app

CMD ["supervisord"]