FROM php:7.4-apache

RUN docker-php-ext-install mysqli
RUN apt-get update && apt-get install -y libzip-dev unzip && docker-php-ext-install zip

COPY . /var/www/html/

WORKDIR /var/www/html/

EXPOSE 80