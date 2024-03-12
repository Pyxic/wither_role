# VARIABLES
#------------------------------------------
MANAGE = python manage.py

# BASE COMMANDS
# ------------------------------------------------------------------------------
run:
	uvicorn config.app:app_fastapi --reload