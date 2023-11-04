FROM ustclug/debian:12

RUN apt update && apt install --no-install-recommends -y \
    libvips-dev python3-dev python3-pip build-essential && \
    pip install pyvips==2.2.1 --break-system-packages
COPY server.py /
ENV VIPS_CONCURRENCY 1
CMD ["python3", "/server.py"]
