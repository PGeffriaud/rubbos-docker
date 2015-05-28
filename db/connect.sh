sudo docker run -it --link rubbos-db:mysql --rm mysql sh -c 'exec mysql -h"$MYSQL_PORT_3306_TCP_ADDR" 
-P"$MYSQL_PORT_3306_TCP_PORT"'
