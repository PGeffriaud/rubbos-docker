#!/bin/sh


SHARED=`pwd`/shared
DOCK_ID=""
sudo docker run -v $SHARED/html:/srv/http:ro --link rubbos-db:mysql -d jprjr/php-fpm