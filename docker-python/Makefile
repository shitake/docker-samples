env:
	@# Change PROJECT_NAME to your favorite name
	@$(eval PROJECT_NAME := myproject)
	@$(eval IMAGE_NAME := poetry)
	@$(eval CONTAINER_NAME := poetry)
	@$(eval SET_WORKDIR := -w /poetry/${PROJECT_NAME})
run:
	@docker run --name ${CONTAINER_NAME} -itd -v `pwd`:/poetry poetry
	@docker exec -it ${SET_WORKDIR} ${CONTAINER_NAME} poetry config virtualenvs.in-project true --local
debug: env
	docker build -t ${IMAGE_NAME} .
	docker rm -f ${CONTAINER_NAME}; docker run --name ${CONTAINER_NAME} -itd ${IMAGE_NAME} bash
# Poetry commands
build-poetry: env
	docker build -t ${IMAGE_NAME} .
rm-poetry:
	docker rm -f poetry
poetry-new: env run
	docker exec -it ${CONTAINER_NAME} poetry new ${PROJECT_NAME}
	docker rm -f ${CONTAINER_NAME}
poetry-install: env run
	docker run --name ${CONTAINER_NAME} -it ${IMAGE_NAME} poetry install
	docker rm -f ${CONTAINER_NAME}
poetry-add: env run
	@echo "INPUT PACKAGE NAMES:"
	@read package_names; \
	docker exec -it ${SET_WORKDIj} ${CONTAINER_NAME} poetry add $${package_names}; \
	docker rm -f ${CONTAINER_NAME}
