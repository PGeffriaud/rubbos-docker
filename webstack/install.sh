#!/bin/sh


SHARED=`pwd`/shared
echo $SHARED

## pull repository images

if [ $0 == "no-pull" ] 
then
	echo "Pulling images"
	sudo docker pull nginx
	sudo docker pull jprjr/php-fpm
fi

# stop existing and running dockers
echo "Stopping running containers..."
sudo docker stop cluster-php
sudo docker rm cluster-php
sudo docker stop cluster-nginx
sudo docker rm cluster-nginx

echo "Run new containers"
sudo docker run --name cluster-php -v $SHARED/html:/srv/http:ro --link rubbos-db:mysql -d jprjr/php-fpm
sudo docker run --name cluster-nginx -v $SHARED/html:/usr/share/nginx/html:ro --link cluster-php:9000 -v $SHARED/conf/nginx.conf:/nginx.conf:ro -d -p 8080:80 nginx nginx -c /nginx.conf
