# Top Movies

## Build

### Compile Sass

	sass \
		--style compressed \
		--no-source-map \
		--watch sass/style.scss:static/stylesheets/style.css

### Set nginx config

	sudo cp configs/nginx.conf configs/backend_proxy.conf /etc/nginx/ && sudo nginx -s reload

## Launch

	cd app && uvicorn main:app --reload --proxy-headers --forwarded-allow-ips="*"
