build-docker-dev:
	cp weather_app/pip-requirements.txt docker/dev/pip-requirements.txt
	cd docker/dev/ && docker build -t "weather-app/dev" .
	rm -rf docker/dev/pip-requirements.txt

start-dev:
	cd docker/dev/ && docker-compose up -d

stop-dev:
	cd docker/dev/ && docker-compose stop

ssh-dev:
	@if [ "$(shell uname -s)" == "Darwin" ]; then \
		( docker exec -it -w /app/project platzi-kraven bash ); \
	else \
		( ssh -p 2015 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no root@$(DOCKER_IP) ); \
	fi;
