FROM debian:buster-slim

RUN apt-get update -y

RUN mkdir -p /var/www/html/

COPY ./database.config /var/www/html/database.config

RUN printf "Username: admin\nPassword: production_admin\n" > /var/www/html/database.config