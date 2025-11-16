FROM ubuntu:22.04

WORKDIR /app

COPY . .

RUN chmod +x ./wisecow.sh

RUN apt update && apt install fortune-mod cowsay netcat-openbsd -y

ENV PATH="/usr/games:${PATH}"

EXPOSE 4499

CMD ["./wisecow.sh"]

