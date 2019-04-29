SHELL		:= /usr/bin/env bash
PYTHON	:= pipenv run python

up:
	@docker-compose up -d

follow:
	@docker-compose logs --follow --tail 10

start: up
	@$(PYTHON) -m aiohttpdemo_polls.main


.PHONY: up
