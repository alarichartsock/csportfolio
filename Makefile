# -- DEV --

SOURCE_DIRS=blog main csportfolio

.PHONY: format
format:
	@echo "Applying black formatting.."
	black ${SOURCE_DIRS}

# -- /DEV --

# -- PROD --

.PHONY: start_http start_https stop_apache free_port_80 free_port_443 kill_gunicorn deploy

# Virtual environment activation
VENV = source /env/csenv/bin/activate
PROJECT_DIR = /home/csportfolio/csportfolio

# Gunicorn HTTP and HTTPS commands
GUNICORN_HTTP = gunicorn csportfolio.wsgi:application --bind 0.0.0.0:80 --reload
GUNICORN_HTTPS = gunicorn csportfolio.wsgi:application --certfile=/etc/letsencrypt/live/alarichartsock.com/fullchain.pem --keyfile=/etc/letsencrypt/live/alarichartsock.com/privkey.pem --bind 0.0.0.0:443 --reload

# Free up port 80 and 443
free_port_80:
	fuser 80/tcp
	fuser 80/tcp -k

free_port_443:
	kill $(lsof -t -i:443)

# Stop Apache
stop_apache:
	sudo systemctl stop apache2

# Start Gunicorn
start_http:
	$(VENV) && cd $(PROJECT_DIR) && $(GUNICORN_HTTP)

start_https:
	$(VENV) && cd $(PROJECT_DIR) && $(GUNICORN_HTTPS)

# Kill Gunicorn process
kill_gunicorn:
	ps ax | grep gunicorn
	pkill gunicorn

# Full deployment process
deploy: stop_apache free_port_80 free_port_443 start_https

# -- /PROD --