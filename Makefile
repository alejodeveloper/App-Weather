build-docker-dev:
	cp -a weather_app/ docker/dev/weather_app
	cd docker/dev/ && docker build -t "weather-app/dev" .
	rm -rf docker/dev/weather_app

start-dev:
	cd docker/dev/ && docker-compose up -d

stop-dev:
	cd docker/dev/ && docker-compose stop
