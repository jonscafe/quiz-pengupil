FROM php:7.4-apache

RUN apt-get update && apt-get install -y python3 python3-pip \
    && ln -s /usr/bin/python3 /usr/bin/python

RUN docker-php-ext-install mysqli
RUN apt-get update && apt-get install -y libzip-dev unzip && docker-php-ext-install zip
RUN pip install selenium

COPY . /var/www/html/
WORKDIR /var/www/html/
EXPOSE 80