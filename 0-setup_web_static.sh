#!/usr/bin/env bash
# Sets up your web servers for the deployment of web_static

# Install nginx on server
if ! which nginx > /dev/null; then
    apt-get -y update
    apt-get -y install nginx
fi

# Create a folder /data/web_static/shared/
PATH_SHARED='/data/web_static/shared/'
if [[ ! -e $PATH_SHARED ]]; then
    mkdir -p /data/web_static/shared/
fi

# Create a folder /data/web_static/releases/test/
PATH_TEST='/data/web_static/releases/test/'
if [[ ! -e $PATH_TEST ]]; then
    mkdir -p /data/web_static/releases/test/
    echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
fi

# Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/
if [[ ! -e /data/web_static/current ]]; then
  ln -s /data/web_static/releases/test/ /data/web_static/current
fi

# Give ownership of the /data/ folder to the ubuntu user AND group
chown -R ubuntu:ubuntu /data/

# Add to the nginx configuration file a location to /hbnb_static
FIND=$(grep "/hbnb_static/" /etc/nginx/sites-available/default)
STRING="\\\n\tlocation /hbnb_static/ {\n\t\t alias /data/web_static/current/;\n\t}\n"
if [[ -z $FIND ]]; then
    sed -i "37i $STRING" /etc/nginx/sites-available/default
fi

# Restart web server to reload new configuration
service nginx restart
