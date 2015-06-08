__DIR=`pwd`

sudo docker rm -f rubbos-db
sudo docker run --name rubbos-db -e MYSQL_ROOT_PASSWORD="d" -d -v $__DIR/data:/var/lib/mysql mysql
