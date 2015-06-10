#!/bin/bash

DOCKIDS="$*"

LINKS=


port=false
for i in $DOCKIDS; do
   LINKS=' --link '$i':9000'
done

SHARED=`pwd`/shared

sudo docker run -v $SHARED/html:/usr/share/nginx/html:ro $LINKS -p 80:80 -d nginx 

