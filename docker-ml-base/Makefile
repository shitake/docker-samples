env:
	@$(eval VAR_PROJECT_NAME := ml-base)
build: env
	@export PROJECT_NAME=${VAR_PROJECT_NAME}; \
	docker-compose -f docker-compose_poet.yml up -d --build
run: env
	@export PROJECT_NAME=${VAR_PROJECT_NAME}; \
	docker-compose -f docker-compose_poet.yml up -d
down:
	docker-compose -f docker-compose_poet.yml down
