FROM debian:bookworm-slim

RUN apt update && apt install -y --no-install-recommends python3 python3-pip python3-selenium chromium-driver \
    && rm -rf /var/lib/apt/lists/*

COPY bot /app
WORKDIR /app

ENTRYPOINT ["python3", "-u", "bot.py"]