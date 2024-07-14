# VARIABLES
#------------------------------------------
MANAGE = python manage.py

# BASE COMMANDS
# ------------------------------------------------------------------------------
run:
	uvicorn config.app:app_fastapi --reload

migration:
	alembic revision --autogenerate

migrate:
	alembic upgrade head

init:
	$(MANAGE) init


