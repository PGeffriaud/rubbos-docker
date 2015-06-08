daemon off;
 
user  root;
worker_processes  1;
 
error_log  /var/log/nginx/error.log warn;
pid        /var/run/nginx.pid;
 
 
events {
    worker_connections  1024;
}
 
 
http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;
    
    upstream php-docker {    
        @@@WORKERS@@@
    }
 
    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';
 
    access_log  /var/log/nginx/access.log  main;
 
    sendfile        on;
    #tcp_nopush     on;
 
    keepalive_timeout  65;
 
    gzip  on;
 
    server {
        listen       80;
        server_name  localhost;
 
        location / {
            root   /srv/http;
            index  index.html index.htm;
        }
 
        #error_page  404              /404.html;
 
        # redirect server error pages to the static page /50x.html
        #
        #error_page   500 502 503 504  /50x.html;
        #location = /50x.html {
        #    root   /usr/share/nginx/html;
        #}
 
        # Pass PHP scripts to PHP-FPM
        location ~* \.php$ {
            fastcgi_index   index.php;
            fastcgi_pass    php-docker;
            #fastcgi_pass   unix:/var/run/php-fpm/php-fpm.sock;
            include         fastcgi_params;
            fastcgi_param   SCRIPT_FILENAME    /srv/http$fastcgi_script_name;
            fastcgi_param   SCRIPT_NAME        $fastcgi_script_name;
        }    
 
        # deny access to .htaccess files, if Apache's document root
        # concurs with nginx's one
        location ~ /\.ht {
            deny  all;
        }
    }
 
}