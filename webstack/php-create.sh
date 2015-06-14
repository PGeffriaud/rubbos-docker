#!/bin/sh

# Script bash permettant de lancer un dock PHP

SHARED=`pwd`/shared
sudo docker run -v $SHARED/html:/srv/http:ro -p $1:9000 --link rubbos-db:mysql -d jprjr/php-fpm
