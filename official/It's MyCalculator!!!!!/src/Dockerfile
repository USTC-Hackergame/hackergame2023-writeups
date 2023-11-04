FROM debian:bookworm-slim

RUN apt-get update && apt-get install -y --no-install-recommends python3 libfl2

RUN echo "flag{this_is_a_fake_flag}" > /flag

ADD src /src
ADD MyCalculator /src/MyCalculator
WORKDIR /src

CMD ["python3", "/src/server.py"]
