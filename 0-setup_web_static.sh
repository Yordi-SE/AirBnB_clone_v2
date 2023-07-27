#!/usr/bin/env bash
if [ ! -d "/data/" ];
then
	sudo mkdir "/data"
fi
if [ ! -d "/data/web_static/" ];
then
	sudo mkdir -p "/data/web_static/"
fi
if [ ! -d "/data/web_static/releases/" ];
then
	sudo mkdir -p "/data/web_static/releases/"
fi
if [ ! -d "/data/web_static/shared/" ];
then
	sudo mkdir -p "/data/web_static/shared/"
fi
mkdir -p /data/web_static/releases
if [ ! -d "/data/web_static/releases/test/" ];
then
	sudo mkdir -p "/data/web_static/releases/test/"
fi
content=\
'
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
'
sudo touch /data/web_static/releases/test/index.html
sudo chown -hR ubuntu:ubuntu /data
echo "$content"  > /data/web_static/releases/test/index.html

if [ -L "/data/web_static/current" ];
then
	rm -f "/data/web_static/current"
fi
ln -s "/data/web_static/releases/test/" "/data/web_static/current"
hostname="$hostname"
config=\
"
server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;

        index index.html index.htm index.nginx-debian.html;
        add_header X-Served-By $hostname;

        server_name _;

        location /redirect_me {
                return 301 https://youtu.be/7VAI73roXaY;
        }

	location /hbnb_static/ {
		alias /data/web_static/current/;
	}
}
"
sudo chown -R "$USER":"$USER" /etc/nginx/sites-available/default
echo "$config" > /etc/nginx/sites-available/default
sudo service nginx restart
