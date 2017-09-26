
FROM resin/raspberrypi3-debian:latest

RUN apt-get update && apt-get install -yq python python-pygame sense-hat raspberrypi-bootloader && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

COPY program.py .

ENV INITSYSTEM on

CMD modprobe i2c-dev && python program.py

