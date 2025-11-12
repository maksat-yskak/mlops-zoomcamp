export LOCAL_TAG:=$(shell date +"%Y-%m-%d-%H-%M")
export LOCAL_IMAGE_NAME:=stream-model-duration:${LOCAL_TAG}

quality_check:
	isort .
	black .
	pylint --recursive=y .

test:
	pytest tests/

build: quality_check test
	docker build -t ${LOCAL_IMAGE_NAME} .

integration_test: build
	LOCAL_IMAGE_NAME=${LOCAL_IMAGE_NAME}
	bash ./integration-test/run.sh

publish: build integration_test
	LOCAL_IMAGE_NAME=${LOCAL_IMAGE_NAME}
	bash ./scripts/publish.sh

setup:
	pipenv install --dev
	pre-commit install
