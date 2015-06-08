#!/bin/sh


SHARED=`pwd`/shared
#docker run -v $SHARED/html:/srv/http:ro -p $1:9000 --link rubbos-db:mysql -d jprjr/php-fpm
docker run -v $SHARED/html:/srv/http:ro -p $1:9000 --link rubbos-db:mysql -d jprjr/php-fpm
