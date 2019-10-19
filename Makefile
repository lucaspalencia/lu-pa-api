.DEFAULT_GOAL := help

DOCKER_NETWORK_NAME = gamersclub

TEST_REPORTS_PATH=reports
COVERAGE_REPORT_HTML=$(TEST_REPORTS_PATH)/html
COVERAGE_REPORT_XML=$(TEST_REPORTS_PATH)/coverage.xml
TEST_RESULT=$(TEST_REPORTS_PATH)/test-result.xml

help:
	@echo "Usage: make [target] ..."
	@echo "Target:"
	@echo "	build			Build the docker containers"
	@echo "	up			Start the local environment"
	@echo "	down			Stop the local environment"
	@echo "	restart			Restart application"
	@echo "	logs			Show Logs"
	@echo "	lint			Run lint"
	@echo "	shell			Run application shell"
	@echo "	test			Run application tests and coverage"

build: | ensure-network
	docker-compose build
	$(call app-run-no-deps, pipenv install --dev)

up: | ensure-network
	docker-compose up -d

down:
	docker-compose kill
	docker-compose rm -f

restart:
	docker-compose restart

logs:
	docker-compose logs -f

db-init:
	$(call app-run, pipenv run python ./manage.py db init)

db-migrate:
	$(call app-run, pipenv run python ./manage.py db migrate)

db-upgrade:
	$(call app-run, pipenv run python ./manage.py db upgrade)

db-downgrade:
	$(call app-run, pipenv run python ./manage.py db downgrade)

db-seed:
	$(call app-run, pipenv run python ./manage.py seed)

shell: | ensure-network
	$(call app-run, bash)

lint:
	$(call app-run-no-deps, pipenv run flake8 .)

test: | ensure-network
	$(call app-run, pipenv run pytest \
		--cov=. \
		--cov-config=.coveragerc \
		--junitxml=$(TEST_RESULT) \
		--cov-report=html:$(COVERAGE_REPORT_HTML) \
		--cov-report=xml:$(COVERAGE_REPORT_XML))

ensure-network:
ifneq ($(shell docker network ls --filter name=^$(DOCKER_NETWORK_NAME)$$ --format='{{ .Name }}'), $(DOCKER_NETWORK_NAME))
	docker network create $(DOCKER_NETWORK_NAME)
endif

define app-run
	docker-compose run --rm app $1
endef

define app-run-no-deps
	docker-compose run --rm --no-deps app $1
endef
