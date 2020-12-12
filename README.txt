To use the deployment server, become root, deploy virtual environment in project directory with

$ source /env/csenv/bin/activate

and run

key: /etc/letsencrypt/live/alarichartsock.com/fullchain.pem
privkey: /etc/letsencrypt/live/alarichartsock.com/privkey.pem

$ gunicorn csportfolio.wsgi:application --bind 0.0.0.0:80 --reload # for HTTP

$ gunicorn csportfolio.wsgi:application --certfile=/etc/letsencrypt/live/alarichartsock.com/fullchain.pem --keyfile=/etc/letsencrypt/live/alarichartsock.com/privkey.pem --bind 0.0.0.0:443 --reload # for HTTPS

in the project directory located at /home/csportfolio/csportfolio

To free up port 80 after boot:

$ fuser 80/tcp
$ fuser 80/tcp -k

$ kill$(lsof -t -i:"443")

To stop apache after boot: 

$ sudo systemctl stop apache2

Todo:
     Fix mobile incompatibilities
     Add email contact form
     Add a blog page
     Switch to HTTPS
