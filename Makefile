build:
	docker build --pull --no-cache --rm -t 'mrjeffapp/sonarqube_new_code' -f Dockerfile .

push:
	docker push 'mrjeffapp/sonarqube_new_code'