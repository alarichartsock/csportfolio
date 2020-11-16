To use the deployment server, become root in tmux, deploy virtual environment in project directory with
     source /env/csenv/bin/activate
 and run
     gunicorn csportfolio.wsgi:application --bind 0.0.0.0:80
in the project directory.

sudo systemctl1 stop apache2

Todo:
     Fix mobile incompatibilities
     Add email contact form
     Add a blog page
     Switch to HTTPS



