FROM mysql 
MAINTAINER Alexandre LEBRUN 
ENV MYSQL_ROOT_PASSWORD="docker"

# Copy the database schema to the /data directory
ADD comments.data moderator_log.data old_comments.data old_stories.data stories.data submissions.data users.data /tmp/
ADD load.sql rubbos.sql /tmp/
ADD run_db.sh init_db.sh /tmp/ 

# init_db will create the default
# database from epcis_schema.sql, then
# stop mysqld, and finally copy the /var/lib/mysql directory
# to default_mysql_db.tar.gz
RUN /tmp/init_db.sh

# run_db starts mysqld, but first it checks
# to see if the /var/lib/mysql directory is empty, if
# it is it is seeded with default_mysql_db.tar.gz before
# the mysql is fired up

ENTRYPOINT "/usr/bin/mysqld_safe"
