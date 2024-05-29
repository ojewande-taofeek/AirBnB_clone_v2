#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static.
sudo apt update 
sudo apt install -y nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo cat <<EOF > /data/web_static/releases/test/index.html
<html>
  <head>
  </head>
  <body>
  My HTML Page
  </body>
</html>
EOF
ln -s -f /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data
sudo ed /etc/nginx/sites-available/default <<EOF
/index index.html*/a

	location /hbnb_static {
		alias /data/web_static/current/;
	}

.
w
q
EOF
sudo service nginx restart
