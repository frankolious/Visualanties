install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt
	
post-install:
	echo "post install steps"

lint:
	pylint --disable=R,C *.py devopslib

test:
	python -m pytest -vvv --cov=devopslib .py test_*.py

format:
	black devopslib/*.py 

deploy:
	echo "deploy goes here cntainer work still to complete."

all: install post-install lint format test deploy

