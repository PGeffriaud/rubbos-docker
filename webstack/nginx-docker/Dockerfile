
FROM jprjr/php-fpm

USER root
RUN sed -i 's/;extension=sockets.so/extension=sockets.so/g' /etc/php/php.ini
USER http

ENTRYPOINT ["php-fpm", "-F"]
