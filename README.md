# Top Movies

## Build

### Compile Sass

	sass \
		--style compressed \
		--no-source-map \
		--watch sass/style.scss:static/stylesheets/style.css

## Launch

	cd app && uvicorn main:app --reload --root-path /api/v1
