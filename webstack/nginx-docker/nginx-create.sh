#!/bin/sh

#
# Création du conteneur Nginx avec link aux conteneur PHP
# How to use: nginx-create.sh [dock_id_1]:[port_1] [dock_id_2]:[port_2]
#
SHARED=`pwd`/shared

LINKS=""
# Récupération des variables
for var in "$@"
do
    LINKS=$LINKS"--link $var "
done

sudo docker run -v $SHARED/html:/usr/share/nginx/html:ro --link $LINKS -v $SHARED/conf/nginx.conf:/nginx.conf:ro -p 8080:80 nginx nginx -c /nginx.conf