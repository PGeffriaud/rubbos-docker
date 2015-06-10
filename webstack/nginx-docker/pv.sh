#!/bin/sh
export PV=`sudo tail /var/log/nginx/access.log | pv -lr >/dev/null`
