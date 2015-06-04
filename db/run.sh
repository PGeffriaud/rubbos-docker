__DIR=`pwd`

sudo docker rm -f rubbos-db
sudo docker run --name rubbos-db -p 0.0.0.0:3306:3306 -e MYSQL_ROOT_PASSWORD="" -v $__DIR/data:/var/lib/mysql -d mysql
